#!/usr/bin/env bash
#
# Auto discovers and runs all the tests (doctests and unittests).
#
# On the command line, just pass additional options to throw to nosetests.
#
# Usage: http://nose.readthedocs.org/en/latest/usage.html
# Common options:
# -v --verbose 
# --nocapture
# -s <module_name> => shuts down auto discovering

nosetests --with-doctest $@
