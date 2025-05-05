from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY id ASC;")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    price = request.form['price']
    pages = request.form['pages']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, price, pages) VALUES (%s, %s, %s, %s);",
        (title, author, price, pages)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        pages = request.form['pages']
        cursor.execute(
            "UPDATE books SET title=%s, author=%s, price=%s, pages=%s WHERE id=%s;",
            (title, author, price, pages, book_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM books WHERE id = %s;", (book_id,))
        book = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('edit.html', book=book)

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book_ui(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s;", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# ---------------- REST APIs ----------------

@app.route('/api/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY id ASC;")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(books)

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = %s;", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(book) if book else ('Not found', 404)



if __name__ == '__main__':
    app.run(debug=True)
