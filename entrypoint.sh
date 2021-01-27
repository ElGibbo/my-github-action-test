#!/bin/sh -l

echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"
cd /
python main.py
#ls -l
