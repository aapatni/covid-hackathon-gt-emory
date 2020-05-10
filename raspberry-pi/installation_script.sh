#!/bin/bash
sudo apt-get install python3-pip
pip3 install -r requirements.txt
cd ~
pip3 install awscli --upgrade --user
export PATH=/home/pi/.local/bin:$PATH
aws configure set aws_access_key_id 'AKIAJRFOLRO6MACCCL6A'
aws configure set aws_secret_access_key '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'
aws configure set aws default.region 'us-west-2'