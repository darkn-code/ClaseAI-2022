#!/bin/bash
cd ~/Alex
git mull origin master
python3 alexInfoBlock.py
python3 alexInfoBlock.py
git add .
git commit -m "Datos Exteriores Agrupados  Alejandro"
git push origin master
