import os
from flask import request, jsonify, render_template
from werkzeug.utils import secure_filename
from app import app, db
from app.models import Book

# 📌 Yüklenen resimleri kaydedeceğimiz klasör
UPLOAD_FOLDER = "app/static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}

# 📌 Yüklenen dosyanın uzantısını kontrol et
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

# 🌐 Ana Sayfa (Web Arayüzü)
@app.route("/web")
def web_ui():
    return render_template("index.html")

# 📌 API Ana Sayfası
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask Book API!"})

# 📌 Tüm kitapları listeleme (GET)
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# 📌 Belirli bir kitabı ID ile getirme (GET)
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404

# 📌 Yeni kitap ekleme (POST) - Fotoğraf yükleme destekleniyor
@app.route("/books", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    published_year = request.form.get("published_year")
    image_file = request.files.get("image")

    if not title or not author:
        return jsonify({"error": "Missing title or author"}), 400

    filename = None
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    new_book = Book(title=title, author=author, published_year=published_year, image_filename=filename)

    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201

# 📌 Kitabı güncelleme (PUT)
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.form or request.get_json()
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.published_year = data.get("published_year", book.published_year)

    # Eğer yeni bir resim yüklenirse, eskiyi değiştirelim
    image_file = request.files.get("image")
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        image_file.save(image_path)
        book.image_filename = filename  # Güncellenen görseli kaydet

    db.session.commit()
    return jsonify(book.to_dict())

# 📌 Kitabı silme (DELETE)
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    # Kitaba ait resim varsa, onu da silelim
    if book.image_filename:
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], book.image_filename)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"})

# 📌 Yüklenen resimleri istemcilere göstermek için bir yol
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return app.send_static_file(f"uploads/{filename}")
