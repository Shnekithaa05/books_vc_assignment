import psycopg2

conn = psycopg2.connect(
    database="flaskpostgres_db",
    user="postgres",
    password="mugu",
    host="localhost",
    port="5432"
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
