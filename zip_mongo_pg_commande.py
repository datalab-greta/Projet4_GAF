#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:05:59 2019

@author: corot
"""

from zip_mongo import all_zip
from mongo_pg import mongo_php

auth_data=input("taper authentification database (ex:Database) : ")
nom_bdd=input("taper le nom de la bdd mongo à créer : " )
collection = input("taper le nom de la collection mongo à créer : ")
#zip_zip="/home/corot/Bureau/Projet 4/*.zip"
#fi_cnf="/home/corot/Bureau/Projet 4/datalab.cnf"
#MOOC_GRP_LeVraiRhum
zip_zip=input("copie colle le chemin de tes zip, (ps ne met pas les guillemets) : ")
fi_cnf=input("copie colle le chemin de ton cnf : ")

table_pg=input("quel est le nom de votre table phpgadmin (ex forum2 : ")

all_zip(fi_cnf,zip_zip,nom_bdd,collection,auth_data)

mongo_php(fi_cnf,nom_bdd,collection,auth_data,table_pg)