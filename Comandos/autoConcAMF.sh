#!/bin/bash
cd ~/Alex
git pull origin master
python3 concatenadoDatosAMF.py
git add .
git commit -m "Datos Exteriores Agrupados  Alejandro"
git push origin master
