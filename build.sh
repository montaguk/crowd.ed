#!/usr/bin/bash

virtualenv env
source env/bin/activate
python --version
pip --version
pip install -r requirements.txt --use-mirrors
#nosetests
python ./test.py

#Build Docs
echo "Building Docs"
pushd docs
make html
