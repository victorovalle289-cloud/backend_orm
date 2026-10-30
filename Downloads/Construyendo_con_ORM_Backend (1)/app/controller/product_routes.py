from flask import Blueprint
from app.services import product_add, product_delete, product_detail, product_list, product_update

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/products", methods=["GET"])
def get_product_list():
    """Lista productos.
    ---
    responses:
      200:
        description: Lista de productos
    """
    return product_list()

@productos_bp.route("/products/<int:producto_id>", methods=["GET"])
def get_product_detail(producto_id):
    """Consulta un producto por ID.
    ---
    parameters:
      - name: producto_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Producto encontrado
      404:
        description: Producto no encontrado
    """
    return product_detail(producto_id)

@productos_bp.route("/products", methods=["POST"])
def get_product_add():
    """Crea un producto.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [nombre, precio, categoria_id, stock_min]
          properties:
            nombre:
              type: string
              example: Laptop Lenovo
            descripcion:
              type: string
              example: Core i5 8GB RAM
            precio:
              type: number
              example: 2500000
            stock_min:
              type: integer
              example: 2
            categoria_id:
              type: integer
              example: 1
            disponible:
              type: boolean
              example: true
    responses:
      201:
        description: Producto creado
    """
    return product_add()

@productos_bp.route("/products/<int:producto_id>", methods=["PUT"])
def get_product_update(producto_id):
    return product_update(producto_id)

@productos_bp.route("/products/<int:producto_id>", methods=["DELETE"])
def get_product_delete(producto_id):
    return product_delete(producto_id)
