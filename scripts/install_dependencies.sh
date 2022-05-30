#!/bin/bash
easy_install pip
export POETRY_VERSION=1.1.8
pip install "poetry==$POETRY_VERSION"
cd /home/ec2-user/page-turn-decipher
pip install -r requirements.txt
