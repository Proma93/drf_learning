import uuid
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta: 
        abstract = True

class Todo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name='todos')
    session_key = models.CharField(max_length=40, null=True, blank=True)
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.todo_title} - {self.user or self.session_key}"   

class TimingTodo(BaseModel):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='timingtodos')
    schedule_date = models.DateField(help_text="Date on which the todo is scheduled")
    start_time = models.TimeField(null=True, blank=True, help_text="When the task starts")
    end_time = models.TimeField(null=True, blank=True, help_text="When the task ends")
    note = models.TextField(null=True, blank=True, help_text="Optional notes about the timing")

class Reminder(BaseModel):  # inherit BaseModel for UUID + timestamps consistency
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='reminders')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.todo.todo_title}"        