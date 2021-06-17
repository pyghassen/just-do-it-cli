import click

from app.config import PRIORIY_ICONS_MAP, STORAGE_FILE_PATH, Status
from app.controllers import BoardController, TaskController
from app.helpers.task_list import (
    get_board_suffix,
    get_done_percentage,
    get_number_of_done_tasks,
    get_number_of_tasks_in_progress,
    get_task_properties,
    get_tasks,
    get_total_number_of_pending_tasks,
)
from app.storage import JsonStorage


@click.group()
def cli():
    pass


@cli.command()
def list():  # pylint: disable=R0914,W0622
    """List all boards and tasks."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    data = storage.read()
    for board_id, board_data in data.items():
        board_suffix = get_board_suffix(board_data['tasks'])
        click.echo()
        message = f'  {board_id}. {board_data["name"]} {board_suffix}'
        click.secho(message, fg='yellow', bold=True)
        for task_id, task_data in board_data['tasks'].items():
            task_properties = get_task_properties(task_data['status'])
            priority_icon = PRIORIY_ICONS_MAP[task_data['priority']]
            description = task_data['description']
            message = f'\t{task_id}. {task_properties.icon} '
            click.secho(
                click.style(
                    message,
                    fg=task_properties.foreground_color,
                    bold=task_properties.bold
                )
                + click.style(
                    f'{description}',
                    fg=task_properties.foreground_color,
                    bold=task_properties.bold,
                    underline=task_properties.underline,
                    strikethrough=task_properties.strikethrough,
                )
                + click.style(f'{priority_icon}')
            )
    click.echo()
    tasks = get_tasks(data)
    total_number_of_tasks = len(tasks)
    total_number_of_done_tasks = get_number_of_done_tasks(tasks)
    total_number_of_tasks_in_progress = get_number_of_tasks_in_progress(tasks)
    done_percentage = get_done_percentage(
        total_number_of_done_tasks, total_number_of_tasks
    )
    total_number_of_pending_tasks = get_total_number_of_pending_tasks(
        total_number_of_tasks,
        total_number_of_done_tasks,
        total_number_of_tasks_in_progress,
    )
    click.secho(
        f'  {done_percentage}% of all tasks complete.',
        fg='green' if done_percentage > 50 else 'red'
    )
    click.secho(
        click.style(f'  {total_number_of_done_tasks} done', fg='green')
        + click.style(
            f'  {total_number_of_tasks_in_progress} in progress', fg='blue'
        )
        + click.style(f' · {total_number_of_pending_tasks} pending', fg='red')
    )
    click.echo()
    click.secho('  Priority Keys:', fg='red')
    message = (
        '    1. Trivial ⛄ · 2. Minor 🌧️ · 3. Major 🌊 · 4. Critical 🔥 · '
        '5. Blocker 🌋'
    )
    click.secho(message, fg='red')
    click.echo()


@cli.command()
@click.argument('name', type=str)
def create_board(name):
    """Create Board."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    board_controller = BoardController(storage)
    board = board_controller.create(name)
    message = f'Board #{board.id}. "{name}" was added'
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('board_id', type=str)
@click.argument('Name', type=str)
def edit_board(board_id, name):
    """Edit board."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    board_controller = BoardController(storage)
    board = BoardController.get_board_by_id(storage, board_id)
    old_name = board.name
    board = board_controller.edit(board_id, name)
    message = f'Board #{board_id}. changed name from "{old_name}" to "{name}"'
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('board_id', type=str)
def delete_board(board_id):
    """Delete board."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    board_controller = BoardController(storage)
    board = BoardController.get_board_by_id(storage, board_id)
    board_controller.delete(board_id)
    message = f'Board #{board_id}. {board.name} was deleted'
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('board-id', type=str)
@click.argument('description', type=str)
def create_task(board_id, description):
    """
    Create Task.

    Example:
        justdoit create-task BOARD_ID "TASK DESCRIPTION"

    Sample:
        justdoit create-task 1 "My first task"
    """
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    task_controller = TaskController(storage)
    task = task_controller.create(board_id, description)
    message = f'Task #{task.id}. "{description}" was added'
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('task_id', type=str)
@click.argument('description', type=str)
def edit_task(task_id, description):
    """Edit task."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    task = TaskController.get_task_by_id(storage, task_id)
    old_description = task.description
    task_controller = TaskController(storage)
    task = task_controller.edit(task_id, description)
    message = (
        f'Task #{task_id}. changed description from "{old_description}" to '
        f'"{description}"'
    )
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('task_id', type=str)
def delete_task(task_id):
    """Delete Task."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    task = TaskController.get_task_by_id(storage, task_id)
    description = task.description
    task_controller = TaskController(storage)
    task_controller.delete(task_id)
    message = f'Task #{task_id}. "{description}" was deleted'
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('task_id', type=str)
def begin(task_id):
    """Delete task."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    task = TaskController.get_task_by_id(storage, task_id)
    task_controller = TaskController(storage)
    task_controller.edit(task_id, status=Status.IN_PROGRESS)
    message = f'Task #{task_id}. "{task.description}" is started'
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('task_id', type=str)
def check(task_id):
    """Mark task as done."""
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    task = TaskController.get_task_by_id(storage, task_id)
    task_controller = TaskController(storage)
    task_controller.edit(task_id, status=Status.DONE)
    message = f'Task #{task_id}. "{task.description}" is done'
    click.secho(message, bold=True, fg='green')


@cli.command()
@click.argument('task_id', type=str)
@click.argument('priority', type=str)
def priority(task_id, priority):  # pylint: disable=W0621
    """Set task priority from 1 to 5.

    1. Trivial ⛄ · 2. Minor 🌧️ · 3. Major 🌊 · 4. Critical 🔥 · 5. Blocker 🌋

    Example:
        justdoit priority TASK_ID PRIORIY

    Sample:
        justdoit priority 20 5
    """
    storage = JsonStorage(file_path=STORAGE_FILE_PATH)
    task = TaskController.get_task_by_id(storage, task_id)
    task_controller = TaskController(storage)
    task_controller.edit(task_id, priority=int(priority))
    message = f'Task #{task_id}. "{task.description}" priority was updated'
    click.secho(message, bold=True, fg='green')
