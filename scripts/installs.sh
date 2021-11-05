#!/bin/bash

echo "Running installs.sh"

# Error Handling
set -o errexit
set -o verbose

# Install local CDK CLI version
npm install -g aws-cdk


# Requirements
pip install -r requirements.txt

echo "Installs completed"