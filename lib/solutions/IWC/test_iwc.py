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
    for task in tasks:
        queue.enqueue(task)

    assert queue.size() == 3
    assert queue.dequeue().user_id == 2
    assert queue.size() == 2
    assert queue.dequeue().user_id == 1
    assert queue.size() == 1
    assert queue.dequeue().user_id == 3
    assert queue.size() == 0
    assert queue.dequeue() == None


def test_de_duplication() -> None:
    queue = QueueSolutionEntrypoint()
    tasks = [
        TaskSubmission(
            user_id=1,
            provider="bank_statements",
            timestamp="2025-10-20 12:00:00",
        ),
        TaskSubmission(
            user_id=1,
            provider="bank_statements",
            timestamp="2025-10-20 12:05:00",
        ),
        TaskSubmission(
            user_id=1,
            provider="id_verification",
            timestamp="2025-10-20 12:05:00",
        ),
    ]
    for task in tasks:
        queue.enqueue(task)

    assert queue.size() == 2
    dequed_task = queue.dequeue()
    dequed_task.user_id == 1
    dequed_task.provider == "bank_statements"

    dequed_task = queue.dequeue()
    dequed_task.user_id == 1
    dequed_task.provider == "id_verification"

    assert queue.dequeue() == None
    assert queue.size() == 0
