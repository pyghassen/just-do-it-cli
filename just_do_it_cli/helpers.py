"""
The helpers module contains a bunch of utility functions.

These functions are needed to display all the boards and the tasks when
`justdoit list` command is called.
"""
from typing import Any

from just_do_it_cli.config import Status, STATUS_TASK_PROPERTIES_MAP


def get_number_of_done_tasks(tasks) -> int:
    """
    Get tasks dictionary and return the number of done tasks.

    Check status value of each task and return the number of tasks which has
    done as its status.

    Args:
    ----
        tasks (dict): A dictionary containing dictionaries of all the tasks.

    Returns
    -------
        The number of tasks which has done as its status.
    """
    return len(
        [task for task in tasks.values() if task['status'] == Status.DONE]
    )


def get_number_of_tasks_in_progress(tasks: dict) -> int:
    """
    Get tasks dictionary and return the number of tasks in progress.

    Check status value of each task and return the number of tasks which has
    in progress as its status.

    Args:
    ----
        tasks (dict): A dictionary containing dictionaries of all the tasks.

    Returns
    -------
        The number of tasks which has in progress as its status.
    """
    return len(
        [
            task
            for task in tasks.values()
            if task['status'] == Status.IN_PROGRESS
        ]
    )


def get_board_suffix(tasks: dict) -> str:
    """
    Get tasks dictionary and return the board suffix.

    Caculate the total number of tasks and how many were done then return a
    string with both results bewtween two brackets and separated by a slash.

    Args:
    ----
        tasks (dict): A dictionary containing dictionaries of all the tasks.

    Returns
    -------
        How many tasks were done out of the total number of tasks between [].
    """
    number_of_tasks = len(tasks)
    number_of_done_tasks = get_number_of_done_tasks(tasks)
    return f'[{number_of_done_tasks}/{number_of_tasks}]'


def get_tasks(boards: dict) -> dict:
    """
    Take boards dictionaries and return tasks dictionaries.

    Extract tasks dictionary from the all boards and merge them all together.

    Args:
    ----
        boards (dict): A dictionary containing dictionaries of all the boards.

    Returns
    -------
        A dictionary containing dictionaries of all the tasks.

    """
    tasks = {}
    for board in boards.values():
        tasks.update(board['tasks'])
    return tasks


def get_done_percentage(
    total_number_of_done_tasks: int, total_number_of_tasks: int
) -> int:
    """
    Get the percentange of done tasks among all the tasks.

    Caculate the percentange of tasks done when given the total number of tasks
    and total done then round it up then return it as an int.

    Args:
    ----
        total_number_of_done_tasks (int): The total number of the done tasks.
        total_number_of_tasks (int): The total number of all tasks.

    Returns
    -------
        An integer which represents the percentage of done tasks.
    """
    return (
        round(total_number_of_done_tasks / total_number_of_tasks * 100)
        if total_number_of_tasks > 0
        else 0
    )


def get_total_number_of_pending_tasks(
    total_number_of_tasks: int,
    total_number_of_done_tasks: int,
    total_number_of_tasks_in_progress: int,
) -> int:
    """
    Get total number of the pending tasks.

    Caculate the total number of pending tasks when given the total number of
    tasks, plus the total number of the done and in progress task then return
    the result.

    Args:
    ----
        total_number_of_tasks (int): The total number of all tasks.
        total_number_of_done_tasks (int): The total number of the done tasks.
        total_number_of_tasks_in_progress (int): The total number of tasks in
            progress.

    Returns
    -------
        An integer which represents the total number of the pending tasks.
    """
    return (
        total_number_of_tasks
        - total_number_of_done_tasks
        - total_number_of_tasks_in_progress
    )


def get_task_properties(status: int) -> Any:
    """
    Take a status and return the task properties class.

    Return the proper TaskProperties class depending on the provided status.

    Args:
    ----
        status (int): The task status value.

    Returns
    -------
        Task properties class.
    """
    return STATUS_TASK_PROPERTIES_MAP[status]
