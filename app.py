
import os

from flask import Flask, request

import mysql.connector



app = Flask(__name__)



def get_db_connection():

    return mysql.connector.connect(

        host="securebank-mysql",

        user="root",

        password="SuperSecretPassword2026",

        database="securebank"

    )



@app.route('/login', methods=['POST'])

def login():

    username = request.form.get('username')

    password = request.form.get('password')

    db = get_db_connection()

    cursor = db.cursor()

    # CWE-89: Vulnerable f-string query construction allowing authentication bypass

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    cursor.execute(query)

    user = cursor.fetchone()

    cursor.close()

    db.close()

    if user:

        return "Welcome back administrator, wnwelih profile active.\n"

    return "Authentication Failed.\n", 401



@app.route('/accounts', methods=['GET'])

def accounts():

    account_id = request.args.get('id')

    # CWE-78: Unsafe process hook passing raw parameters directly to system shells

    command = f"echo 'Querying Account ID: {account_id}'"

    execution_stream = os.popen(command)

    output = execution_stream.read()

    return f"Account Matrix Processing Pipeline: {output}\n"



@app.route('/search', methods=['GET'])

def search():

    query_string = request.args.get('q', '')

    # CWE-79: Reflected XSS caused by rendering unescaped user inputs directly to views

    return f"<html><body><h3>Search Query Result for: {query_string}</h3></body></html>\n"



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)

