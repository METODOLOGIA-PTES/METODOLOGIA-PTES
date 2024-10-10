from flask import Flask, render_template, request, redirect
app=Flask(__name__)
from flask_mysqldb import MySQL

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/Clientes')
def index_Clientes():
    return render_template('modulos/Clientes/index.html')


@app.route('/Clientes/create')
def create():
    return render_template('modulos/Clientes/create.html')

@app.route('/Clientes/create/guardar', methods=['POST'])
def Cliente_guardar():
    Nombre=request.form['Nombre']
    Teléfono=request.form['Teléfono']
    Fecha=request.form['Fecha']

    Sql="INSERT INTO Clientes (Nombre, Teléfono, Fecha) VALUES(%s, %s, %s)"
    Datos=(Nombre, Teléfono, Fecha)
    Conexion=MySQL.connection
    Cursor=Conexion.Cursor()
    Cursor.execute(Sql, Datos)
    Conexion.commit()
    return redirect('/Clientes')




if __name__ == '__main__':
    app.run(debug=True)
    