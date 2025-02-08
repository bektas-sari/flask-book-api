document.addEventListener("DOMContentLoaded", function() {
    fetchBooks();
});

function fetchBooks() {
    fetch('/books')
        .then(response => response.json())
        .then(data => {
            let table = document.getElementById('book-list');
            table.innerHTML = "";
            data.forEach(book => {
                let imageTag = book.image_url ? `<img src="${book.image_url}" alt="${book.title}">` : "No Image";
                let row = `<tr>
                    <td>${book.id}</td>
                    <td>${book.title}</td>
                    <td>${book.author}</td>
                    <td>${book.published_year || ''}</td>
                    <td>${imageTag}</td>
                    <td>
                        <button class="btn btn-warning btn-sm" onclick="updateBook(${book.id})">✏ Edit</button>
                        <button class="btn btn-danger btn-sm" onclick="deleteBook(${book.id})">🗑 Delete</button>
                    </td>
                </tr>`;
                table.innerHTML += row;
            });
        });
}

function addBook() {
    let formData = new FormData();
    formData.append("title", document.getElementById('title').value);
    formData.append("author", document.getElementById('author').value);
    formData.append("published_year", document.getElementById('year').value);
    
    let imageFile = document.getElementById('image').files[0];
    if (imageFile) {
        formData.append("image", imageFile);
    }

    fetch('/books', {
        method: "POST",
        body: formData
    }).then(() => {
        fetchBooks();
        document.getElementById('book-form').reset();
    });
}

function deleteBook(id) {
    fetch(`/books/${id}`, { method: "DELETE" })
        .then(() => fetchBooks());
}

function updateBook(id) {
    let newTitle = prompt("Enter new title:");
    let newAuthor = prompt("Enter new author:");
    let newYear = prompt("Enter new published year:");

    if (newTitle && newAuthor) {
        let formData = new FormData();
        formData.append("title", newTitle);
        formData.append("author", newAuthor);
        formData.append("published_year", newYear);

        let newImageFile = document.getElementById('image').files[0];
        if (newImageFile) {
            formData.append("image", newImageFile);
        }

        fetch(`/books/${id}`, {
            method: "PUT",
            body: formData
        }).then(() => fetchBooks());
    }
}
