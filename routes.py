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
      
# try:
    
#     conn = sqlite3.connect('cadastro.db')
#     cursor = conn.cursor()
    
#     cursor.execute("DELETE from register WHERE email = 'anas@gmil.com'")
    
#     conn.commit()
#     conn.close()
#     print("os dados foram removidos com sucesso!")
    
# except sqlite3.Error as erro:
#     print("Erro ao Excluir ", erro)
    
try:
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE register SET email = 'lover288@gmail.com' WHERE email = 'lover277@gmail.com'")
    
    conn.commit()
    conn.close()
    print("os dados foram atualizados com sucesso!")
    
except sqlite3.Error as erro:
    print("Erro ao atualizar ", erro)
    


