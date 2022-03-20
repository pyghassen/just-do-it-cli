import pytest

from just_do_it_cli.config import (
    DoneTaskProperties,
    InProgressTaskProperties,
    PendingTaskProperties,
    Status,
)
from just_do_it_cli.helpers import (
    get_board_suffix,
    get_done_percentage,
    get_number_of_done_tasks,
    get_number_of_tasks_in_progress,
    get_task_properties,
    get_tasks,
    get_total_number_of_pending_tasks,
)


@pytest.mark.parametrize(
    'tasks,expected',
    [
        ({}, 0),
        ({'1': {'status': Status.IN_PROGRESS}}, 0),
        ({'1': {'status': Status.PENDING}}, 0),
        ({'1': {'status': Status.DONE}}, 1),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.PENDING},
            },
            1,
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.DONE},
            },
            2,
        ),
    ],
)
def test_get_number_of_done_tasks_returns_total_done_tasks(tasks, expected):
    assert get_number_of_done_tasks(tasks) == expected


@pytest.mark.parametrize(
    'tasks,expected',
    [
        ({}, 0),
        ({'1': {'status': Status.DONE}}, 0),
        ({'1': {'status': Status.PENDING}}, 0),
        ({'1': {'status': Status.IN_PROGRESS}}, 1),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.PENDING},
            },
            1,
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.IN_PROGRESS},
            },
            2,
        ),
    ],
)
def test_get_number_of_tasks_in_progress_returns_the_correct_number(
    tasks, expected
):
    assert get_number_of_tasks_in_progress(tasks) == expected


@pytest.mark.parametrize(
    'tasks,expected',
    [
        ({}, '[0/0]'),
        ({'1': {'status': Status.PENDING}}, '[0/1]'),
        ({'1': {'status': Status.IN_PROGRESS}}, '[0/1]'),
        ({'1': {'status': Status.DONE}}, '[1/1]'),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.IN_PROGRESS},
                '3': {'status': Status.PENDING},
            },
            '[1/3]',
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.DONE},
                '3': {'status': Status.IN_PROGRESS},
            },
            '[2/3]',
        ),
        (
            {
                '1': {'status': Status.DONE},
                '2': {'status': Status.DONE},
                '3': {'status': Status.DONE},
            },
            '[3/3]',
        ),
    ],
)
def test_get_board_suffix(tasks, expected):
    assert get_board_suffix(tasks) == expected


@pytest.mark.parametrize(
    'data,expected',
    [
        ({'1': {'name': 'Board 1', 'tasks': {}}}, {}),
        (
            {'1': {'name': 'Board 1', 'tasks': {'1': {'name': 'Task 1'}}}},
            {'1': {'name': 'Task 1'}},
        ),
        (
            {
                '1': {
                    'name': 'Board 1',
                    'tasks': {'1': {'name': 'Task 1'}, '2': {'name': 'Task 2'}},
                }
            },
            {'1': {'name': 'Task 1'}, '2': {'name': 'Task 2'}},
        ),
        (
            {
                '1': {
                    'name': 'Board 1',
                    'tasks': {'1': {'name': 'Task 1'}, '2': {'name': 'Task 2'}},
                },
                '2': {'name': 'Board 2', 'tasks': {'3': {'name': 'Task 3'}}},
            },
            {
                '1': {'name': 'Task 1'},
                '2': {'name': 'Task 2'},
                '3': {'name': 'Task 3'},
            },
        ),
    ],
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
    ],
)
def test_get_done_percentage_should_return_the_correct_percentage(
    total_number_of_done_tasks, total_number_of_tasks, expected
):
    assert (
        get_done_percentage(total_number_of_done_tasks, total_number_of_tasks)
        == expected
    )


@pytest.mark.parametrize(
    'total_number_of_tasks,total_number_of_done_tasks,'
    'total_number_of_tasks_in_progress,expected',
    [
        (0, 0, 0, 0),
        (10, 10, 0, 0),
        (10, 0, 10, 0),
        (10, 5, 5, 0),
        (10, 5, 0, 5),
        (10, 0, 5, 5),
        (10, 0, 0, 10),
    ],
)
def test_get_total_number_of_pending_tasks(
    total_number_of_tasks,
    total_number_of_done_tasks,
    total_number_of_tasks_in_progress,
    expected,
):
    assert (
        get_total_number_of_pending_tasks(
            total_number_of_tasks,
            total_number_of_done_tasks,
            total_number_of_tasks_in_progress,
        )
        == expected
    )


@pytest.mark.parametrize(
    'status,expected',
    [
        (Status.PENDING, PendingTaskProperties),
        (Status.IN_PROGRESS, InProgressTaskProperties),
        (Status.DONE, DoneTaskProperties),
    ],
)
def test_get_task_properties(status, expected):
    assert get_task_properties(status) == expected
