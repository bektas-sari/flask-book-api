# 📚 Flask Book API

A RESTful API built with Flask to manage books, allowing users to **add, delete, update, and list books**.  
It also supports **image uploads** for book covers and provides a **simple web interface** for interaction.  

## ✨ Features
- ✅ **RESTful API** with CRUD operations.
- ✅ **Image upload support** for book covers.
- ✅ **SQLite database** for storage.
- ✅ **Web UI** with Bootstrap for easy book management.
- ✅ **Flask CORS support** for cross-origin requests.

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/bektas-sari/flask-book-api.git
cd flask-book-api
```
### **2️⃣ Create a Virtual Environment & Install Dependencies**
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt

### **3️⃣ Run the Application**
python run.py

📌 API Endpoints
🔹 1. Get All Books
Endpoint: GET /books
Response:
json
Kopyala
Düzenle
[
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949,
        "image_url": "/uploads/1984-cover.jpg"
    }
]
🔹 2. Get a Single Book by ID
Endpoint: GET /books/<id>
Example: GET /books/1
Response:
json
Kopyala
Düzenle
{
    "id": 1,
    "title": "1984",
    "author": "George Orwell",
    "published_year": 1949,
    "image_url": "/uploads/1984-cover.jpg"
}
🔹 3. Add a New Book (With Image Upload)
Endpoint: POST /books
Content-Type: multipart/form-data
Request Body (Form Data):
title: string (Required)
author: string (Required)
published_year: integer (Optional)
image: file (Optional)

Example (cURL Command):
curl -X POST http://127.0.0.1:5000/books -F "title=Animal Farm" -F "author=George Orwell" -F "published_year=1945" -F "image=@cover.jpg"

Response:
{
    "id": 2,
    "title": "Animal Farm",
    "author": "George Orwell",
    "published_year": 1945,
    "image_url": "/uploads/animal-farm.jpg"
}

🔹 4. Update a Book
Endpoint: PUT /books/<id>
Content-Type: multipart/form-data
Example Request (Update Title & Author):

curl -X PUT http://127.0.0.1:5000/books/1 -F "title=Brave New World" -F "author=Aldous Huxley"

Response:
{
    "id": 1,
    "title": "Brave New World",
    "author": "Aldous Huxley",
    "published_year": 1949,
    "image_url": "/uploads/1984-cover.jpg"
}

🔹 5. Delete a Book
Endpoint: DELETE /books/<id>
Example: DELETE /books/2

Response:
{
    "message": "Book deleted successfully"
}

🔹 6. Serve Uploaded Images
Endpoint: GET /uploads/<filename>
Example: GET /uploads/1984-cover.jpg
Displays the book cover image.

🖥️ Web UI
This project also includes a simple web interface for managing books visually.

http://127.0.0.1:5000/web

🎨 Features:
* 📄 List books
* ➕ Add books (with image upload)
* ✏ Edit books
* 🗑 Delete books
* 📷 View book covers

🛠️ Technologies Used
* Backend: Flask, Flask-RESTful, Flask-SQLAlchemy, Flask-CORS
* Database: SQLite
* Frontend: HTML, CSS (Bootstrap), JavaScript (Fetch API)
* Storage: Local file storage for images

📌 Folder Structure
```
flask-book-api/
│── app/
│   ├── static/
│   │   ├── css/style.css
│   │   ├── js/script.js
│   │   ├── uploads/ (Book images)
│   ├── templates/
│   │   ├── index.html
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
│── run.py
│── requirements.txt
│── README.md
```

🤝 Contributing
Contributions are welcome! Feel free to:

* Open an issue
* Submit a pull request
* Improve the documentation

🏆 Author
bektas-sari – GitHub
flask-book-api: GitHub

📜 License
This project is licensed under the MIT License.
