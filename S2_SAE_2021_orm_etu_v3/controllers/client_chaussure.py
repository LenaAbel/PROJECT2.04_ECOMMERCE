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
    sql = "SELECT * FROM CHAUSSURE"
    mycursor.execute(sql)
    chaussures = mycursor.fetchall()
    sql = "SELECT * FROM TYPE_CHAUSSURE"
    mycursor.execute(sql)
    types_chaussures = mycursor.fetchall()
    sql = "SELECT * FROM CHAUSSURE"
    mycursor.execute(sql)
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
    userHasMadeAComment = mycursor.fetchall() != ()

    return render_template('client/boutique/article_details.html', article=article, commentaires=commentaires, commandes_articles=commandes_articles, userHasMadeAComment=userHasMadeAComment)
