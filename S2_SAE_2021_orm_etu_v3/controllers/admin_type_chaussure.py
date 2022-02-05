#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

admin_type_chaussure = Blueprint('admin_type_chaussure', __name__,
                        template_folder='templates')

@admin_type_chaussure.route('/admin/type-chaussure/show')
def show_type_chaussure():
    mycursor = get_db().cursor()
    types_chaussures = []
    return render_template('admin/type_chaussure/show_type_chaussure.html', types_chaussures=types_chaussures)

@admin_type_chaussure.route('/admin/type-chaussure/add', methods=['GET'])
def add_type_chaussure():
    return render_template('admin/type_chaussure/add_type_chaussure.html')

@admin_type_chaussure.route('/admin/type-chaussure/add', methods=['POST'])
def valid_add_type_chaussure():
    libelle = request.form.get('libelle', '')
    tuple_insert = (libelle,)
    message = u'type ajouté , libellé :'+libelle
    flash(message)
    return redirect('/admin/type-chaussure/show') #url_for('show_type_chaussure')

@admin_type_chaussure.route('/admin/type-chaussure/delete', methods=['GET'])
def delete_type_chaussure():
    id_type_chaussure = request.args.get('id', '')
    flash(u'suppression type chaussure , id : ' + id_type_chaussure)
    return redirect('/admin/type-chaussure/show') #url_for('show_type_chaussure')

@admin_type_chaussure.route('/admin/type-chaussure/edit/<int:id>', methods=['GET'])
def edit_type_chaussure(id):
    mycursor = get_db().cursor()
    type_chaussure = []
    return render_template('admin/type_chaussure/edit_type_chaussure.html', type_chaussure=type_chaussure)

@admin_type_chaussure.route('/admin/type-chaussure/edit', methods=['POST'])
def valid_edit_type_chaussure():
    libelle = request.form['libelle']
    id_type_chaussure = request.form.get('id', '')
    flash(u'type chaussure modifié, id: ' + id_type_chaussure + " libelle : " + libelle)
    return redirect('/admin/type-chaussure/show') #url_for('show_type_chaussure')
