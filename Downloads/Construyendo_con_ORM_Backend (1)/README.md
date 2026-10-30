# Construyendo con ORM — Backend Flask + SQLAlchemy + MySQL

Proyecto organizado por capas según la guía: `common`, `controller`, `models` y `services`. Incluye CRUD de categorías, productos y entradas, y documentación Swagger.

## 1. Requisitos
- Python 3.10 o superior.
- MySQL Server encendido.
- Visual Studio Code y extensión de Python (recomendado).

## 2. Crear la base de datos
En MySQL Workbench o en la consola de MySQL ejecuta:

```sql
CREATE DATABASE construyendo_orm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 3. Configurar el proyecto en Windows (PowerShell)
Abre la carpeta `Backend` en VS Code y ejecuta:

```powershell
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Abre `.env` y cambia `DB_PASSWORD` por la contraseña real de tu usuario MySQL. Si tu usuario no es `root`, modifica también `DB_USER`. No compartas el archivo `.env`.

## 4. Ejecutar
Con el entorno virtual activado:

```powershell
python main.py
```

Prueba la API:
- Inicio: http://127.0.0.1:5000/
- Swagger: http://127.0.0.1:5000/apidocs/

Las tablas se crean automáticamente al iniciar el backend. Si MySQL no está iniciado o la clave está incorrecta, la conexión fallará.

## 5. Rutas
| Método | Ruta | Acción |
|---|---|---|
| GET | `/categorias` | Listar categorías |
| GET | `/categorias/<id>` | Ver categoría |
| POST | `/categorias` | Crear categoría |
| PUT | `/categorias/<id>` | Actualizar categoría |
| DELETE | `/categorias/<id>` | Eliminar categoría |
| GET | `/products` | Listar productos |
| GET | `/products/<id>` | Ver producto |
| POST | `/products` | Crear producto |
| PUT | `/products/<id>` | Actualizar producto |
| DELETE | `/products/<id>` | Eliminar producto |
| GET | `/entradas` | Listar entradas |
| GET | `/entradas/<id>` | Ver entrada |
| POST | `/entradas` | Crear entrada |
| PUT | `/entradas/<id>` | Actualizar entrada |
| DELETE | `/entradas/<id>` | Eliminar entrada |

## 6. Datos de la guía
En Swagger (`/apidocs/`) crea primero las 5 categorías, luego los productos y finalmente las entradas. La guía adjunta incluye ejemplos de datos para esas tres entidades. Para crear una entrada, el `entra_producto_id` debe corresponder a un producto que ya exista.

Nota: la tabla de productos exige `stock_min`; el precio debe ser mayor que cero. Para crear una entrada, envía factura, stand y ubicación además de producto y cantidad.
