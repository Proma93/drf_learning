from celery import shared_task
from django.utils import timezone
from django.apps import apps
import logging
from prometheus_client import Counter

logger = logging.getLogger(__name__)

# Lazy loading models ensures tasks work even if Celery starts before Django fully loads
Todo = apps.get_model('home', 'Todo')
TimingTodo = apps.get_model('home', 'TimingTodo')
Reminder = apps.get_model('home', 'Reminder')

# Prometheus metrics
reminders_created_total = Counter(
    "todo_reminders_created_total",
    "Total number of reminders created by Celery tasks"
)

due_todos_checked_total = Counter(
    "todo_due_todos_checked_total",
    "Total number of TimingTodos checked for upcoming reminders"
)

new_due_reminders_total = Counter(
    "todo_new_due_reminders_total",
    "Total number of new reminders created for due todos"
)


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def create_todo_reminder(self, todo_uid):
    """
    Create a reminder in DB when a new Todo is created.
    This is triggered via perform_create() in TodoModelViewSet.
    """
    try:
        todo = Todo.objects.get(uid=todo_uid)
        reminder = Reminder.objects.create(
            todo=todo,
            message=f"Background reminder: Todo '{todo.todo_title}' created"
        )
        logger.info(f"Reminder created for Todo {todo_uid}: {reminder.message}")

        # Increment Prometheus metric
        reminders_created_total.inc()

        return {"status": "success", "reminder_uid": reminder.uid}

    except Todo.DoesNotExist:
        logger.warning(f"Todo {todo_uid} not found. Skipping reminder.")
        return {"status": "failed", "reason": "Todo not found"}
    except Exception as e:
        logger.error(f"Failed to create reminder for Todo {todo_uid}: {e}")
        raise  # retried because of autoretry_for


@shared_task(bind=True)
def mark_due_todos(self):
    """
    Periodically check for TimingTodos due in next 15 minutes
    and create reminders for them.
    """
    now = timezone.now()
    window_start = now
    window_end = now + timezone.timedelta(minutes=15)

    upcoming = TimingTodo.objects.filter(
        start_time__gte=window_start,
        start_time__lte=window_end
    )

    # Increment metric for checked todos
    due_todos_checked_total.inc(upcoming.count())

    logger.info(f"Checking {upcoming.count()} upcoming todos between {window_start} and {window_end}")

    created_reminders = []
    for timing in upcoming:
        reminder, created = Reminder.objects.get_or_create(
            todo=timing.todo,
            message=f"Your task '{timing.todo.todo_title}' is due at {timing.start_time}"
        )
        if created:
            created_reminders.append(reminder.uid)
            # Increment metric for new reminders
            new_due_reminders_total.inc()

    logger.info(f"{len(created_reminders)} new reminders created.")
    return {
        "status": "success",
        "new_reminders_count": len(created_reminders),
        "reminder_uids": created_reminders
    }
