#!/bin/bash
set -e
pip install -r requirements.txt
sudo apt-get install -y postgresql
sudo service postgresql start
