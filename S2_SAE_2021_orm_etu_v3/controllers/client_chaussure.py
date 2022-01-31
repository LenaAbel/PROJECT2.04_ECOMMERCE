#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

client_chaussure = Blueprint('client_chaussure', __name__,
                        template_folder='templates')

@client_chaussure.route('/client/index')
@client_chaussure.route('/client/chaussure/show')      # remplace /client
def client_chaussure_show():                                 # remplace client_index
    mycursor = get_db().cursor()
    chaussures = []
    types_chaussures = []
    chaussures_panier = []
    prix_total = None
    return render_template('client/boutique/panier_chaussure.html', chaussures=chaussures, chaussuresPanier=chaussures_panier, prix_total=prix_total, itemsFiltre=types_chaussures)

@client_chaussure.route('/client/chaussure/details/<int:id>', methods=['GET'])
def client_chaussure_details(id):
    mycursor = get_db().cursor()
    chaussure=None
    commentaires=None
    commandes_chaussures=None
    return render_template('client/boutique/chaussure_details.html', chaussure=chaussure, commentaires=commentaires, commandes_chaussures=commandes_chaussures)
