#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

admin_users = Blueprint('admin_users', __name__,
                        template_folder='templates')


@admin_users.route('/admin/users/show')
def admin_users_show():
    cursor = get_db().cursor()
    sql = "SELECT * FROM UTILISATEUR"
    cursor.execute(sql)
    utilisateurs = cursor.fetchall()
    print(utilisateurs)
    return render_template('admin/users/show_users.html', utilisateurs=utilisateurs)
