#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g
from flask import Blueprint

from controllers.auth_security import *

from controllers.client_chaussure import *
from controllers.client_panier import *
from controllers.client_commande import *
from controllers.client_commentaire import *

from controllers.admin_chaussure import *
from controllers.admin_commande import *
from controllers.admin_panier import *
from controllers.admin_type_chaussure import *
from controllers.admin_dataviz_chaussure import *

import pymysql.cursors

mydb = pymysql.connect(    #pymysql.connect remplace mysql.connector
  host="serveurmysql",   #serveurmysql
  user="label2",
  password="0310",
  database="BDD_label2",
  charset='utf8mb4',                      # 2 attributs à ajouter
  cursorclass=pymysql.cursors.DictCursor  # 2 attributs à ajouter
)
mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def show_accueil():
    return render_template('auth/layout.html')

###################ADMIN CHAUSSURE###########################

@app.route('/admin')
def show_accueil_admin():
    return render_template('admin/layout_admin.html')

@app.route('/admin/chaussure/add_chaussure', methods=['GET'])
def add_chaussure():
    k
@app.route('/admin/chaussure/add_chaussure', methods=['POST'])
def valid_add_chaussure():
    k
@app.route('/admin/chaussure/edit_chaussure', methods=['GET'])
def edit_chaussure():
    k

@app.route('/admin/chaussure/edit_chaussure', methods=['POST'])
def valid_edit_chaussure():
    k
    
@app.route('/admin/chaussure/show_chaussure')
def show_chaussure():
    k
    
########ADMIN DATA VIZ#######
    
@app.route('/dataviz/etat_chaussure_vente')
def etat_chaussure_vente():
    return render_template('/admin/dataviz/etat_chaussure_vente.html')
@app.route('/dataviz/etat_type_chaussure_stock')
def etat_type_chaussure_stock():
    k
    
#####ADMIN TYPE CHAUSSURE######    

@app.route('/type_chaussure/add_type_chaussure', methods=['GET'])
def add_type_chaussure():
    k
@app.route('/type_chaussure/add_type_chaussure', methods=['POST'])
def valid_add_type_chaussure():
    k
@app.route('/type_chaussure/delete_type_chaussure')
def delete_type_chaussure():
    k
@app.route('/type_chaussure/edit_type_chaussure', methods=['GET'])
def edit_type_chaussure():
    k
@app.route('/type_chaussure/edit_type_chaussure', methods=['POST'])
def valid_edit_type_chaussure():
    k
@app.route('/type_chaussure/show_type_chaussure')
def show_type_chaussure():
    k
#######ADMIN COMMANDES#######
@app.route('/commandes/show')
def show_commandes():    
    k
    
#############AUTH##############################

@app.route('/auth/layout')
def layout():
    k
@app.route('/auth/login')
def login():
    k
@app.route('/auth/signup')
def signup():
    k
    
##################CLIENT#########################
@app.route('/client')
def show_accueil():
    return render_template('auth/layout.html')

#########BOUTIQUE###########
@app.route('/client/boutique/_filtre')
def _filtre():
    k
@app.route('/client/boutique/chaussure_details')
def chaussure_details():
    k
@app.route('/client/boutique/panier_chaussure')
def panier_chaussure():
    k
    
#########COMMANDES###########
@app.route('/client/commandes/show')
def show_commandes_client():
    k
    
if __name__ == '__main__':
    app.run()
