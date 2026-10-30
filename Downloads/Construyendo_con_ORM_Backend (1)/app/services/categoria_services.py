from flask import jsonify, request, abort
from sqlalchemy.exc import IntegrityError
from app.models import Categoria, db

def categoria_list():
    items = db.session.execute(db.select(Categoria).order_by(Categoria.categoria_id)).scalars().all()
    return jsonify([x.to_dict() for x in items]), 200

def categoria_detail(categoria_id):
    item = db.session.get(Categoria, categoria_id)
    if not item:
        abort(404, description="Categoría no encontrada")
    return jsonify(item.to_dict()), 200

def categoria_add():
    data = request.get_json(silent=True)
    if not data:
        abort(400, description="Envía un cuerpo JSON")
    nombre = str(data.get("nombre", "")).strip()
    descripcion = str(data.get("descripcion", "")).strip()
    if not nombre or not descripcion:
        abort(400, description="Los campos nombre y descripcion son obligatorios")
    item = Categoria(categoria_nombre=nombre, descripcion=descripcion)
    try:
        db.session.add(item)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(409, description="Ya existe una categoría con ese nombre")
    return jsonify(item.to_dict()), 201

def categoria_update(categoria_id):
    data = request.get_json(silent=True)
    if data is None:
        abort(400, description="Envía un cuerpo JSON")
    item = db.session.get(Categoria, categoria_id)
    if not item:
        abort(404, description="Categoría no encontrada")
    item.categoria_nombre = str(data.get("nombre", item.categoria_nombre)).strip()
    item.descripcion = str(data.get("descripcion", item.descripcion)).strip()
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(409, description="Ya existe una categoría con ese nombre")
    return jsonify(item.to_dict()), 200

def categoria_delete(categoria_id):
    item = db.session.get(Categoria, categoria_id)
    if not item:
        abort(404, description="Categoría no encontrada")
    if item.productos:
        abort(409, description="No puedes eliminar una categoría que tiene productos asociados")
    db.session.delete(item)
    db.session.commit()
    return jsonify({"mensaje": "Categoría eliminada correctamente"}), 200
