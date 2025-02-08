from app import db

# Kitap modeli
from app import db

# Kitap modeli
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_year = db.Column(db.Integer, nullable=True)
    image_filename = db.Column(db.String(255), nullable=True)  # Yeni alan!

    def __init__(self, title, author, published_year, image_filename):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.image_filename = image_filename

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
            "image_url": f"/uploads/{self.image_filename}" if self.image_filename else None
        }

