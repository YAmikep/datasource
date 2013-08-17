#!/usr/bin/env bash
# Run from the root directory: ./scripts/clean.sh
#
# Clean all the temporary files created when running tests or packaging

cleanpyc="find . | grep '.pyc$' | xargs rm -f"
cleantmpfiles="rm -rf dist;rm -rf *.egg-info;rm -rf .tox;rm -rf htmlcov; rm .coverage"

eval $cleanpyc
eval $cleantmpfiles
