from flask import jsonify, request, abort
from app.models import Producto, Categoria, db

def product_list():
    items = db.session.execute(db.select(Producto).order_by(Producto.producto_id)).scalars().all()
    return jsonify([x.to_dict() for x in items]), 200

def product_detail(producto_id):
    item = db.session.get(Producto, producto_id)
    if not item:
        abort(404, description="Producto no encontrado")
    return jsonify(item.to_dict()), 200

def product_add():
    data = request.get_json(silent=True)
    if not data:
        abort(400, description="Envía un cuerpo JSON")
    for field in ("nombre", "precio", "categoria_id", "stock_min"):
        if field not in data:
            abort(400, description=f"Falta el campo obligatorio: {field}")
    try:
        precio = float(data["precio"])
        categoria_id = int(data["categoria_id"])
        stock_min = int(data["stock_min"])
    except (TypeError, ValueError):
        abort(422, description="precio, categoria_id y stock_min deben tener valores numéricos válidos")
    if precio <= 0 or stock_min < 0:
        abort(422, description="El precio debe ser mayor que cero y stock_min no puede ser negativo")
    categoria = db.session.get(Categoria, categoria_id)
    if not categoria:
        abort(400, description="La categoría no existe")
    item = Producto(
        nombre=str(data["nombre"]).strip(),
        descripcion=data.get("descripcion"),
        precio=precio,
        stock_min=stock_min,
        disponible=bool(data.get("disponible", True)),
        categoria_id=categoria_id
    )
    if not item.nombre:
        abort(400, description="El nombre es obligatorio")
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

def product_update(producto_id):
    data = request.get_json(silent=True)
    if data is None:
        abort(400, description="Envía un cuerpo JSON")
    item = db.session.get(Producto, producto_id)
    if not item:
        abort(404, description="Producto no encontrado")
    if "nombre" in data:
        item.nombre = str(data["nombre"]).strip()
    if "descripcion" in data:
        item.descripcion = data["descripcion"]
    if "precio" in data:
        try:
            item.precio = float(data["precio"])
        except (TypeError, ValueError):
            abort(422, description="El precio debe ser numérico")
        if item.precio <= 0:
            abort(422, description="El precio debe ser mayor que cero")
    if "stock_min" in data:
        try:
            item.stock_min = int(data["stock_min"])
        except (TypeError, ValueError):
            abort(422, description="stock_min debe ser entero")
        if item.stock_min < 0:
            abort(422, description="stock_min no puede ser negativo")
    if "disponible" in data:
        item.disponible = bool(data["disponible"])
    if "categoria_id" in data:
        categoria = db.session.get(Categoria, data["categoria_id"])
        if not categoria:
            abort(400, description="La categoría no existe")
        item.categoria_id = categoria.categoria_id
    db.session.commit()
    return jsonify(item.to_dict()), 200

def product_delete(producto_id):
    item = db.session.get(Producto, producto_id)
    if not item:
        abort(404, description="Producto no encontrado")
    if item.entradas:
        abort(409, description="No puedes eliminar un producto que tiene entradas asociadas")
    db.session.delete(item)
    db.session.commit()
    return jsonify({"mensaje": "Producto eliminado correctamente"}), 200
