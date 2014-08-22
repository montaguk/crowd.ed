#!/usr/bin/bash

nosetests
python ./test.py

#Build Docs
echo "Building Docs"
pushd docs
make html
