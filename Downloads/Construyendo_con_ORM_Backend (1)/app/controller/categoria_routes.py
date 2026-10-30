from flask import Blueprint
from app.services import categoria_list, categoria_detail, categoria_add, categoria_update, categoria_delete

categoria_bp = Blueprint("categorias", __name__)

@categoria_bp.route("/categorias", methods=["GET"])
def get_categoria_list():
    """Lista categorías.
    ---
    responses:
      200:
        description: Lista de categorías
    """
    return categoria_list()

@categoria_bp.route("/categorias/<int:categoria_id>", methods=["GET"])
def get_categoria_detail(categoria_id):
    """Consulta una categoría por ID.
    ---
    parameters:
      - name: categoria_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Categoría encontrada
      404:
        description: Categoría no encontrada
    """
    return categoria_detail(categoria_id)

@categoria_bp.route("/categorias", methods=["POST"])
def get_categoria_add():
    """Crea una categoría.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [nombre, descripcion]
          properties:
            nombre:
              type: string
              example: Electrónica
            descripcion:
              type: string
              example: Dispositivos electrónicos y accesorios
    responses:
      201:
        description: Categoría creada
    """
    return categoria_add()

@categoria_bp.route("/categorias/<int:categoria_id>", methods=["PUT"])
def get_categoria_update(categoria_id):
    return categoria_update(categoria_id)

@categoria_bp.route("/categorias/<int:categoria_id>", methods=["DELETE"])
def get_categoria_delete(categoria_id):
    return categoria_delete(categoria_id)
