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
    JUST_DO_IT_VENV=$JUST_DO_IT_DIRECTORY/venv
    if [ ! -d "$JUST_DO_IT_DIRECTORY" ]; then
      mkdir "$JUST_DO_IT_DIRECTORY"
    fi
    if [ ! -x "$JUST_DO_IT_VENV/bin/python" ]; then
      python3 -m venv "$JUST_DO_IT_VENV"
    fi
    STORAGE_FILE_PATH=$JUST_DO_IT_DIRECTORY/storage.json
    ENV_FILE_PATH=just_do_it_cli/.env
    REQUIREMENT_FILE_PATH=requirements/common.txt
    INSTALL_PYTHON=$JUST_DO_IT_VENV/bin/python
fi
echo "STORAGE_FILE_PATH='$STORAGE_FILE_PATH'" > "$ENV_FILE_PATH"
FIXTURES='{"boards": {}, "boards_index": {}, "tasks_index": {}, "last_board_id": null, "last_task_id": null}'
echo $FIXTURES > $STORAGE_FILE_PATH
echo "Installing requirements"
if [ "$ENV" = "CI" ]; then
    INSTALL_PYTHON=python3
fi
"$INSTALL_PYTHON" -m pip install -r "$REQUIREMENT_FILE_PATH"
echo "Installing Just Do It CLI"
"$INSTALL_PYTHON" -m pip install .
if [ "$ENV" != "CI" ]; then
    mkdir -p "$HOME/.local/bin"
    printf '#!/bin/sh\nexec "%s/bin/justdoit" "$@"\n' "$JUST_DO_IT_VENV" \
      > "$HOME/.local/bin/justdoit"
    chmod +x "$HOME/.local/bin/justdoit"
    if ! grep -Fq 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.bashrc"; then
      printf '\n# Just Do It CLI\nexport PATH="$HOME/.local/bin:$PATH"\n' >> "$HOME/.bashrc"
    fi
    export PATH="$HOME/.local/bin:$PATH"
fi
JUSTDOIT_COMMAND=$(command -v justdoit)
if [ "$ENV" != "CI" ]; then
    echo "Installing shell completion"
    mkdir -p "$HOME/.local/share/bash-completion/completions"
    _JUSTDOIT_COMPLETE=bash_source "$JUSTDOIT_COMMAND" \
      > "$HOME/.local/share/bash-completion/completions/justdoit"
    if ! grep -Fq 'source "$HOME/.local/share/bash-completion/completions/justdoit"' "$HOME/.bashrc"; then
      printf '\n# Just Do It CLI completion\nsource "$HOME/.local/share/bash-completion/completions/justdoit"\n' >> "$HOME/.bashrc"
    fi

    mkdir -p "$HOME/.local/share/zsh/site-functions"
    _JUSTDOIT_COMPLETE=zsh_source "$JUSTDOIT_COMMAND" \
      > "$HOME/.local/share/zsh/site-functions/_justdoit"
fi
echo "Before you start you need to run 'source ~/.bashrc' so ~/.local/bin' is added to the system path."
echo "Installtion is done now, please type 'justdoit --help' to start, but "
