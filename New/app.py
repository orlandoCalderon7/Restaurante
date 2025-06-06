from flask import Flask, render_template, jsonify, request, redirect, url_for
import mysql.connector
import pymysql



mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "restaurant"
)
    
myCursor = mydb.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/registrado_menu')
def registrado_menu():
    return render_template('registrado_menu.html')
         
    
@app.route('/registro', methods=['POST'])
def registro():
    try:
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            email = request.form['email']
            telefono = request.form['telefono']
            dni = request.form['dni']
            query = f"INSERT INTO clientes (nombre, apellidos, email, telefono, dni) VALUES ('{nombre}', '{apellidos}', '{email}', {telefono}, {dni})"
            myCursor.execute(query)
            result = myCursor.fetchall()
            mydb.commit()
            
            return render_template('registrado.html')                    
            
        else:
            return "Error en el envío"
        
    except Exception as ex:                
        return 'Error'


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/registro_pedido', methods=['POST'])
def registro_pedido():
    try:
        if request.method == 'POST':
            data = request.get_json()
            pedido = data['pedido']
            query = f"INSERT INTO orden (pedido) VALUES ('{pedido}')"
            myCursor.execute(query)
            mydb.commit()                        
            
            return jsonify({"mensaje": "Pedido registrado correctamente"})                   
            
        else:
            return "Error en el envío"
        
    except Exception as ex:                
        return 'Error'

    
    
if __name__ == '__main__':
    app.run(debug=True)


