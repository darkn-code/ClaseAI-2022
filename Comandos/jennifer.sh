#!/bin/bash
cd Jennifer
git pull origin master
python3 Jennifer.py
python3 Jennifer.py
git commit -am "datos Jenn"
git push origin master
cd ..
