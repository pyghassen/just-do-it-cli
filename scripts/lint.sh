#!/bin/sh
set -e

echo "Running pylint .."
# black --check --diff app
# isort --check-only app
pylint just_do_it_cli

if [ "$ENV" = "CI" ]
then
  echo "Running codecov .."
  codecov
fi
