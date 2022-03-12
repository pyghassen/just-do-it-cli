#!/bin/bash
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
    ENV_FILE_PATH=just_do_it_cli/.env
    REQUIREMENT_FILE_PATH=requirements/common.txt
fi
echo "STORAGE_FILE_PATH='$STORAGE_FILE_PATH'" > "$ENV_FILE_PATH"
FIXTURES='{"boards":{}, "tasks_index": {}, "last_board_id": null, "last_task_id": null}'
echo $FIXTURES > $STORAGE_FILE_PATH
echo "Installing requirements"
python3 -m pip install -r $REQUIREMENT_FILE_PATH
echo "Installing Just Do It CLI"
echo "#Added by Just DO It CLI" >> ~/.bashrc
echo "export PATH=\$PATH:~/.local/bin"  >> ~/.bashrc
source ~/.bashrc
python3 -m pip install .
echo "Before you start you need to run 'source ~/.bashrc' so ~/.local/bin' is added to the system path."
echo "Installtion is done now, please type 'justdoit --help' to start, but "
