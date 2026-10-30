import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Forzar la carga del archivo .env desde la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(
            user=quote_plus(os.getenv("DB_USER", "root")),
            password=quote_plus(os.getenv("DB_PASSWORD", "")),
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=os.getenv("DB_PORT", "3306"),
            database=os.getenv("DB_NAME", "construyendo_orm"),
        ),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False