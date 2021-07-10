#!/bin/sh
set -e

echo "Running pylint .."
# black --check --diff app
# isort --check-only app
pylint app

if [ "$ENV" = "CI" ]
then
  echo "Running codecov .."
  codecov
fi
