import json
import os
from tempfile import NamedTemporaryFile

import pytest

from app.storage import JsonStorage


@pytest.fixture
def data():
    return {
        'boards': {
            '1': {'name': 'My Board'},
            'last_board_id': 1,
            'last_task_id': None,
            'tasks_index': {}
        }
    }


@pytest.fixture
def file_path(data):  # pylint: disable=W0621
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        json.dump(data, temp_file)
    yield temp_file.name
    os.remove(temp_file.name)


def test_should_read_from_json_file_and_return_dict(file_path, data):  # pylint: disable=W0621
    storage = JsonStorage(file_path=file_path)
    assert storage.read() == data


def test_should_write_to_json_file_and_return(file_path):  # pylint: disable=W0621
    _data = {
        'boards': {'1': {'name': 'My Board'}, '2': {'name': 'Meetings'}},
        'last_board_id': 2,
        'last_task_id': None,
        'tasks_index': {}
    }
    storage = JsonStorage(file_path=file_path)
    storage.write(_data)
    assert storage.read() == _data
