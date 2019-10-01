#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:02:33 2019

@author: axel
"""

from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import collections
import pprint
import pandas as np

##########importation ############


chemin = '/home/axel/Documents/Projet_4/course-v1_CNAM+01032+session01'
fichiers = [f for f in listdir(chemin)
            if isfile(join(chemin, f))]


#########pour lire les fichiers du document#####

surnom_l=[]
liste_id=[]
liste_thread_type=[]
liste_course=[]

for i in fichiers:
    #print(i)
    try:
        fichier = open("/home/axel/Documents/Projet_4/course-v1_CNAM+01032+session01/{}".format(i), "r")
        R = fichier.read().strip()
        l= eval(R)
        #pprint.pprint(l)
        ids=l["content"]["id"]
        s_n=l["content"]['username']
        thread=l["content"]["thread_type"]
        course=l["content"]["courseware_title"]
        
        surnom_l.append(s_n)
        liste_id.append(ids)
        liste_thread_type.append(thread)
        liste_course.append(course)
    except:
        s_n="none"
        ids="none"
        thread="none"
        course="none"
        surnom_l.append(s_n)
        
######pratique la collection pour compter######
        
intervention_nom = collections.Counter(surnom_l).most_common(20)# Compte les 20 premiers
#print(">>>>>>>",type(intervention_nom))
intervention_nom=intervention_nom[-19:]
#print(">>>>>>>>>",intervention_nom)

########et un graph en barre########

f, ax1 = plt.subplots(figsize =(10,10))
plt.bar(*zip(*intervention_nom), width = 0.6, color = 'orange',    edgecolor = 'blue', linewidth = 5)
plt.xticks(rotation = 90)    
plt.xlabel('pseudo', fontsize = 20,color='blue')
plt.ylabel("Intervention",fontsize = 20,color='blue')

plt.title('Nombre d\'interventions par personne',fontsize = 20,color='blue')