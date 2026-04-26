from .task_types import TaskSubmission, TaskDispatch
from .queue_solution_legacy import Queue
from .queue_solution_entrypoint import QueueSolutionEntrypoint
from datetime import datetime, timedelta


def test_init() -> None:
    queue = QueueSolutionEntrypoint()
    task_submission_companies_house = TaskSubmission(
        "companies_house",
        1,
        datetime.now(),
    )
    queue.enqueue(task_submission_companies_house)
    assert queue.dequeue() == task_submission_companies_house



