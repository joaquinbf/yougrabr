from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import op
import json

""" base de datos simulada """
db = None

with open("db.json", "r") as db_file:
    db = json.load(db_file)

""" Se crea un servidor """
app = Flask(__name__)


""" ruta index """
@app.route('/')
def index():
    paquetes = db["paquetes"]
    paquetes = op.paquetes_ordenados(paquetes)
    origenes = op.origenes(db)
    destinos = op.destinos(db)
    return render_template('index.html',paquetes=paquetes, 
                                        origenes=origenes, 
                                        destinos=destinos)


""" ruta buscar """
@app.route('/buscar/')
def buscar_paquetes():
    paquetes = db["paquetes"]
    origenes = op.origenes(db)
    destinos = op.destinos(db)

    origen = request.args.get('origen-input')
    destino = request.args.get('destino-input')

    fecha_ida = request.args.get('fecha-ida')
    fecha_vuelta = request.args.get('fecha-vuelta')

    cant_adultos = request.args.get('cant-adultos')
    cant_menores = request.args.get('cant-menores')
    cant_habitaciones = request.args.get('cant-habitaciones')
    
    paquetes = op.filtrar_paquetes_segun_lugar(paquetes, origen, destino)
    paquetes = op.filtrar_paquetes_segun_fecha(paquetes,fecha_ida, fecha_vuelta)
    paquetes = op.filtrar_paquetes_segun_personas(paquetes, cant_adultos, cant_menores, cant_habitaciones)
    
    paquetes = op.paquetes_ordenados(paquetes)
    return render_template('index.html',paquetes=paquetes, 
                                        origenes=origenes, 
                                        destinos=destinos)

# Se inicia el servidor en el puerto 4000 del localhost
if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=4000)
