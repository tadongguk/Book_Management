import sqlite3

# Connect to the database (will create a new one if it doesn't exist)
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

# Create authors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_year INTEGER,
    country TEXT
)
''')

# Create genres table
cursor.execute('''
CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# Create books table (with foreign keys to authors and genres)
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    genre_id INTEGER,
    year INTEGER,
    isbn TEXT,
    FOREIGN KEY (author_id) REFERENCES authors (id),
    FOREIGN KEY (genre_id) REFERENCES genres (id)
)
''')

# Create readers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT
)
''')

# Create loans table
cursor.execute('''
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    reader_id INTEGER,
    loan_date TEXT,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES books (id),
    FOREIGN KEY (reader_id) REFERENCES readers (id)
)
''')

# Add sample data to authors table
authors = [
    ('Harper Lee', 1926, 'USA'),
    ('George Orwell', 1903, 'UK'),
    ('Jane Austen', 1775, 'UK'),
    ('F. Scott Fitzgerald', 1896, 'USA'),
    ('Gabriel García Márquez', 1927, 'Colombia')
]
cursor.executemany('INSERT INTO authors (name, birth_year, country) VALUES (?, ?, ?)', authors)

# Add sample data to genres table
genres = [('Fiction',), ('Science Fiction',), ('Romance',), ('Classic',), ('Magical Realism',)]
cursor.executemany('INSERT INTO genres (name) VALUES (?)', genres)

# Add sample data to books table
books = [
    ('To Kill a Mockingbird', 1, 1, 1960, '978-0446310789'),
    ('1984', 2, 2, 1949, '978-0451524935'),
    ('Pride and Prejudice', 3, 3, 1813, '978-0141439518'),
    ('The Great Gatsby', 4, 4, 1925, '978-0743273565'),
    ('One Hundred Years of Solitude', 5, 5, 1967, '978-0060883287')
]
cursor.executemany('INSERT INTO books (title, author_id, genre_id, year, isbn) VALUES (?, ?, ?, ?, ?)', books)

# Add sample data to readers table
readers = [
    ('John Doe', 'john@example.com', '123-456-7890'),
    ('Jane Smith', 'jane@example.com', '098-765-4321')
]
cursor.executemany('INSERT INTO readers (name, email, phone) VALUES (?, ?, ?)', readers)

# Add sample data to loans table
loans = [
    (1, 1, '2023-01-01', '2023-01-15'),
    (2, 2, '2023-02-01', '2023-02-15')
]
cursor.executemany('INSERT INTO loans (book_id, reader_id, loan_date, return_date) VALUES (?, ?, ?, ?)', loans)

# Save changes and close the connection
conn.commit()
conn.close()

print("The database has been created and sample data has been added.")

# Created/Modified files during execution:
print("book.db")