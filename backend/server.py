#import psycopg2
#utilisé pour set up la db
#import os
from dotenv import load_dotenv
from flask import Flask,render_template, request, redirect,url_for

load_dotenv()

#je set up le serveur avec flask
#pour run le serveur en dev mode dans le cmd avec .venv activé: flask --app server run
app = Flask(__name__)
#j'importe ma fonction sous forme de module.
from db.PostGredb import db_conn

#GET ma data
@app.route('/')
def index():
    conn = db_conn()
    cursor = conn.cursor()
    cursor.execute('''SELECT*FROM rooms ORDER BY id''')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html',data= data)

#POST creer une nouvelle entrée dans la db vec les différends champs à compléter
@app.route('/create',methods=["POST"])
def create():
    conn = db_conn()
    cursor = conn.cursor()
    name = request.form["name"]
    description = request.form["description"]
    email = request.form["email"]
    cursor.execute('''INSERT INTO rooms (name,description,email) VALUES(%s,%s,%s)''',(name,description,email))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

#POST Update des infos de la db
@app.route('/update',methods=['POST'])
def update():
    conn = db_conn()
    cursor = conn.cursor()
    name = request.form["name"]
    description = request.form["description"]
    email = request.form["email"]
    id = request.form["id"]
    cursor.execute('''UPDATE rooms SET name=%s,description=%s,email=%s WHERE id=%s''',(name,description,email,id))    
    conn.commit()
    return redirect(url_for('index'))

#POST Delete une entrée de la data via l'id.
@app.route('/delete', methods=["POST"])
def delete():
    conn = db_conn()
    cursor = conn.cursor()
    id = request.form["id"]
    cursor.execute('''DELETE FROM rooms WHERE id={0}'''.format(id))#ici format parce que j'ai eu des erreurs de formatage avec %s qui bloquaient les requetes de delete
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


