# 📚 Flask Book Manager App

A simple CRUD web application built with **Flask** and **PostgreSQL** to manage a list of books. It includes both a web interface and a set of RESTful API endpoints.

---

## 🚀 Features

- Add, edit, delete, and list books.
- Full RESTful API support for external tools like Postman.
- Clean HTML UI for direct interaction.
- PostgreSQL as the backend database.
- Environment variables for secure database credentials.

---

## 🧱 Tech Stack

- Python 3
- Flask
- PostgreSQL
- HTML/CSS
- psycopg2
- python-dotenv

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Shnekithaa05/books_vc_assignment.git
cd books_vc_assignment
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a .env file in the project root:
```bash
DB_NAME=flaskpostgres_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

### 5. Set Up the Database

Ensure PostgreSQL is running. Then run the database setup script:

```bash
python init_db.py
```
- This will create the books table (if not exists)
- Seed it with sample data

### 6. Run the Flask App
```bash
flask run
```

Go to http://127.0.0.1:5000 to use the UI.

---

## 📬 API Endpoints

Use a tool like Postman to interact with the following endpoints:

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| GET    | `/api/books`       | Get all books           |
| GET    | `/api/books/<id>`  | Get book by ID          |
| POST   | `/add` (form data) | Add book (HTML form)    |
| POST   | `/edit/<id>`       | Update book (HTML form) |
| POST   | `/delete/<id>`     | Delete book (HTML form) |


