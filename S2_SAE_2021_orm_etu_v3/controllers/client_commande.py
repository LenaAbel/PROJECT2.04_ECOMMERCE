#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template, redirect, flash
from connexion_db import get_db

client_commande = Blueprint('client_commande', __name__,
                        template_folder='templates')


@client_commande.route('/client/commande/add', methods=['POST'])
def client_commande_add():
    mycursor = get_db().cursor()
    flash(u'Commande ajoutée')
    return redirect('/client/chaussure/show')
    #return redirect(url_for('client_index'))



@client_commande.route('/client/commande/show', methods=['get','post'])
def client_commande_show():
    mycursor = get_db().cursor()
    commandes = None
    chaussures_commande = None
    return render_template('client/commandes/show.html', commandes=commandes, chaussures_commande=chaussures_commande)

