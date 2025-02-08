import os

# Proje dizinini al
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLite veritabanı yolu
DATABASE_FILE = os.path.join(BASE_DIR, "books.db")

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_FILE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
