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
    print("In show_chaussure(): ")
    print(chaussures)
    return render_template('admin/chaussure/show_chaussure.html', chaussures=chaussures)

@admin_chaussure.route('/admin/chaussure/add', methods=['GET'])
def add_chaussure():
    mycursor = get_db().cursor()
    sql = "SELECT * FROM TYPE_CHAUSSURE"
    mycursor.execute(sql)
    types_chaussures = mycursor.fetchall()
    print("In add_chaussure(): ")
    print(types_chaussures)
    return render_template('admin/chaussure/add_chaussure.html', types_chaussures=types_chaussures)

@admin_chaussure.route('/admin/chaussure/add', methods=['POST'])
def valid_add_chaussure():
    nom         = request.form.get('nom_chaussure', '')
    id_type     = request.form.get('id_type_chaussure', '')
    prix        = request.form.get('prix_chaussure', '')
    stock       = request.form.get('stock_chaussure', '')
    marque      = request.form.get('marque_chaussure', '')
    fournisseur = request.form.get('fournisseur_chaussure', '')
    #description= request.form.get('description', '')
    image       = request.form.get('image_chaussure', '')
    tuple_insert= (nom,id_type,prix,stock,marque,fournisseur,image)
    sql = "INSERT INTO CHAUSSURE(nom_chaussure, id_type_chaussure, prix_chaussure,stock_chaussure,marque_chaussure, fournisseur_chaussure, image_chaussure) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    mycursor = get_db().cursor()
    res = mycursor.execute(sql, tuple_insert)
    res = get_db().commit()
    #print(u'Chaussure ajoutée, Nom: ', nom, ' - Type chaussure:', id_type, ' - Prix:', prix, ' - Stock:', stock,' - Marque:', marque, ' - Fournisseur:', fournisseur, ' - Image:', image)
    message = u'Chaussure ajoutée, Nom:'+nom + '- Type chaussure:' + id_type + ' - Prix:' + prix + ' - Stock:'+  stock + ' - Marque:'+ marque+' - Fournisseur:'+fournisseur+ ' - Image:' + image
    flash(message)
    return redirect(url_for('admin_chaussure.show_chaussure'))

@admin_chaussure.route('/admin/chaussure/delete', methods=['POST'])
def delete_chaussure():
    # id = request.args.get('id', '')
    id = request.form.get('id', '')

    print("Une chaussure supprimée, id :", id)
    flash(u'Une chaussure supprimée, id : ' + id)
    return redirect(url_for('admin_chaussure.show_chaussure'))

@admin_chaussure.route('/admin/chaussure/edit/<int:id>', methods=['GET'])
def edit_chaussure(id):
    mycursor = get_db().cursor()
    chaussure = None
    types_chaussures = None
    return render_template('admin/chaussure/edit_chaussure.html', chaussure=chaussure, types_chaussures=types_chaussures)

@admin_chaussure.route('/admin/chaussure/edit', methods=['POST'])
def valid_edit_chaussure():
    nom = request.form['nom']
    id = request.form.get('id', '')
    type_chaussure_id = request.form.get('type_chaussure_id', '')
    #type_chaussure_id = int(type_chaussure_id)
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')

    print(u'Chaussure modifiée , nom : ', nom, ' - type_chaussure:', type_chaussure_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'Chaussure modifiée , nom:'+nom + '- type_chaussure:' + type_chaussure_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message)
    return redirect(url_for('admin_chaussure.show_chaussure'))
