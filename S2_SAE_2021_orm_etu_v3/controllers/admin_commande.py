#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template, redirect

from connexion_db import get_db

admin_commande = Blueprint('admin_commande', __name__,
                        template_folder='templates')

@admin_commande.route('/admin/commande/index')
def admin_index():
    return render_template('admin/layout_admin.html')

@admin_commande.route('/admin/commande/show', methods=['GET', 'POST'])
def admin_commande_show():
    mycursor = get_db().cursor()
    sql = "SELECT username, C.id_commande, SUM(CHAUSSURE.prix_chaussure*LC.quantite) AS prix_total, SUM(quantite) as nbr_chaussures, C.date_achat, libelle_etat " \
          "FROM CHAUSSURE " \
          "INNER JOIN LIGNE_COMMANDE LC on CHAUSSURE.id_chaussure = LC.id_chaussure" \
          "INNER JOIN COMMANDE C on LC.id_commande = C.id_commande" \
          "INNER JOIN UTILISATEUR U on C.id_utilisateur = U.id_utilisateur" \
          "INNER JOIN ETAT E on C.id_etat = E.id_etat" \
          "GROUP BY U.id_utilisateur, C.id_commande" \
          "ORDER BY prix_total DESC;"
    mycursor.execute(sql)
    commandes = mycursor.fetchall()
    return render_template('/admin/commande/show_commande.html', commandes=commandes)


@admin_commande.route('/admin/commande/valider/<int:id_commande>', methods=['get', 'post'])
def admin_commande_valider(id_commande):
    mycursor = get_db().cursor()
    sql = '''UPDATE COMMAND4E SET id_etat=2 WHERE COMMANDE.id_commande=%s'''
    mycursor.execute(sql, id_commande)
    mycursor.execute("SELECT * FROM COMMANDE WHERE id_commande = %s",(id_commande))
    commande = mycursor.fetchone()
    get_db().commit()
    return redirect('/admin/commande/show_commande')


@admin_commande.route('/admin/commande/<int:id_commande>', methods=['GET', 'POST'])
def admin_commande_details(id_commande):
    mycursor = get_db().cursor()
    sql = '''SELECT id_commande, prix_unit, quantite, prix_unit*quantite AS prix_tot FROM
     LIGNE_COMMANDE INNER JOIN CHAUSSURE on CHAUSSURE.id_chaussure = id_chaussure WHERE id_commande = %s'''
    mycursor.execute(sql, id_commande)
    chaussures = mycursor.fetchall()
    sql = '''SELECT libelle_etat FROM ETAT INNER JOIN COMMANDE on COMMANDE.id_etat=ETAT.id_etat WHERE COMMANDE.id_etat = %s '''
    mycursor.execute(sql, id_commande)
    etat = mycursor.fetchone()
    return render_template('admin/commande/detail/show.html', chaussures=chaussures, etat=etat)