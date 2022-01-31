#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

admin_dataviz_chaussure = Blueprint('admin_dataviz_chaussure', __name__,
                        template_folder='templates')

@admin_dataviz_chaussure.route('/admin/type-chaussure/bilan-stock')
def show_type_chaussure_stock():
    mycursor = get_db().cursor()
    types_chaussures_cout = []
    labels = []
    values = []
    cout_total = 0
    return render_template('admin/dataviz/etat_type_chaussure_stock.html',
                           types_chaussures_cout=types_chaussures_cout, cout_total=cout_total
                           , labels=labels, values=values)


@admin_dataviz_chaussure.route('/admin/chaussure/bilan')
def show_chaussure_bilan():
    mycursor = get_db().cursor()

    types_chaussures_cout = []
    labels = []
    values = []
    cout_total = 0
    return render_template('admin/dataviz/etat_chaussure_vente.html',
                           types_chaussures_cout=types_chaussures_cout, cout_total=cout_total
                           , labels=labels, values=values)
