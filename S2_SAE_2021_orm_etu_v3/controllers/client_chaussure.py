#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint, session
from flask import render_template

from connexion_db import get_db

client_chaussure = Blueprint('client_chaussure', __name__,
                        template_folder='templates')

@client_chaussure.route('/client/index')
@client_chaussure.route('/client/chaussure/show')      # remplace /client
def client_chaussure_show():                                 # remplace client_index
    mycursor = get_db().cursor()
    debut = True
    params = []
    sql = "SELECT * FROM CHAUSSURE"
    if "filter_word" in session.keys():
        sql += " WHERE nom_chaussure LIKE %s"
        params.append("%" + session['filter_word'] + "%")
        debut = False
    if "filter_types" in session.keys() and len(session['filter_types']) > 0:
        if len(session['filter_types']) == 1:
            tpl = "('" + str(session['filter_types'][0]) + "')"
        else:
            tpl = str(tuple(session['filter_types']))
        if debut:
            sql += " WHERE id_type_chaussure in " + tpl
        else:
            sql += " AND id_type_chaussure in " + tpl
        debut = False
    if "filter_prix_min" in session.keys() and session["filter_prix_min"] != "":
        if debut:
            sql += " WHERE prix_chaussure > %s"
        else:
            sql += " AND prix_chaussure > %s"
        debut = False
        params.append(session['filter_prix_min'])
    if "filter_prix_max" in session.keys() and session["filter_prix_max"] != "":
        if debut:
            sql += " WHERE prix_chaussure < %s"
        else:
            sql += " AND prix_chaussure < %s"
        params.append(session['filter_prix_max'])

    sql += " GROUP BY id_chaussure"
    mycursor.execute(sql, params)
    chaussures = mycursor.fetchall()
    sql = "SELECT * FROM TYPE_CHAUSSURE"
    mycursor.execute(sql)
    types_chaussures = mycursor.fetchall()
    mycursor.execute("SELECT *, CHAUSSURE.nom_chaussure, CHAUSSURE.stock_chaussure FROM PANIER INNER JOIN CHAUSSURE ON PANIER.id_chaussure=CHAUSSURE.id_chaussure WHERE PANIER.id_utilisateur=%s", session['user_id'])
    chaussures_panier = mycursor.fetchall()
    prix_total = None
    return render_template('client/boutique/panier_chaussure.html', chaussures=chaussures, chaussuresPanier=chaussures_panier, prix_total=prix_total, itemsFiltre=types_chaussures)

@client_chaussure.route('/client/chaussure/details/<int:id>', methods=['GET'])
def client_chaussure_details(id):
    mycursor = get_db().cursor()

    mycursor.execute("SELECT * FROM CHAUSSURE where id_chaussure = %s", (id))
    article = mycursor.fetchone()

    mycursor.execute("SELECT * FROM NOTE where id_chaussure = %s", (id))
    commentaires = mycursor.fetchall()

    mycursor.execute(
        "SELECT * FROM LIGNE_COMMANDE INNER JOIN COMMANDE ON LIGNE_COMMANDE.id_commande = COMMANDE.id_commande WHERE id_chaussure = %s AND id_utilisateur = %s", (id, session["user_id"]))
    commandes_articles = mycursor.fetchall()

    mycursor.execute("SELECT * FROM NOTE WHERE id_chaussure = %s AND id_utilisateur = %s", (id, session["user_id"]))
    userComment = mycursor.fetchall() != ()

    return render_template('client/boutique/article_details.html', article=article, commentaires=commentaires, commandes_articles=commandes_articles, userComment=userComment)
