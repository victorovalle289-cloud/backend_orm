from flask import jsonify, request, abort
from app.models import Entrada, Producto, db

def entrada_list():
    items = db.session.execute(db.select(Entrada).order_by(Entrada.entra_id)).scalars().all()
    return jsonify([x.to_dict() for x in items]), 200

def entrada_detail(entrada_id):
    item = db.session.get(Entrada, entrada_id)
    if not item:
        abort(404, description="Entrada no encontrada")
    return jsonify(item.to_dict()), 200

def entrada_add():
    data = request.get_json(silent=True)
    if not data:
        abort(400, description="Envía un cuerpo JSON")
    required = ("entra_producto_id", "entra_cantidad", "entra_factura", "entra_stand", "entra_ubicacion")
    for field in required:
        if field not in data or data[field] in (None, ""):
            abort(400, description=f"Falta el campo obligatorio: {field}")
    try:
        producto_id = int(data["entra_producto_id"])
        cantidad = int(data["entra_cantidad"])
    except (TypeError, ValueError):
        abort(422, description="producto_id y cantidad deben ser enteros")
    if cantidad <= 0:
        abort(422, description="La cantidad debe ser mayor que cero")
    if not db.session.get(Producto, producto_id):
        abort(400, description="El producto no existe")
    item = Entrada(
        entra_producto_id=producto_id,
        entra_cantidad=cantidad,
        entra_factura=str(data["entra_factura"]),
        entra_stand=str(data["entra_stand"]),
        entra_ubicacion=str(data["entra_ubicacion"])
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

def entrada_update(entrada_id):
    data = request.get_json(silent=True)
    if data is None:
        abort(400, description="Envía un cuerpo JSON")
    item = db.session.get(Entrada, entrada_id)
    if not item:
        abort(404, description="Entrada no encontrada")
    if "entra_producto_id" in data:
        try:
            producto_id = int(data["entra_producto_id"])
        except (TypeError, ValueError):
            abort(422, description="entra_producto_id debe ser entero")
        if not db.session.get(Producto, producto_id):
            abort(400, description="El producto no existe")
        item.entra_producto_id = producto_id
    if "entra_cantidad" in data:
        try:
            item.entra_cantidad = int(data["entra_cantidad"])
        except (TypeError, ValueError):
            abort(422, description="entra_cantidad debe ser entero")
        if item.entra_cantidad <= 0:
            abort(422, description="La cantidad debe ser mayor que cero")
    for field in ("entra_factura", "entra_stand", "entra_ubicacion"):
        if field in data:
            setattr(item, field, str(data[field]))
    db.session.commit()
    return jsonify(item.to_dict()), 200

def entrada_delete(entrada_id):
    item = db.session.get(Entrada, entrada_id)
    if not item:
        abort(404, description="Entrada no encontrada")
    db.session.delete(item)
    db.session.commit()
    return jsonify({"mensaje": "Entrada eliminada correctamente"}), 200
