#!/bin/bash
git pull origin master --allow-unrelated-histories
python Alejnadro.py
git add "basedatos/datos.csv"
git commit -m "Datos Exteriores Alejandro"
git push origin master
