#!/bin/bash
cd ~/Alex
python3 concatenadoDatosAMF.py
git add .
git commit -m "Datos Exteriores Agrupados  Alejandro"
git pull origin master
git push origin master
