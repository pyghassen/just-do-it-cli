#!/bin/sh
set -e

echo "Setting up Just Do It CLI .."
echo "Setting up the production enviroment.."
echo "STORAGE_FILE_PATH='app/storage.json'" > app/.env
echo "Done"
echo "Setting up the test enviroment.."
echo "STORAGE_FILE_PATH='tests/storage.json''" > tests/.env
echo "Done"
