#!/bin/bash
python Alejnadro.py

git pull origin master --allow-unrelated-histories
git add "basedatos/datos.csv"
git commit -m "Datos Exteriores Alejandro"
git push origin master
