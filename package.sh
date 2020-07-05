#!/usr/bin/env bash

# Install dependencies with:
# exctract package to destination
# python3 -m pip install --no-index --find-links=wheelhouse -r requirements.txt


set -o errexit
set -o pipefail
set -o nounset


working_dir="$(dirname ${0})"
if [[ -z ${1+x} ]]; then
    echo "Environment name is not specified yet it is a required parameter. Make sure you provide one and try again."
    exit 1
fi

environment=${1}

echo "Setting up wheelhouse for ${environment}"
rm -rf wheelhouse
mkdir wheelhouse
python3 -m pip wheel --wheel-dir=wheelhouse -r requirements.txt
echo "Packaging source code and wheelhouse dependencies"
python3 setup.py sdist