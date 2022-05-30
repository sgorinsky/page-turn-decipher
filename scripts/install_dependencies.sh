#!/bin/bash
yum update -y
pip install "poetry==$POETRY_VERSION"
poetry export -f requirements.txt > requirements.txt
pip install -r requirements.txt
