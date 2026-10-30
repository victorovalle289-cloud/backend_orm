from . import db

class Categoria(db.Model):
    __tablename__ = "categorias"

    categoria_id = db.Column(db.Integer, primary_key=True)
    categoria_nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(150), nullable=False)

    productos = db.relationship("Producto", back_populates="categoria", lazy=True)

    def to_dict(self):
        return {
            "id": self.categoria_id,
            "nombre": self.categoria_nombre,
            "descripcion": self.descripcion
        }
