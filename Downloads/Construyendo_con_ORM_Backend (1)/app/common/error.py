from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(HTTPException)
def handle_http_error(err):
    return jsonify({
        "error": err.name,
        "descripcion": err.description
    }), err.code

@error_bp.app_errorhandler(Exception)
def handle_unexpected_error(err):
    return jsonify({
        "error": "Error interno del servidor",
        "descripcion": str(err)
    }), 500
