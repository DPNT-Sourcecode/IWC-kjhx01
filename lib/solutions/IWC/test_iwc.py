from .task_types import TaskSubmission, TaskDispatch
from .queue_solution_legacy import Queue
from .queue_solution_entrypoint import QueueSolutionEntrypoint
from datetime import datetime, timedelta


def test_init() -> None:
    queue = QueueSolutionEntrypoint()
    tasks = [
        TaskSubmission(
            "companies_house",
            1,
            datetime.now(),
        ),
        TaskSubmission(
            "companies_house",
            3,
            datetime.now() + timedelta(minutes=90),
        ),
        TaskSubmission(
            "companies_house",
            2,
            datetime.now() - timedelta(minutes=40),
        ),
    ]

    assert queue.size() == 3

    assert queue.dequeue().user_id == 2
    assert queue.size() == 2
    assert queue.dequeue().user_id == 1
    assert queue.size() == 1
    assert queue.dequeue().user_id == 3
    assert queue.size() == 0
    assert queue.dequeue() == None
