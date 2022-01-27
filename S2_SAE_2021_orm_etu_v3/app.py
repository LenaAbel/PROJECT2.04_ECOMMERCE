@app.route('/')
def show_accueil():

    return render_template('layout.html')

@app.route('/client/show')
def show_client():
    sql = "SELECT * FROM CLIENT"
    mycursor.execute(sql)
    clients = mycursor.fetchall()
    #print(types_articles)
    return render_template('client/show_clients.html', client=clients)

@app.route('/client/add', methods=['GET'])
def add_type_article():
    return render_template('client/add_client.html')

@app.route('/client/add', methods=['POST'])
def valid_add_type_article():
    nomClient = request.form.get('nomClient', '')
    prenomClient = request.form.get('prenomClient', '')
    print(u'type ajouté , libellé :', nomClient)
    sql = "INSERT INTO CLIENT VALUES (NULL , %s, %s, 1)"
    mycursor.execute(sql, (nomClient, prenomClient))
    mydb.commit()
    return redirect(url_for('show_client'))

@app.route('/client/delete', methods=['GET'])
def delete_type_article():
    id = request.args.get('id', '')
    print ("un type d'article supprimé, id :",id)
    sql = "DELETE FROM CLIENT WHERE numClient=%s"
    mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
    mycursor.execute(sql, (id))
    mydb.commit()
    return redirect(url_for('show_client'))

@app.route('/client/edit/<int:id>', methods=['GET'])
def edit_type_article(id):

    sql = "SELECT numClient, nomClient, prenomClient, numParrain FROM CLIENT WHERE numClient=%s"
    mycursor.execute(sql, (id))
    client = mycursor.fetchone()
    print(client)
    mydb.commit()
    return render_template('client/edit_client.html', client=client)

@app.route('/client/edit', methods=['POST'])
def valid_edit_type_article():
    nomClient = request.form.get('nomClient', '')
    prenomClient = request.form.get('prenomClient', '')
    numClient = request.form.get('numClient', '')
    print("un type d'article supprimé, id :", id)
    sql = "UPDATE CLIENT SET nomClient=%s, prenomClient=%s WHERE numClient=%s"
    mycursor.execute(sql, (nomClient, prenomClient, numClient))
    mydb.commit()
    print(nomClient, prenomClient, numClient)
    return redirect(url_for('show_client'))

if __name__ == '__main__':
    app.run()
