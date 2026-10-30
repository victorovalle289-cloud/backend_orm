from flask import Blueprint
from app.services import entrada_list, entrada_detail, entrada_add, entrada_update, entrada_delete

entrada_bp = Blueprint("entradas", __name__)

@entrada_bp.route("/entradas", methods=["GET"])
def get_entrada_list():
    """Lista entradas de inventario.
    ---
    responses:
      200:
        description: Lista de entradas
    """
    return entrada_list()

@entrada_bp.route("/entradas/<int:entrada_id>", methods=["GET"])
def get_entrada_detail(entrada_id):
    """Consulta una entrada por ID.
    ---
    parameters:
      - name: entrada_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Entrada encontrada
    """
    return entrada_detail(entrada_id)

@entrada_bp.route("/entradas", methods=["POST"])
def get_entrada_add():
    """Registra una entrada de inventario.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [entra_producto_id, entra_cantidad, entra_factura, entra_stand, entra_ubicacion]
          properties:
            entra_producto_id:
              type: integer
              example: 1
            entra_cantidad:
              type: integer
              example: 10
            entra_factura:
              type: string
              example: FAC-001
            entra_stand:
              type: string
              example: A1
            entra_ubicacion:
              type: string
              example: Bodega Principal
    responses:
      201:
        description: Entrada registrada
    """
    return entrada_add()

@entrada_bp.route("/entradas/<int:entrada_id>", methods=["PUT"])
def get_entrada_update(entrada_id):
    return entrada_update(entrada_id)

@entrada_bp.route("/entradas/<int:entrada_id>", methods=["DELETE"])
def get_entrada_delete(entrada_id):
    return entrada_delete(entrada_id)
