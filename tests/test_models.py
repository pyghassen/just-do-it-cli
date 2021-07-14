import pytest

from app.models import Board, Task


@pytest.fixture
def storage_data():
    return {
        'boards': {
            '1': {
                'name': 'Coding',
                'tasks': {
                    '1': {
                        'description': (
                            'Create justdoit push command to sync local data '
                            'with the API'
                        ),
                        'priority': 4,
                        'board': '1',
                        'status': 3
                    }
                }
            }
        }
    }


@pytest.fixture
def board_data():
    return {
        'id': 1,
        'name': 'My board',
        'tasks': {}
    }


@pytest.fixture
def task_data():
    return {
        'id': 1,
        'description': 'My task',
        'priority': 5,
        'status': 1,
    }


def test_board_constructor(board_data):  # pylint: disable=W0621
    board = Board(**board_data)

    assert board.id == board_data['id']
    assert board.name == board_data['name']
    assert board.tasks == board_data['tasks']


def test_board_to_dict_method(board_data):  # pylint: disable=W0621
    board = Board(**board_data)
    expected_data = {
        board_data['id']: {
            'name': board_data['name'],
            'tasks': board_data['tasks']
        }
    }
    assert board.to_dict() == expected_data


def test_task_constructor(task_data):  # pylint: disable=W0621
    task = Task(**task_data)

    assert task.id == task_data['id']
    assert task.description == task_data['description']
    assert task.priority == task_data['priority']
    assert task.status == task_data['status']


def test_task_to_dict_method(task_data):  # pylint: disable=W0621
    task = Task(**task_data)
    expected_data = {
        task_data['id']: {
            'description': task_data['description'],
            'priority': task_data['priority'],
            'status': task_data['status']
        }
    }
    assert task.to_dict() == expected_data
