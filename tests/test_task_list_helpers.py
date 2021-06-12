import pytest

from app.config import (
    DoneTaskProperties,
    InProgressTaskProperties,
    PendingTaskProperties,
    Status
)
from app.helpers.task_list import (
    get_board_suffix,
    get_done_percentage,
    get_number_of_done_tasks,
    get_number_of_tasks_in_progress,
    get_task_properties,
    get_tasks,
    get_total_number_of_pending_tasks
)


@pytest.mark.parametrize(
    'task_list,expected',
    [
        ({}, 0),
        ({'1': {'status': Status.IN_PROGRESS}}, 0),
        ({'1': {'status': Status.PENDING}}, 0),
        ({'1': {'status': Status.DONE}}, 1),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.PENDING}
            },
            1
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.DONE}
            },
            2
        ),
    ]
)
def test_get_number_of_done_tasks_returns_total_done_tasks(task_list, expected):
    assert get_number_of_done_tasks(task_list) == expected


@pytest.mark.parametrize(
    'task_list,expected',
    [
        ({}, 0),
        ({'1': {'status': Status.DONE}}, 0),
        ({'1': {'status': Status.PENDING}}, 0),
        ({'1': {'status': Status.IN_PROGRESS}}, 1),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.PENDING}
            },
            1
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.IN_PROGRESS}
            },
            2
        ),
    ]
)
def test_get_number_of_tasks_in_progress_returns_total_tasks_in_progress(task_list, expected):
    assert get_number_of_tasks_in_progress(task_list) == expected


@pytest.mark.parametrize(
    'task_list,expected',
    [
        ({}, '[0/0]'),
        ({'1': {'status': Status.PENDING}}, '[0/1]'),
        ({'1': {'status': Status.IN_PROGRESS}}, '[0/1]'),
        ({'1': {'status': Status.DONE}}, '[1/1]'),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.PENDING}
            },
            '[1/3]'
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.DONE},
                '3': {'status': Status.IN_PROGRESS}
            },
            '[2/3]'
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.DONE},
                '3': {'status': Status.DONE}
            },
            '[3/3]'
        ),
    ]
)
def test_get_board_suffix(task_list, expected):
    assert get_board_suffix(task_list) == expected


@pytest.mark.parametrize(
    'data,expected',
    [
        (
            {
                '1': {
                    'name': 'Board 1',
                    'tasks': {}
                }
            },
            {}
        ),
        (
            {
                '1': {
                    'name': 'Board 1',
                    'tasks': {'1': {'name': 'Task 1'}}
                }
            },
            {'1': {'name': 'Task 1'}}
        ),
        (
            {
                '1': {
                    'name': 'Board 1',
                    'tasks': {
                        '1': {'name': 'Task 1'},
                        '2': {'name': 'Task 2'}
                    }
                }
            },
            {
                '1': {'name': 'Task 1'},
                '2': {'name': 'Task 2'}
            }
        ),
        (
            {
                '1': {
                    'name': 'Board 1',
                    'tasks': {
                        '1': {'name': 'Task 1'},
                        '2': {'name': 'Task 2'}
                    },
                },
                '2': {
                    'name': 'Board 2',
                    'tasks': {
                        '3': {'name': 'Task 3'}
                    }
                }
            },
            {
                '1': {'name': 'Task 1'},
                '2': {'name': 'Task 2'},
                '3': {'name': 'Task 3'}
            }
        )
    ]
)
def test_get_tasks(data, expected):
    assert get_tasks(data) == expected


@pytest.mark.parametrize(
    'total_number_of_done_tasks,total_number_of_tasks,expected',
    [
        (0, 0, 0),
        (0, 10, 0),
        (1, 3, 33),
        (5, 10, 50),
        (4, 6, 67),
        (7, 10, 70),
        (10, 10, 100),
    ]
)
def test_get_done_percentage(total_number_of_done_tasks, total_number_of_tasks, expected):
    assert get_done_percentage(total_number_of_done_tasks, total_number_of_tasks) == expected


@pytest.mark.parametrize(
    'total_number_of_tasks,total_number_of_done_tasks,total_number_of_tasks_in_progress,expected',
    [
        (0, 0, 0, 0),
        (10, 10, 0, 0),
        (10, 0, 10, 0),
        (10, 5, 5, 0),
        (10, 5, 0, 5),
        (10, 0, 5, 5),
        (10, 0, 0, 10),
    ]
)
def test_get_total_number_of_pending_tasks(total_number_of_tasks, total_number_of_done_tasks, total_number_of_tasks_in_progress, expected):
    assert (
        get_total_number_of_pending_tasks(
            total_number_of_tasks,
            total_number_of_done_tasks,
            total_number_of_tasks_in_progress
        ) == expected
    )

@pytest.mark.parametrize(
    'status,expected',
    [
        (Status.PENDING, PendingTaskProperties),
        (Status.IN_PROGRESS, InProgressTaskProperties),
        (Status.DONE, DoneTaskProperties),
    ]
)
def test_get_task_properties(status, expected):
    assert get_task_properties(status) == expected
