import sqlite3
from flask import Flask
from flask_cors import CORS

from flask import Flask, request


app = Flask(__name__)
CORS(app)

@app.route('/save_data', methods=['POST'])
def save_data_route():
    print("estou aqui")
    data = request.get_json()
    print(data)
    save_data(data['username'], data['email'], data['password'])
    return 'Dados salvos com sucesso!'

def save_data(username, email, password):
    conn = sqlite3.connect('cadastro.db')
    c = conn.cursor()
    c.execute("INSERT INTO register VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()