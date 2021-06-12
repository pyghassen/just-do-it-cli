from tempfile import NamedTemporaryFile
from unittest.mock import MagicMock

import pytest

from app.controllers import BoardController, TaskController
from app.storage import JsonStorage


@pytest.mark.parametrize(
    'data,expected_id',
    [({}, 0), ({1: {}}, 1), ({1: {}, 2: {}}, 2),({1: {}, 2: {}, 5: {}}, 5)]
)
def test_board_controller_get_last_id(data, expected_id):
    mocked_storage = MagicMock()
    mocked_storage.read.return_value = data
    board_controller = BoardController(storage=mocked_storage)

    assert board_controller.get_last_id() == expected_id


def test_board_controller_create_should_return_board():
    mocked_storage = MagicMock()
    board_name = 'My Board'
    board_controller = BoardController(storage=mocked_storage)
    board = board_controller.create(name=board_name)

    mocked_storage.write.assert_called_once()
    assert board.name == board_name

def test_board_controller_delete_should_remove_board_from_storage():
    board_id = 1
    data = {
        board_id: {
            'name': 'My Board',
            'id': None,
            'tasks': {}
        }
    }
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        storage = JsonStorage(file_path=temp_file.name)
    storage.write(data)
    board_controller = BoardController(storage=storage)
    board_controller.delete(board_id)

    assert board_id not in board_controller.storage.read()

def test_board_controller_edit_should_update_board_name():
    board_id = '1'
    new_board_name = 'My Meetings'
    data = {
        board_id: {
            'name': 'My Board',
            'tasks': {}
        }
    }
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        storage = JsonStorage(file_path=temp_file.name)
    storage.write(data)
    board_controller = BoardController(storage=storage)
    board = board_controller.edit(board_id, new_board_name)

    assert board.name == new_board_name

def test_board_controller_get_board_by_id_should_return_board_from_storage():
    mocked_storage = MagicMock()
    board_id = '1'
    mocked_data = {
        board_id: {
            'name': 'My Board',
            'tasks': {}
        }
    }
    mocked_storage.read.return_value = mocked_data
    board = BoardController.get_board_by_id(
        mocked_storage, board_id
    )

    assert board.to_dict() == mocked_data


@pytest.mark.parametrize(
    'data,expected_id',
    [
        (
            {'1': {'name': 'My Board', 'tasks': {}}},
            0
        ),
        (
            {'1': {'name': 'My Board', 'tasks': {'1': {'name': 'Task 1'}}}},
            1
        ),
        (
            {
                '1': {'name': 'My Board', 'tasks': {
                    '1': {'name': 'Task 1'},
                    '2': {'name': 'Task 2'}
                    }
                }
            },
            2
        ),
        (
            {
                '1': {'name': 'My Board', 'tasks': {'1': {'name': 'Task 1'}}},
                '2': {'name': 'My Board', 'tasks': {'2': {'name': 'Task 2'}}}
            },
            2
        ),
        (
            {
                '1': {'name': 'My Board', 'tasks': {
                    '10': {'name': 'Task 1'},
                    '20': {'name': 'Task 2'}
                    }
                }
            },
            20
        ),
        (
            {
                '1': {'name': 'My Board', 'tasks': {'10': {'name': 'Task 1'}}},
                '2': {'name': 'My Board', 'tasks': {'15': {'name': 'Task 2'}}}
            },
            15
        )
    ]
)
def test_board_controller_get_last_id(data, expected_id):
    mocked_storage = MagicMock()
    mocked_storage.read.return_value = data
    task_controller = TaskController(storage=mocked_storage)

    assert task_controller.get_last_id() == expected_id


def test_task_controller_create_should_return_task():
    board_id = '1'
    data = {
        board_id: {
            'name': 'My Board',
            'tasks': {}
        }
    }
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        storage = JsonStorage(file_path=temp_file.name)
    storage.write(data)
    task_description = 'Finish writing the tests'
    task_controller = TaskController(storage=storage)
    task = task_controller.create(board_id, description=task_description)

    assert task.description == task_description
    assert any(
        [
            task.id in board_data['tasks']
            for board_data in task_controller.storage.read().values()
        ]
    )

def test_task_controller_get_task_by_id_should_return_board_from_storage():
    mocked_storage = MagicMock()
    task_id = '1'
    mocked_task_data = {
        task_id: {
            'description': 'Task 1',
            'priority': 5,
            'status': 1
        }
    }
    mocked_storage.read.return_value = {
        '1': {
            'name': 'My Board',
            'tasks': {**mocked_task_data}
        }
    }
    task = TaskController.get_task_by_id(
        mocked_storage, task_id
    )

    assert task.to_dict() == mocked_task_data


def test_task_controller_edit_should_update_task_description():
    task_id = '1'
    mocked_task_data = {
        task_id: {
            'description': 'Task 1',
            'priority': 5,
            'status': 1
        }
    }
    data = {
        '1': {
            'name': 'My Board',
            'tasks': {**mocked_task_data}
        }
    }
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        storage = JsonStorage(file_path=temp_file.name)
    storage.write(data)
    task_controller = TaskController(storage=storage)
    new_task_description = 'Task 1 renamed'
    task = task_controller.edit(task_id, new_task_description)

    assert task.description == new_task_description

def test_task_controller_delete_should_remove_task_from_storage():
    task_id = '1'
    mocked_task_data = {
        task_id: {
            'description': 'Task 1',
            'priority': 5,
            'status': 1
        }
    }
    data = {
        '1': {
            'name': 'My Board',
            'tasks': {**mocked_task_data}
        }
    }
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        storage = JsonStorage(file_path=temp_file.name)
    storage.write(data)
    task_controller = TaskController(storage=storage)
    task_controller.delete(task_id)

    assert not any(
        [
            task_id in board_data['tasks']
            for board_data in task_controller.storage.read().values()
        ]
    )
    # TODO: Remove all the temp files.
