from flask import g

import pymysql.cursors

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = pymysql.connect(
            host="serveurmysql",
            user="label2",
            password="0310",
            database="BDD_label2",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return db

