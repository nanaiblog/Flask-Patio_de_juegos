from flask import Flask, render_template

app = Flask(__name__)


@app.route( "/" , methods = ['GET'] )
def mensaje_prueba():
    return  "¡Hola Mundo!"

@app.route('/play/<int:x>/<color>')
def mostrar_cajas(x, color):
    return render_template('play.html', cantidad=x, color=color)



@app.route('/say/<nombre>')
def saludar(nombre):
    return f'¡Hola, {nombre}!'

@app.route('/repeat/<int:cantidad>/<mensaje>')
def repetir_mensaje(cantidad, mensaje):
    resultado = mensaje * cantidad
    return resultado

@app.route('/')
def mensaje_error():
    abort(404, "¡Lo siento! No hay respuesta. Inténtalo otra vez.")

@app.errorhandler(404)
def manejar_error(error):
    return error.description, 404

#ejercicios extra
@app.route('/hola/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def hola(name):
    print(name)
    return "Hola, " + name

@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__ == "__main__":
    app.run( debug = True )

