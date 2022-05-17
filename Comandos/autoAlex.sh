#!/bin/bash

git pull origin master --allow-unrelated-histories
python Alejnadro.py
git commit -am "Datos Exteriores Alejandro"
git push origin master
