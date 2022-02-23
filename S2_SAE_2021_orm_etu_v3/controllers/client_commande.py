#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint, session, request
from flask import render_template, redirect, flash
from connexion_db import get_db

client_commande = Blueprint('client_commande', __name__,
                        template_folder='templates')


@client_commande.route('/client/commande/add', methods=['POST'])
def client_commande_add():
    mycursor = get_db().cursor()
    id_utilisateur = session['user_id']
    sql = "SELECT * FROM PANIER INNER JOIN CHAUSSURE ON CHAUSSURE.id_chaussure=PANIER.id_chaussure where id_utilisateur=%s"
    mycursor.execute(sql, id_utilisateur)
    panierUser = mycursor.fetchall()

    sql = "INSERT INTO COMMANDE VALUE (NULL,CURDATE(),%s,2)"
    mycursor.execute(sql, (id_utilisateur))
    get_db().commit()

    id_commande = mycursor.lastrowid

    sql = "INSERT INTO LIGNE_COMMANDE VALUE (%s,%s,%s,%s)"
    sql2 = "SELECT * FROM CHAUSSURE WHERE id_chaussure=%s"
    sql3 = "UPDATE CHAUSSURE SET stock_chaussure=%s WHERE id_chaussure=%s"
    cout_tot = 0
    for ligne in panierUser:
        tuple = ( ligne['id_chaussure'],id_commande, ligne['prix_unit'], ligne['quantite'])
        mycursor.execute(sql, tuple)

        mycursor.execute(sql2, (ligne['id_chaussure']))
        quantite = int(mycursor.fetchone()['stock_chaussure']) - int(ligne['quantite'])
        cout_tot += float(ligne['quantite']) * float(ligne['prix_unit'])
        mycursor.execute(sql3, (quantite, ligne['id_chaussure']))

    sql = "DELETE FROM PANIER WHERE id_utilisateur=%s"
    mycursor.execute(sql, id_utilisateur)
    get_db().commit()
    return redirect('/client/chaussure/show')
    #return redirect(url_for('client_index'))



@client_commande.route('/client/commande/show', methods=['get','post'])
def client_commande_show():
    mycursor = get_db().cursor()
    current_commande = request.form.get("id_commande", '')
    id_utilisateur = session['user_id']

    sql = "SELECT COMMANDE.id_commande,ETAT.libelle_etat,date_achat,ETAT.id_etat," \
          "COUNT(*) AS nbr_chaussures," \
          "SUM(quantite) AS nb_total," \
          "SUM(prix_unit*quantite) AS prix_total " \
          "FROM COMMANDE " \
          "INNER JOIN LIGNE_COMMANDE ON COMMANDE.id_commande=LIGNE_COMMANDE.id_commande " \
          "INNER JOIN ETAT ON COMMANDE.id_etat=ETAT.id_etat " \
          "WHERE COMMANDE.id_utilisateur=%s " \
          "GROUP BY COMMANDE.id_commande"
    mycursor.execute(sql, id_utilisateur)
    commandes = mycursor.fetchall()

    if current_commande is not None:
        sql = "SELECT quantite,prix_unit as prix,CHAUSSURE.nom_chaussure as nom,sum(prix_unit*quantite) as prix_ligne " \
              "FROM LIGNE_COMMANDE " \
              "INNER JOIN CHAUSSURE ON LIGNE_COMMANDE.id_chaussure = CHAUSSURE.id_chaussure " \
              "WHERE id_commande = %s " \
              "GROUP BY CHAUSSURE.id_chaussure"
        mycursor.execute(sql, current_commande)
        chaussures_commande = mycursor.fetchall()
    else:
        chaussures_commande = None
    return render_template('client/commandes/show_commandes.html', commandes=commandes, chaussures_commande=chaussures_commande)

