from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola! Bienvenido a mi aplicación utilizando flask.'

@app.route('/usuario/<sebas>')
def usuario(sebas):
    return f'Bienvenido, {sebas}!'

@app.route('/contacto')
def contacto(sebastian):
    return "Página de contacto: puedes escribirnos a contacto@miweb.com"

@app.route('/contacto/<persona>')
def contacto_persona(persona):
    return f"Hola {persona}, gracias por visitar la página de contacto."

@app.route('/acerca/<tema>')
def acerca(tema):
    return f"Sección Acerca de: aquí encontrarás información sobre {tema}."




if __name__ == '__main__':
    app.run(debug=True)