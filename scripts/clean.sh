#!/bin/sh
set -e

echo "Removing the python and pytest cache files"
find . -type d -name __pycache__ | xargs rm -rf
rm -rf .pytest_cache/
