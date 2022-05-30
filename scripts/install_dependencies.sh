#!/bin/bash
easy_install pip
pip install "poetry==$POETRY_VERSION"
cd /home/ec2-user/page-turn-decipher
pip install -r requirements.txt
