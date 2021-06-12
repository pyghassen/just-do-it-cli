from click.testing import CliRunner

from app.config import STORAGE_FILE_PATH
from app.main import cli
from app.storage import JsonStorage


def setup_function(function):
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    storage.write({})


def test_create_board_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    assert result.exit_code == 0
    expected_output = f'Board #1. "{board_name}" was added\n'
    assert result.output == expected_output


def test_edit_board_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    new_board_name = 'My New Board'
    result = runner.invoke(
        cli,
        ['edit-board', board_id, new_board_name]
    )
    expected_output = (
        f'Board #{board_id}. changed name from "{board_name}" to '
        f'"{new_board_name}"\n'
    )

    assert result.exit_code == 0
    assert result.output == expected_output


def test_delete_board_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    result = runner.invoke(
        cli,
        ['delete-board', board_id]
    )
    expected_output = f'Board #{board_id}. {board_name} was deleted\n'

    assert result.exit_code == 0
    assert result.output == expected_output

def test_create_task_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(
        cli,
        ['create-task', board_id, description]
    )
    task_id = '1'
    expected_output = f'Task #{task_id}. "{description}" was added\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_edit_task_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    old_description = 'My first task'
    result = runner.invoke(
        cli,
        ['create-task', board_id, old_description]
    )
    task_id = '1'
    description = 'My first task updated'
    result = runner.invoke(
        cli,
        ['edit-task', task_id, description]
    )
    expected_output = (
        f'Task #{task_id}. changed description from "{old_description}" to '
        f'"{description}"\n'
    )

    assert result.exit_code == 0
    assert result.output == expected_output


def test_delete_task_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(
        cli,
        ['create-task', board_id, description]
    )
    task_id = '1'
    result = runner.invoke(
        cli,
        ['delete-task', task_id]
    )
    expected_output = f'Task #{task_id}. "{description}" was deleted\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_begin_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(
        cli,
        ['create-task', board_id, description]
    )
    task_id = '1'
    result = runner.invoke(
        cli,
        ['begin', task_id]
    )
    expected_output = f'Task #{task_id}. "{description}" is started\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_check_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(
        cli,
        ['create-task', board_id, description]
    )
    task_id = '1'
    result = runner.invoke(
        cli,
        ['check', task_id]
    )
    expected_output = f'Task #{task_id}. "{description}" is done\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_priority_command():
    board_name = 'My Board'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name]
    )
    board_id = '1'
    description = 'My first task'
    result = runner.invoke(
        cli,
        ['create-task', board_id, description]
    )
    task_id = '1'
    priority = '5'
    result = runner.invoke(
        cli,
        ['priority', task_id, priority]
    )
    expected_output = f'Task #{task_id}. "{description}" priority was updated\n'

    assert result.exit_code == 0
    assert result.output == expected_output


def test_list_command():
    board_name_1 = 'Board 1'
    board_name_2 = 'Board 2'
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ['create-board', board_name_1]
    )
    result = runner.invoke(
        cli,
        ['create-board', board_name_2]
    )
    board_1_id = '1'
    board_2_id = '2'
    description_1 = 'Task 1'
    description_2 = 'Task 2'
    description_3 = 'Task 3'
    description_4 = 'Task 4'
    description_5 = 'Task 5'
    result = runner.invoke(
        cli,
        ['create-task', board_1_id, description_1]
    )
    result = runner.invoke(
        cli,
        ['create-task', board_1_id, description_2]
    )
    result = runner.invoke(
        cli,
        ['create-task', board_2_id, description_3]
    )
    result = runner.invoke(
        cli,
        ['create-task', board_2_id, description_4]
    )
    result = runner.invoke(
        cli,
        ['create-task', board_2_id, description_5]
    )

    task_1_id = '1'
    task_2_id = '2'
    task_3_id = '3'
    task_4_id = '4'
    task_5_id = '5'

    result = runner.invoke(
        cli,
        ['begin', task_4_id]
    )
    result = runner.invoke(
        cli,
        ['check', task_5_id]
    )
    priority_1 = '1'
    priority_2 = '2'
    priority_3 = '4'
    priority_4 = '5'
    result = runner.invoke(
        cli,
        ['priority', task_1_id, priority_1]
    )
    result = runner.invoke(
        cli,
        ['priority', task_2_id, priority_2]
    )
    result = runner.invoke(
        cli,
        ['priority', task_4_id, priority_3]
    )
    result = runner.invoke(
        cli,
        ['priority', task_5_id, priority_4]
    )

    result = runner.invoke(
        cli,
        ['list']
    )
    expected_output = (
'''
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

''')

    assert result.exit_code == 0
    assert result.output == expected_output
