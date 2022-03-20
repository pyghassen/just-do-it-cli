from unittest.mock import patch

from click.testing import CliRunner

from just_do_it_cli.cli import main
from just_do_it_cli.config import STORAGE_FILE_PATH
from just_do_it_cli.storage import JsonStorage


def setup_function(function):  # pylint: disable=W0613
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    storage.write(
        {
            "boards": {},
            "boards_index": {},
            "tasks_index": {},
            "last_board_id": None,
            "last_task_id": None,
            "secret": None,
            "is_connected": False
            # "secret": "6cf9ec924b9c51d409e39ebae4de378cb544240e",
            # "is_connected": True
        }
    )


def test_create_board_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    assert result.exit_code == 0
    expected_output = f'Board #1. "{board_name}" was added\n'
    assert result.output == expected_output


def test_edit_board_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    new_board_name = 'My New Board'
    result = runner.invoke(main, ['edit-board', board_id, new_board_name])
    expected_output = (
        f'Board #{board_id}. changed name from "{board_name}" to '
        f'"{new_board_name}"\n'
    )

    assert result.exit_code == 0
    assert result.output == expected_output


def test_delete_board_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    result = runner.invoke(main, ['delete-board', board_id])
    expected_output = f'Board #{board_id}. {board_name} was deleted\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_create_task_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(main, ['create-task', board_id, description])
    task_id = '1'
    expected_output = f'Task #{task_id}. "{description}" was added\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_edit_task_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    old_description = 'My first task'
    result = runner.invoke(main, ['create-task', board_id, old_description])
    task_id = '1'
    description = 'My first task updated'
    result = runner.invoke(main, ['edit-task', task_id, description])
    expected_output = (
        f'Task #{task_id}. changed description from "{old_description}" to '
        f'"{description}"\n'
    )

    assert result.exit_code == 0
    assert result.output == expected_output


def test_delete_task_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(main, ['create-task', board_id, description])
    task_id = '1'
    result = runner.invoke(main, ['delete-task', task_id])
    expected_output = f'Task #{task_id}. "{description}" was deleted\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_begin_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(main, ['create-task', board_id, description])
    task_id = '1'
    result = runner.invoke(main, ['begin', task_id])
    expected_output = f'Task #{task_id}. "{description}" is started\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_check_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(main, ['create-task', board_id, description])
    task_id = '1'
    result = runner.invoke(main, ['check', task_id])
    expected_output = f'Task #{task_id}. "{description}" is done\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_priority_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(main, ['create-task', board_id, description])
    task_id = '1'
    priority = '5'
    result = runner.invoke(main, ['priority', task_id, priority])
    expected_output = f'Task #{task_id}. "{description}" priority was updated\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_priority_command_should_fail():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(main, ['create-board', board_name])
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(main, ['create-task', board_id, description])
    task_id = '1'
    invalid_priority = '10'

    result = runner.invoke(main, ['priority', task_id, invalid_priority])
    expected_output = (
        f'{invalid_priority} is invalid value for priority must be in the '
        'range of 1 to 5.\n'
    )

    assert result.exit_code == 0
    assert result.output == expected_output


def test_list_command():

    runner = CliRunner()
    result = runner.invoke(main, ['create-board', 'Board 1'])
    result = runner.invoke(main, ['create-board', 'Board 2'])
    result = runner.invoke(main, ['create-task', '1', 'Task 1'])
    result = runner.invoke(main, ['create-task', '1', 'Task 2'])
    result = runner.invoke(main, ['create-task', '2', 'Task 3'])
    result = runner.invoke(main, ['create-task', '2', 'Task 4'])
    result = runner.invoke(main, ['create-task', '2', 'Task 5'])

    result = runner.invoke(main, ['begin', '4'])
    result = runner.invoke(main, ['check', '5'])
    result = runner.invoke(main, ['priority', '1', '1'])
    result = runner.invoke(main, ['priority', '2', '2'])
    result = runner.invoke(main, ['priority', '4', '4'])
    result = runner.invoke(main, ['priority', '5', '5'])

    result = runner.invoke(main, ['list'])
    expected_output = '''
  1. Board 1 [0/2]
	1. ◻ Task 1⛄
	2. ◻ Task 2🌧️

  2. Board 2 [1/3]
	3. ◻ Task 3🌊
	4. … Task 4🔥
	5. ✔ Task 5🌋

  20% of all tasks complete.
  1 done  1 in progress · 3 pending

  Priority Keys:
    1. Trivial ⛄ · 2. Minor 🌧️ · 3. Major 🌊 · 4. Critical 🔥 · 5. Blocker 🌋

'''

    assert result.exit_code == 0
    assert result.output == expected_output
