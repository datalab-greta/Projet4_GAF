#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:43:19 2019

@author: corot
"""

import requests, pprint, os
import libarchive
from pymongo import MongoClient # librairie qui va bien
import configparser
import pprint, os, pandas

from sqlalchemy import create_engine
from sqlalchemy.sql import text
import sys, glob, zipfile, json, ast, demjson,os
from demjson import decode
import configparser
from pymongo import MongoClient



#nom_bdd=input("taper le nom de la bdd : " )
#collection = input("taper le nom de la collection : ")
#zip_zip="/home/corot/Bureau/Projet 4/*.zip"
#fi_cnf="/home/corot/Bureau/Projet 4/datalab.cnf"
def all_zip(fi_cnf,zip_zip,nom_bdd,collection,auth_data):
    
    config = configparser.ConfigParser()
    config.read_file(open(os.path.expanduser(fi_cnf)))

    CNF = "mongo"
    BDD = auth_data
    
    # Ouverture connection -> mongo sur serveur
    client = MongoClient('mongodb://%s:%s@%s/?authSource=%s' % (config[CNF]['user'], config[CNF]['password'], config[CNF]['host'], BDD))
    print(client)
    
    bdd = client['Datalab'] # BDD "Datalab" de mongoDB sur serveur
    bdd
    #print("'Datalab' Collections:")    
    collec = client[nom_bdd][collection]
    
    
    
    
    fichier = glob.glob(zip_zip)
    #print(fichier)
    ############ON DEZIPE###################################
    for fil in fichier:
        #print("-"+fil)
        zf = zipfile.ZipFile(fil, 'r') # le ZIP
        #print(zipfile)
        for zipName in zf.namelist():
            try:
            #txt = zf.read(zipName).decode("utf-8")
            # https://stackoverflow.com/questions/4162642/single-vs-double-quotes-in-json
            ##############fonction qui permet de traduire du str en Json
                x = ast.literal_eval(zf.read(zipName).decode("utf-8"))
            #pprint.pprint(x)
            #flag = 'username' in x['content']
            #print(zipName+": "+x['content']['title']+", "+str(flag))
            #~ break
                collec.insert_one(x)
            except SyntaxError:
                print('bbb')
            except TypeError:
                print('bloub')
                
                
#nom_bdd=input("taper le nom de la bdd : " )
#collection = input("taper le nom de la collection : ")
#zip_zip="/home/corot/Bureau/Projet 4/*.zip"
#fi_cnf="/home/corot/Bureau/Projet 4/datalab.cnf"
#
#all_zip(fi_cnf,zip_zip,nom_bdd,collection)