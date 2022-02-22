#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request, redirect, session

from connexion_db import get_db

client_panier = Blueprint('client_panier', __name__,
                        template_folder='templates')


@client_panier.route('/client/panier/add', methods=['POST'])
def client_panier_add():
    mycursor = get_db().cursor()
    id_utilisateur = session['user_id']
    id_chaussure = request.form.get('id_chaussure')
    quantite = request.form.get('quantite')
    mycursor.execute("SELECT quantite FROM PANIER WHERE id_chaussure=%s AND id_utilisateur=%s",(id_chaussure, id_utilisateur))
    quantitePanier = mycursor.fetchone()
    mycursor.execute("SELECT stock_chaussure FROM CHAUSSURE WHERE id_chaussure=%s", (id_chaussure))
    stockChaussure = mycursor.fetchone()

    sql = "SELECT * FROM PANIER WHERE id_chaussure=%s AND id_utilisateur=%s"
    mycursor.execute(sql, (id_chaussure, id_utilisateur))
    res = mycursor.fetchall()

    if len(res) == 0:
        mycursor.execute("SELECT prix_chaussure FROM CHAUSSURE WHERE id_chaussure=%s", (id_chaussure))
        prixChaussure = mycursor.fetchone()
        sql = "INSERT INTO PANIER VALUE (NULL,CURDATE(),%s,%s,%s,%s)"
        tuple = (prixChaussure["prix_chaussure"],quantite, id_chaussure, id_utilisateur)
        mycursor.execute(sql, tuple)
        get_db().commit()
    else :
        if quantitePanier["quantite"] >= int( stockChaussure["stock_chaussure"]) :
            return redirect('/client/chaussure/show')
        else :
            mycursor.execute("UPDATE PANIER SET quantite = quantite+%s WHERE id_chaussure=%s AND id_utilisateur=%s", (quantite, id_chaussure, id_utilisateur))
            get_db().commit()
    return redirect('/client/chaussure/show')

@client_panier.route('/client/panier/delete', methods=['POST'])
def client_panier_delete():
    mycursor = get_db().cursor()
    client_id = session['user_id']
    id_chaussure = request.form.get('id_chaussure')
    mycursor.execute("SELECT quantite FROM PANIER WHERE id_chaussure=%s AND id_utilisateur=%s",(id_chaussure, client_id))
    quantitePanier = mycursor.fetchone()
    if quantitePanier["quantite"]<=1:
        return redirect('/client/panier/delete/line')
    else :
        mycursor.execute("UPDATE PANIER SET quantite = quantite-1 WHERE id_chaussure=%s AND id_utilisateur=%s",(id_chaussure, client_id))
        get_db().commit()
    return redirect('/client/chaussure/show')


@client_panier.route('/client/panier/vider', methods=['POST'])
def client_panier_vider():
    mycursor = get_db().cursor()
    id_utilisateur = session['user_id']
    mycursor.execute("DELETE FROM PANIER WHERE id_utilisateur=%s", id_utilisateur)
    get_db().commit()

    return redirect('/client/chaussure/show')
    #return redirect(url_for('client_index'))


@client_panier.route('/client/panier/delete/line', methods=['POST'])
def client_panier_delete_line():
    mycursor = get_db().cursor()
    id_chaussure = request.form.get('id_chaussure')
    id_utilisateur = session['user_id']
    mycursor.execute("DELETE FROM PANIER WHERE id_utilisateur=%s and id_chaussure=%s", (id_utilisateur, id_chaussure))
    get_db().commit()
    return redirect('/client/chaussure/show')
    #return redirect(url_for('client_index'))


@client_panier.route('/client/panier/filtre', methods=['POST'])
def client_panier_filtre():
    # SQL
    filter_word = request.form.get('filter_word', None)
    filter_prix_min = request.form.get('filter_prix_min', None)
    filter_prix_max = request.form.get('filter_prix_max', None)
    filter_types = request.form.getlist('filter_types', None)
    if type(filter_word) == str:
        session['filter_word'] = filter_word
    session['filter_prix_min'] = filter_prix_min
    session['filter_prix_max'] = filter_prix_max
    session['filter_types'] = filter_types
    return redirect('/client/chaussure/show')
    #return redirect(url_for('client_index'))


@client_panier.route('/client/panier/filtre/suppr', methods=['POST'])
def client_panier_filtre_suppr():
    session.pop('filter_word', None)
    session.pop('filter_prix_min', None)
    session.pop('filter_prix_max', None)
    session.pop('filter_types', None)
    print("suppr filtre")
    return redirect('/client/chaussure/show')
    #return redirect(url_for('client_index'))