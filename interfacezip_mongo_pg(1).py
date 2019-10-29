#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:26:45 2019

@author: alflo
"""
from zip_mongo import all_zip
from mongo_pg import mongo_php
import tkinter as tk




#######fonction permettant extraction des saisies et appel des fonction de transfert zip vers mongo et pg######"

def show_entry_fields():
    print("auth_data: %s\ncollection: %s\nzip_zip: %s\nfi_cnf: %s\ntable_pg: %s" % (auth_data_entry.get(),
                                                                                    collection_entry.get(),
                                                                                    zip_zip_entry.get(),
                                                                                    fi_cnf_entry.get(),
                                                                                    table_pg_entry.get()))
        
    auth_data=auth_data_entry.get()
    print(auth_data)
    collection=collection_entry.get()
    print(collection)
    zip_zip=zip_zip_entry.get()
    print(zip_zip)
    fi_cnf=fi_cnf_entry.get()
    print(fi_cnf)
    table_pg=table_pg_entry.get()
    print(table_pg)
    nom_bdd=nom_bdd_entry.get()
    print(nom_bdd)
    
    all_zip(fi_cnf,zip_zip,nom_bdd,collection,auth_data)
    
    mongo_php(fi_cnf,nom_bdd,collection,auth_data,table_pg)
    
    
#######creation d'une fenetre les labels######    
    
master = tk.Tk()
master.title("Fenetre de transfert" )
#master['bg']='bisque'

#Label1 = Label(master, text = "taper authentification database (ex:Database)")
#Label1.pack(side = LEFT, padx = 5, pady = 5)


tk.Label(master, text="taper authentification database (ex:Database)").grid(row=0)
tk.Label(master, text="taper le nom de la bdd mongo à créer : " ).grid(row=1)
tk.Label(master, text="taper le nom de la collection mongo à créer : ").grid(row=2)
tk.Label(master, text="copie colle le chemin de tes zip, (ps ne met pas les guillemets) : ").grid(row=3)
tk.Label(master, text="copie colle le chemin de ton cnf : ").grid(row=4)
tk.Label(master, text="quel est le nom de votre table phpgadmin (ex forum2 : ").grid(row=5)

##########creation des saisies########

auth_data_entry = tk.Entry(master,textvariable="Motdepasse",width=50,bg='bisque')
nom_bdd_entry=tk.Entry(master,width=50,bg='bisque')
collection_entry = tk.Entry(master,width=50,bg='bisque')
zip_zip_entry = tk.Entry(master,width=50,bg='bisque')
fi_cnf_entry = tk.Entry(master,width=50,bg='bisque')
table_pg_entry = tk.Entry(master,width=50,bg='bisque')

##########creation de la gille#######

pos=auth_data_entry.grid(row=0, column=1)
nom_bdd_entry.grid(row=1, column=1)
collection_entry.grid(row=2, column=1)
zip_zip_entry.grid(row=3, column=1)
fi_cnf_entry.grid(row=4, column=1)
table_pg_entry.grid(row=5, column=1)

#######creation des boutons######

tk.Button(master, 
          text='Quitter', 
          command=master.destroy).grid(row=7, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='executer', command=show_entry_fields).grid(row=7, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)


master.mainloop()





