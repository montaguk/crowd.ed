#!/usr/bin/bash

# Run Unit Tests
nosetests

#Build Docs
echo "Building Docs"
pushd docs
make html
