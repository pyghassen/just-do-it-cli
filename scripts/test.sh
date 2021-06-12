#!/bin/sh
set -e

python -m pytest --cov=app --no-cov-on-fail --cov-report term-missing
