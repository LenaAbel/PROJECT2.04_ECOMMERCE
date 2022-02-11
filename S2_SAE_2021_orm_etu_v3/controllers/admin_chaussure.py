#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash

from connexion_db import get_db


admin_chaussure = Blueprint('admin_chaussure', __name__,
                        template_folder='templates')

@admin_chaussure.route('/admin/chaussure/show')
def show_chaussure():
    mycursor = get_db().cursor()
    sql = "SELECT * FROM CHAUSSURE"
    mycursor.execute(sql)
    chaussures = mycursor.fetchall()
    sql = "SELECT * FROM TYPE_CHAUSSURE"
    mycursor.execute(sql)
    types_chaussures = mycursor.fetchall()
    sql = "SELECT * FROM FOURNISSEUR"
    mycursor.execute(sql)
    fournisseurs = mycursor.fetchall()
    sql = "SELECT * FROM MARQUE"
    mycursor.execute(sql)
    marques = mycursor.fetchall()
    sql = "SELECT * FROM MATIERE"
    mycursor.execute(sql)
    matieres = mycursor.fetchall()
    print("In show_chaussure(): ")
    print(chaussures)
    return render_template('admin/chaussure/show_chaussure.html', chaussures=chaussures, types_chaussures=types_chaussures, fournisseurs=fournisseurs, marques=marques, matieres=matieres)

@admin_chaussure.route('/admin/chaussure/add', methods=['GET'])
def add_chaussure():
    mycursor = get_db().cursor()
    sql = "SELECT * FROM TYPE_CHAUSSURE"
    mycursor.execute(sql)
    types_chaussures = mycursor.fetchall()
    sql = "SELECT * FROM FOURNISSEUR"
    mycursor.execute(sql)
    fournisseurs = mycursor.fetchall()
    sql = "SELECT * FROM MARQUE"
    mycursor.execute(sql)
    marques = mycursor.fetchall()
    sql = "SELECT * FROM MATIERE"
    mycursor.execute(sql)
    matieres = mycursor.fetchall()

    print("In add_chaussure(): ")
    print(types_chaussures)
    print(fournisseurs)
    print(marques)
    return render_template('admin/chaussure/add_chaussure.html', types_chaussures=types_chaussures, fournisseurs=fournisseurs, marques=marques, matieres=matieres)

@admin_chaussure.route('/admin/chaussure/add', methods=['POST'])
def valid_add_chaussure():
    nom         = request.form.get('nom_chaussure', '')
    id_type     = request.form.get('id_type_chaussure', '')
    prix        = request.form.get('prix_chaussure', '')
    stock       = request.form.get('stock_chaussure', '')
    marque      = request.form.get('marque_chaussure', '')
    fournisseur = request.form.get('fournisseur_chaussure', '')
    matiere = request.form.get('matiere_chaussure', '')
    #description= request.form.get('description', '')
    image       = request.form.get('image_chaussure', '')
    tuple_insert= (nom,id_type,prix,stock,marque,fournisseur,matiere,image)
    sql = "INSERT INTO CHAUSSURE(nom_chaussure, id_type_chaussure, prix_chaussure,stock_chaussure,id_marque,id_fournisseur, id_matiere , image_chaussure) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    mycursor = get_db().cursor()
    res = mycursor.execute(sql, tuple_insert)
    res = get_db().commit()
    #print(u'Chaussure ajoutée, Nom: ', nom, ' - Type chaussure:', id_type, ' - Prix:', prix, ' - Stock:', stock,' - Marque:', marque, ' - Fournisseur:', fournisseur, ' - Image:', image)
    message = u'Chaussure ajoutée, Nom:'+nom + '- Type chaussure:' + id_type + ' - Prix:' + prix + ' - Stock:'+  stock + ' - Marque:'+ marque+' - Fournisseur:'+fournisseur+ ' - Image:' + image
    flash(message)
    return redirect(url_for('admin_chaussure.show_chaussure'))

