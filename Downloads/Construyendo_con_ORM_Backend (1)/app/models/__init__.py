from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .categoria import Categoria
from .producto import Producto
from .entrada import Entrada

__all__ = ["db", "Categoria", "Producto", "Entrada"]
