import os
import time
import logging
from prometheus_client import Counter, Histogram, start_http_server
from celery.signals import worker_process_init, task_prerun, task_postrun, task_failure

logger = logging.getLogger(__name__)

# Metrics
TASKS_STARTED = Counter(
    "celery_tasks_started_total", "Total started Celery tasks", ["task"]
)
TASKS_SUCCEEDED = Counter(
    "celery_tasks_succeeded_total", "Total succeeded Celery tasks", ["task"]
)
TASKS_FAILED = Counter(
    "celery_tasks_failed_total", "Total failed Celery tasks", ["task"]
)
TASK_RUNTIME = Histogram(
    "celery_task_runtime_seconds", "Celery task runtime in seconds", ["task"]
)

# Keep per-task start times
_runtime_cache = {}

@worker_process_init.connect
def _start_metrics_server(**_kwargs):
    port = int(os.getenv("CELERY_METRICS_PORT", "9091"))
    start_http_server(port, addr="0.0.0.0")
    logger.info(f"Prometheus metrics server started on port {port}")

@task_prerun.connect
def _on_prerun(task_id=None, task=None, **_kwargs):
    TASKS_STARTED.labels(task=task.name).inc()
    _runtime_cache[task_id] = time.perf_counter()

@task_postrun.connect
def _on_postrun(task_id=None, task=None, **_kwargs):
    start = _runtime_cache.pop(task_id, None)
    if start is not None:
        TASK_RUNTIME.labels(task=task.name).observe(time.perf_counter() - start)
    TASKS_SUCCEEDED.labels(task=task.name).inc()

@task_failure.connect
def _on_failure(task_id=None, exception=None, task=None, **_kwargs):
    # Count failure; runtime (if any) will be captured in postrun if it fires
    TASKS_FAILED.labels(task=task.name).inc()