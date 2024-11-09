import sqlite3
from flask import  Flask, render_template, abort, request, url_for, redirect

def get_db_connection():
    conn = sqlite3.connect("alumnos.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)


@app.route('/', methods=['GET'])
def base():
    return render_template('home.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/estudiante', methods = ['GET'])
def get_all_estudiantes():
    conn = get_db_connection()
    estudiantes = conn.execute('SELECT * FROM alumnos').fetchall()
    conn.close()
    return render_template('estudiante/estudiantes.html', estudiantes = estudiantes)

@app.route('/estudiante/<int:estudiante_id>', methods=['GET'])
def get_one_estudiante(estudiante_id):
    conn = get_db_connection()
    estudiante = conn.execute('SELECT * FROM alumnos WHERE id = ?', (estudiante_id,)).fetchone()
    conn.close()
    return render_template('estudiante/estudiantes.html', estudiante=estudiante)

@app.route('/estudiante/create', methods=['GET','POST'])
def create_one_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = request.form['aprobado']
        nota = request.form['nota']
        fecha = request.form['fecha']


        conn = get_db_connection()
        conn.execute('INSERT INTO alumnos (nombre, apellido,aprobado,nota, fecha) VALUES (?,?,?,?, ?)', (nombre, apellido,aprobado,nota,fecha))
        conn.commit()
        conn.close()
        return redirect(url_for('get_all_estudiantes'))

    return render_template('estudiante/create.html')


@app.route('/estudiante/edit/<int:estudiante_id>', methods=['GET', 'POST'])
def edit_one_estudiante(estudiante_id):
    conn = get_db_connection()
    estudiante = conn.execute('SELECT * FROM alumnos WHERE id = ?', (estudiante_id,)).fetchone()
    conn.close()
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = request.form['aprobado']
        nota = request.form['nota']
        fecha = request.form['fecha']

        conn = get_db_connection()
        conn.execute('UPDATE alumnos SET nombre = ?, apellido = ?,aprobado = ?,nota =? , fecha = ?  WHERE id = ?', (nombre, apellido, aprobado, nota, fecha,estudiante_id))
        conn.commit()
        conn.close()
        return redirect(url_for('get_all_estudiantes'))

    elif request.method == 'GET':
        return render_template('estudiante/edit.html', estudiante=estudiante)


@app.route('/estudiante/delete/<int:estudiante_id>', methods=['POST'])
def delete_one_estudiante(estudiante_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM alumnos WHERE id = ?', (estudiante_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('get_all_estudiantes'))

if __name__ == '__main__':
    app.run(debug=True, port=80, host="localhost")
########################################################################## END BLOQUE 2
