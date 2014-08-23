#!/bin/bash

# Find the install dir
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PRJ_DIR="$DIR/../"

# Set up the virtual env
echo "Installing the virtual environment to :$PRJ_DIR/env"
virtualenv $PRJ_DIR/env
source $PRJ_DIR/env/bin/activate
pip install -r $PRJ_DIR/requirements.txt
