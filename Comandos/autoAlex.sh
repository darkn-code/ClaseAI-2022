#!/bin/bash
cd ..
git pull origin master 
python3 Alejnadro.py
python3 Alejnadro.py
git add .
git commit -m "Datos Exteriores Alejandro"
git push origin master
