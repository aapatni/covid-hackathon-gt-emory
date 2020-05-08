#!/bin/bash
cd ~
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws configure set aws_access_key_id 'AKIAJRFOLRO6MACCCL6A'
aws configure set aws_secret_access_key '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'
aws configure set aws default.region 'us-west-2'

