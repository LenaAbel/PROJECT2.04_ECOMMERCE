#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

admin_chaussure = Blueprint('admin_chaussure', __name__,
                        template_folder='templates')

@admin_chaussure.route('/admin/chaussure/show')
def show_chaussure():
    mycursor = get_db().cursor()
    chaussures = None
    # print(chaussures)
    return render_template('admin/chaussure/show_chaussure.html', chaussures=chaussures)

@admin_chaussure.route('/admin/chaussure/add', methods=['GET'])
def add_chaussure():
    mycursor = get_db().cursor()
    types_chaussures = None
    return render_template('admin/chaussure/add_chaussure.html', types_chaussures=types_chaussures)

@admin_chaussure.route('/admin/chaussure/add', methods=['POST'])
def valid_add_chaussure():
    nom = request.form.get('nom', '')
    type_chaussure_id = request.form.get('type_chaussure_id', '')
   # type_chaussure_id = int(type_chaussure_id)
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')


    print(u'chaussure ajouté , nom: ', nom, ' - type_chaussure:', type_chaussure_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'chaussure ajouté , nom:'+nom + '- type_chaussure:' + type_chaussure_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message)
    return redirect(url_for('admin_chaussure.show_chaussure'))

@admin_chaussure.route('/admin/chaussure/delete', methods=['POST'])
def delete_chaussure():
    # id = request.args.get('id', '')
    id = request.form.get('id', '')

    print("un chaussure supprimé, id :", id)
    flash(u'un chaussure supprimé, id : ' + id)
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

    print(u'chaussure modifié , nom : ', nom, ' - type_chaussure:', type_chaussure_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'chaussure modifié , nom:'+nom + '- type_chaussure:' + type_chaussure_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message)
    return redirect(url_for('admin_chaussure.show_chaussure'))
