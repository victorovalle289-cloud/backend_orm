from datetime import date
from . import db

class Producto(db.Model):
    __tablename__ = "productos"

    producto_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock_min = db.Column(db.Integer, nullable=False, default=0)
    fecha_registro = db.Column(db.Date, nullable=False, default=date.today)
    disponible = db.Column(db.Boolean, nullable=False, default=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.categoria_id"), nullable=False)

    categoria = db.relationship("Categoria", back_populates="productos")
    entradas = db.relationship("Entrada", back_populates="producto", lazy=True)

    def to_dict(self):
        return {
            "id": self.producto_id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": float(self.precio) if self.precio is not None else None,
            "stock_min": self.stock_min,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None,
            "disponible": self.disponible,
            "categoria_id": self.categoria_id,
            "categoria_nombre": self.categoria.categoria_nombre if self.categoria else None
        }
