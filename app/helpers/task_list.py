from app.config import (
    DoneTaskProperties,
    InProgressTaskProperties,
    PendingTaskProperties,
    Status,
)


def get_number_of_done_tasks(task_list):
    return len(
        [task for task in task_list.values() if task['status'] == Status.DONE]
    )


def get_number_of_tasks_in_progress(task_list):
    return len(
        [
            task
            for task in task_list.values()
            if task['status'] == Status.IN_PROGRESS
        ]
    )


def get_board_suffix(task_list):
    number_of_tasks = len(task_list)
    number_of_done_tasks = get_number_of_done_tasks(task_list)
    return f'[{number_of_done_tasks}/{number_of_tasks}]'


def get_tasks(board_data):
    tasks = {}
    for board in board_data.values():
        tasks.update(board['tasks'])
    return tasks


def get_done_percentage(total_number_of_done_tasks, total_number_of_tasks):
    return (
        round(total_number_of_done_tasks / total_number_of_tasks * 100)
        if total_number_of_tasks > 0
        else 0
    )


def get_total_number_of_pending_tasks(
        total_number_of_tasks,
        total_number_of_done_tasks,
        total_number_of_tasks_in_progress,
    ):
    return (
        total_number_of_tasks
        - total_number_of_done_tasks
        - total_number_of_tasks_in_progress
    )


def get_task_properties(status):
    if status == Status.PENDING:
        status_properties = PendingTaskProperties
    elif status == Status.IN_PROGRESS:
        status_properties = InProgressTaskProperties
    else:
        status_properties = DoneTaskProperties
    return status_properties
