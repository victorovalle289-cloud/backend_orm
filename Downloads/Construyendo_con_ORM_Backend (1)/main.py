
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from dotenv import load_dotenv

from app.models import db
from app.common import Config, error_bp
from app.controller import productos_bp, categoria_bp, entrada_bp

# Cargar las variables de entorno
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar la aplicación
app.config.from_object(Config)

# Configurar Swagger
app.config["SWAGGER"] = {
    "title": "Construyendo con ORM - API",
    "uiversion": 3
}

swagger = Swagger(
    app,
    config={
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
)

# Habilitar CORS
CORS(app)

# Inicializar SQLAlchemy
db.init_app(app)

# Crear las tablas definidas en los modelos
with app.app_context():
    db.create_all()

# Registrar el manejador de errores
app.register_blueprint(error_bp)

# Registrar las rutas de la API
app.register_blueprint(productos_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(entrada_bp)

# Ruta principal para comprobar el funcionamiento
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensaje": "API funcionando correctamente"
    }), 200

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
