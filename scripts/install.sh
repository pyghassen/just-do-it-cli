#!/bin/sh
set -e
echo "Setting up Just Do It CLI .."
if [ "$ENV" = "CI" ]
then
    echo "Setting up the test enviroment.."
    STORAGE_FILE_PATH=tests/storage.json
    ENV_FILE_PATH=tests/.env
    REQUIREMENT_FILE_PATH=requirements/test.txt
else
    echo "Setting up the production enviroment.."
    JUST_DO_IT_DIRECTORY=$HOME/.just-do-it-cli
    if [ ! -d "$JUST_DO_IT_DIRECTORY" ]; then
      mkdir "$JUST_DO_IT_DIRECTORY"
    fi
    STORAGE_FILE_PATH=$JUST_DO_IT_DIRECTORY/storage.json
    ENV_FILE_PATH=app/.env
    REQUIREMENT_FILE_PATH=requirements/common.txt
fi
echo "STORAGE_FILE_PATH='$STORAGE_FILE_PATH'" > "$ENV_FILE_PATH"
FIXTURES='{"boards":{}, "tasks_index": {}, "last_board_id": null, "last_task_id": null}'
echo $FIXTURES > "$STORAGE_FILE_PATH"
echo "Installing requirements"
python3 -m pip install -r $REQUIREMENT_FILE_PATH
echo "Installing Just Do It CLI"
python3 -m pip install -e .
echo "Installtion is done, please type 'justdoit --help' to start"
