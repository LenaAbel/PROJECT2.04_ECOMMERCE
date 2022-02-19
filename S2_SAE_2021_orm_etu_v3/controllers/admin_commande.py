#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint, flash, url_for
from flask import render_template, redirect

from connexion_db import get_db

admin_commande = Blueprint('admin_commande', __name__,
                           template_folder='templates')


@admin_commande.route('/admin/commandes/index')
def admin_index():
    return render_template('/admin/layout_admin.html')


@admin_commande.route('/admin/commandes/show', methods=['GET', 'POST'])
def admin_commande_show():
    mycursor = get_db().cursor()
    sql = "SELECT username, C.id_commande, SUM(CHAUSSURE.prix_chaussure*LC.quantite) AS prix_total,  SUM(quantite) as nbr_chaussures, C.date_achat, libelle_etat " \
          "FROM CHAUSSURE " \
          "INNER JOIN LIGNE_COMMANDE LC on CHAUSSURE.id_chaussure = LC.id_chaussure " \
          "INNER JOIN COMMANDE C on LC.id_commande = C.id_commande " \
          "INNER JOIN UTILISATEUR U on C.id_utilisateur = U.id_utilisateur " \
          "INNER JOIN ETAT E on C.id_etat = E.id_etat " \
          "GROUP BY U.id_utilisateur, C.id_commande " \
          "ORDER BY id_commande ASC;"
    mycursor.execute(sql)
    commandes = mycursor.fetchall()
    return render_template('/admin/commandes/show_commandes.html', commandes=commandes)


@admin_commande.route('/admin/commandes/valider/<int:id_commande>', methods=['GET', 'POST'])
def admin_commande_valider(id_commande):
    mycursor = get_db().cursor()
    sql = "UPDATE COMMANDE SET id_etat=1 WHERE id_commande=%s"
    mycursor.execute(sql, id_commande)

    mycursor.execute("SELECT * FROM COMMANDE WHERE id_commande = %s", (id_commande))
    commande = mycursor.fetchone()
    get_db().commit()
    print("Validation de la commande n°", id_commande)
    flash(u'Validation de la commande n°' + str(id_commande))
    return redirect(url_for('admin_commande.admin_commande_show'))


@admin_commande.route('/admin/commandes/<int:id_commande>', methods=['GET', 'POST'])
def admin_commande_details(id_commande):
    mycursor = get_db().cursor()
    sql = "SELECT LIGNE_COMMANDE.id_commande, LIGNE_COMMANDE.prix_unit, quantite, prix_unit*quantite AS prix_total " \
          "FROM LIGNE_COMMANDE " \
          "INNER JOIN CHAUSSURE C on LIGNE_COMMANDE.id_chaussure = C.id_chaussure WHERE id_commande=%s;"
    mycursor.execute(sql, id_commande)
    chaussures = mycursor.fetchall()
    sql = "SELECT libelle_etat FROM ETAT INNER JOIN COMMANDE on COMMANDE.id_etat=ETAT.id_etat WHERE COMMANDE.id_etat = %s"
    mycursor.execute(sql, id_commande)
    etat = mycursor.fetchone()
    return render_template('admin/commandes/details/show.html', chaussures=chaussures, etat=etat)
