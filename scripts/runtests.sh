#!/usr/bin/env bash
# Run from the root directory: ./scripts/runtests.sh
#
# Auto discovers and runs all the tests (doctests and unittests).
#
# On the command line, just pass additional options to throw to nosetests.
#
# Usage: http://nose.readthedocs.org/en/latest/usage.html
#
# Common options:
# -v --verbose 
# --nocapture
# -s <module_name> => shuts down auto discovering
# --doctest-extension=rst  => add doctests from .rst files
#
# Coverage and nose-cov
# --cov-report=html => coverage report in html
# added --cov-report term-missing because show_missing in .coveragerc has no effect as of today: bug?

nosetests --with-doctest --doctest-extension=rst --with-cov --cov-config .coveragerc --cov-report term-missing $@