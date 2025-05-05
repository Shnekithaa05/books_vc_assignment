import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  

conn = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        price INTEGER,
        pages INTEGER
    );
''')

cursor.execute('''
    INSERT INTO books (title, author, price, pages)
    VALUES
    ('Flask Basics', 'John Doe', 300, 150),
    ('Advanced PostgreSQL', 'Jane Roe', 450, 350)
    ON CONFLICT DO NOTHING;
''')

conn.commit()
cursor.close()
conn.close()

print("Table `books` created and seeded successfully.")
