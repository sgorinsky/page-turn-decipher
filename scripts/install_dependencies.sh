#!/bin/bash
echo "Installing dependencies..."
easy_install pip
echo "pip installed!"
export POETRY_VERSION=1.1.8
pip install "poetry==$POETRY_VERSION"
echo "poetry installed!"
cd /home/ec2-user/page-turn-decipher
echo "now at page-turn-decipher: $(pwd)"
pip install -r requirements.txt
echo "deps installed!"
