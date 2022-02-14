#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import request, render_template, redirect, flash

from connexion_db import get_db

admin_type_chaussure = Blueprint('admin_type_chaussure', __name__,
                                 template_folder='templates')


# Merge two lists of dictionaries
def update_dic_lists(dicList1, dicList2, element):
    for dic1 in dicList1:
        for dic2 in dicList2:
            if dic1['id_type_chaussure'] == dic2['id_type_chaussure']:
                dic1[element] = dic2[element]
    return dicList1


@admin_type_chaussure.route('/admin/type-chaussure/show')
def show_type_chaussure():
    mycursor = get_db().cursor()
    sql = "SELECT * FROM TYPE_CHAUSSURE"
    mycursor.execute(sql)
    typesChaussuresList = mycursor.fetchall()
    print("In show_type_chaussure(): ")
    print(typesChaussuresList)
    # Build a command to retrieve the number of chaussure per type_chaussure
    sql = "SELECT id_type_chaussure, COUNT(id_type_chaussure) AS nmbChaussures FROM CHAUSSURE GROUP BY id_type_chaussure ORDER BY id_type_chaussure ASC"
    mycursor.execute(sql)
    nmbChaussuresList = mycursor.fetchall()
    # print("nmbChaussuresList: ")
    # print(nmbChaussuresList)
    updtatedTypeList = update_dic_lists(typesChaussuresList, nmbChaussuresList, 'nmbChaussures')
    # print("updtatedTypeList: ")
    # print(updtatedTypeList)
    return render_template('admin/type_chaussure/show_type_chaussure.html', types_chaussures=updtatedTypeList)


@admin_type_chaussure.route('/admin/type-chaussure/add', methods=['GET'])
def add_type_chaussure():
    return render_template('admin/type_chaussure/add_type_chaussure.html')


@admin_type_chaussure.route('/admin/type-chaussure/add', methods=['POST'])
def valid_add_type_chaussure():
    mycursor = get_db().cursor()
    nom = request.form.get('nom_type_chaussure', '')
    tuple_insert = (nom)
    sql = "INSERT INTO TYPE_CHAUSSURE(nom_type_chaussure) VALUES (%s);"
    mycursor.execute(sql, tuple_insert)
    res = get_db().commit()
    print(u'Ajout du type, Nom: ', nom)
    message = u'Ajout du type , Nom:' + nom
    flash(message)
    return redirect('/admin/type-chaussure/show')  # url_for('show_type_chaussure')


@admin_type_chaussure.route('/admin/type-chaussure/delete/<int:id_type_chaussure>', methods=['GET'])
def delete_type_chaussure(id_type_chaussure):
    mycursor = get_db().cursor()
    id_type_chaussure = request.args.get('id', '')
    # flash(u'suppression type chaussure , id : ' + id_type_chaussure)

    tuple_delete = (id_type_chaussure)
    sql = "DELETE FROM CHAUSSURE WHERE id_type_chaussure=%s;"
    mycursor.execute(sql, tuple_delete)
    if mycursor.rowcount != 0:
        print(u'Warning: ' + str(mycursor.rowcount) + " shoes might be deleted.")
        mycursor.rollback()
        res = get_db().commit()
        sql = "SELECT * FROM CHAUSSURE WHERE id_type_chaussure=%s;"
        mycursor.execute(sql, tuple_delete)
        chaussureToDelete = mycursor.fetchall()
        print('chaussureToDelete:')
        print(chaussureToDelete)
        return render_template('/admin/type_chaussure/delete_type_chaussure.html', chaussureToDelete=chaussureToDelete)
    else:
        sql = "DELETE FROM TYPE_CHAUSSURE WHERE id_type_chaussure=%s;"
        mycursor.execute(sql, tuple_delete)
        res = get_db().commit()
        print("Suppression de la chaussure de type: ", id_type_chaussure)
        flash(u'Suppression de la chaussure de type: ' + str(id_type_chaussure))
        return redirect('/admin/type-chaussure/show')  # url_for('show_type_chaussure')


@admin_type_chaussure.route('/admin/type-chaussure/edit/<int:id_type_chaussure>', methods=['GET'])
def edit_type_chaussure(id_type_chaussure):
    mycursor = get_db().cursor()
    sql = "SELECT * FROM TYPE_CHAUSSURE WHERE id_type_chaussure=%s;"
    mycursor.execute(sql, id_type_chaussure)
    type_chaussure = mycursor.fetchone()
    res = get_db().commit()
    return render_template('admin/type_chaussure/edit_type_chaussure.html', type_chaussure=type_chaussure)


@admin_type_chaussure.route('/admin/type-chaussure/edit', methods=['POST'])
def valid_edit_type_chaussure():
    mycursor = get_db().cursor()
    id_type_chaussure = request.form.get('id_type_chaussure', '')
    nom = request.form.get('nom_type_chaussure', '')
    tuple_update = (nom, id_type_chaussure)
    sql = "UPDATE TYPE_CHAUSSURE SET nom_type_chaussure=%s WHERE id_type_chaussure=%s;"
    mycursor.execute(sql, tuple_update)
    res = get_db().commit()
    print(u'Modification d\'un type = ', id_type_chaussure, ' Nouveau nom: ', nom)
    message = u'Modification d\'un type= ' + str(id_type_chaussure) + ' Nouveau nom: ' + nom
    flash(message)
    return redirect('/admin/type-chaussure/show')  # url_for('show_type_chaussure')
