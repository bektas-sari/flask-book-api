from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config

# Flask uygulamasını başlat
app = Flask(__name__)

# Config ayarlarını yükle
app.config.from_object(Config)

# CORS (Cross-Origin Resource Sharing) aktif et
CORS(app)

# Veritabanını başlat
db = SQLAlchemy(app)

# Rotaları içe aktar
from app.routes import *

# Veritabanı tablolarını oluştur
with app.app_context():
    db.create_all()