@admin_chaussure.route('/admin/chaussure/delete', methods=['GET'])
def delete_chaussure():
    id = request.args.get('id', '')
    #id = request.form.get('id', '')
    tuple_delete = (id)
    sql = "DELETE FROM LIGNE_COMMANDE WHERE id_chaussure = %s;"
    mycursor = get_db().cursor()
    # mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, tuple_delete)
    get_db().commit()

    sql = "DELETE FROM NOTE WHERE id_chaussure = %s;"
    mycursor = get_db().cursor()
    # mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, tuple_delete)
    get_db().commit()

    sql = "DELETE FROM COMMENTAIRE WHERE id_chaussure = %s;"
    mycursor = get_db().cursor()
    # mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, tuple_delete)
    get_db().commit()

    sql = "DELETE FROM EST_DE_COULEUR WHERE id_chaussure = %s;"
    mycursor = get_db().cursor()
    # mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, tuple_delete)
    get_db().commit()

    sql = "DELETE FROM PANIER WHERE id_chaussure = %s;"
    mycursor = get_db().cursor()
    # mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, tuple_delete)
    get_db().commit()

    sql = "DELETE FROM MESURE WHERE id_chaussure = %s;"
    mycursor = get_db().cursor()
    # mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, tuple_delete)
    get_db().commit()

    sql = "DELETE FROM CHAUSSURE WHERE id_chaussure = %s;"
    mycursor = get_db().cursor()
    #mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, tuple_delete)
    res = get_db().commit()
    print("Supression de la chaussure #", id)
    flash(u'Supression de la chaussure #' + id)
    return redirect(url_for('admin_chaussure.show_chaussure'))

@admin_chaussure.route('/admin/chaussure/edit/<int:id>', methods=['GET'])
def edit_chaussure(id):
    sql="SELECT * FROM CHAUSSURE WHERE id_chaussure=%s"
    mycursor = get_db().cursor()
    mycursor.execute(sql, id)
    chaussure = mycursor.fetchone()
    sql="SELECT * FROM TYPE_CHAUSSURE"
    mycursor.execute(sql)
    types_chaussures = mycursor.fetchall()
    sql = "SELECT * FROM FOURNISSEUR"
    mycursor.execute(sql)
    fournisseurs = mycursor.fetchall()
    sql = "SELECT * FROM MARQUE"
    mycursor.execute(sql)
    marques = mycursor.fetchall()
    sql = "SELECT * FROM MATIERE"
    mycursor.execute(sql)
    matieres = mycursor.fetchall()
    return render_template('admin/chaussure/edit_chaussure.html', chaussure=chaussure, types_chaussures=types_chaussures, fournisseurs=fournisseurs, marques=marques, matieres=matieres)

@admin_chaussure.route('/admin/chaussure/edit', methods=['POST'])
def valid_edit_chaussure():
    id = request.form.get('id_chaussure', '')
    nom = request.form['nom_chaussure']
    id_type = request.form.get('id_type_chaussure', '')
    #type_chaussure_id = int(type_chaussure_id)
    prix = request.form.get('prix_chaussure', '')
    stock = request.form.get('stock_chaussure', '')
    marque = request.form.get('marque_chaussure', '')
    fournisseur = request.form.get('fournisseur_chaussure', '')
    matiere = request.form.get('fournisseur_chaussure', '')
    # description= request.form.get('description', '')
    image = request.form.get('image_chaussure', '')
    tuple_update = (nom, id_type, prix, stock, marque, fournisseur, matiere, image, id)
    sql = "UPDATE CHAUSSURE SET nom_chaussure=%s, id_type_chaussure=%s, prix_chaussure=%s, stock_chaussure=%s, id_marque=%s, id_fournisseur=%s, id_matiere=%s, image_chaussure=%s  WHERE id_chaussure=%s; "
    mycursor = get_db().cursor()
    res = mycursor.execute(sql, tuple_update)
    res = get_db().commit()
    print(u'Chaussure modifiée, Nom: ', nom, ' -ID: ', id,' - Type chaussure:', id_type, ' - Prix:', prix, ' - Stock:', stock,' - Marque:', marque, ' - Fournisseur:', fournisseur, ' - Image:', image)
    message = u'Chaussure modifiée, Nom:' + nom + '- Type chaussure:' + id_type + ' - Prix:' + prix + ' - Stock:' + stock + ' - Marque:' + marque + ' - Fournisseur:' + fournisseur + ' - Image:' + image
    flash(message)
    return redirect(url_for('admin_chaussure.show_chaussure'))
