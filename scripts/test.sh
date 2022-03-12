#!/bin/sh
set -e

python -m pytest -vvv -x -s --cov=just_do_it_cli --no-cov-on-fail --cov-report term-missing
