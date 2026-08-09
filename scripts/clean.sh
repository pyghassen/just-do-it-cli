#!/bin/sh
set -e

echo "Removing the python and pytest cache files"
find . -type d -name __pycache__ -exec rm -rf {} +
rm -rf .pytest_cache/
