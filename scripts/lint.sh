#!/bin/sh
set -e

echo "Running pylint .."
# black --check --diff app
# isort --check-only app
#pylint app
pylint -d C0114,C0115,C0116,R0903 app

if [ "$ENV" = "CI" ]
then
  echo "Running codecov .."
  codecov
fi
