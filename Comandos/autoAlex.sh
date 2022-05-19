#!/bin/bash

git pull origin master --allow-unrelated-histories
python3 Alejnadro.py
git add .
git commit -m "Datos Exteriores Alejandro"
git push origin master
