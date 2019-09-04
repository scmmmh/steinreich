#!/bin/bash

# An optional script to be run before building
if [ -f 'pre-build' ]
then
    ./pre-build
fi

git pull
export PIPENV_VENV_IN_PROJECT=True
pipenv install
pipenv run pelican -s publishconf.py -o output -d content

# An optional script to be run after building
if [ -f 'post-build' ]
then
    ./post-build
fi
