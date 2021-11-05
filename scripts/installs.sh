#!/bin/bash

echo "Running installs.sh"

# Error Handling
set -o errexit
set -o verbose

# Install local CDK CLI version
npm install -g aws-cdk

# Needed for cdk.out during synth step
cdk synth

# Requirements
pip install -r requirements.txt

echo "Installs completed"