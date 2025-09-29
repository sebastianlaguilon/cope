from flask import Flask,render_template
from rutas.habitaciones import habitaciones_bp
from rutas.clientes import clientes_bp
from rutas.reservas import reservas_bp
from modelos import inicializar_csv 

app = Flask(__name__)
app.secret_key = 'clave-secreta'

inicializar_csv()

app.register_blueprint(habitaciones_bp)
app.register_blueprint(clientes_bp)
app.register_blueprint(reservas_bp)

@app.route('/')
def inicio():
    return render_template('inicio.html')



if __name__ == '__main__':
    app.run(debug=True)


