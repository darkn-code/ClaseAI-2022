#!/bin/bash
pwd
cd Jennifer/
git pull origin master
python3 Jennifer.py
git commit -am "jenn-dato"
git push origin master
