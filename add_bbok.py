import sqlite3

# Connect to the database
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

# Check if the author "Ernest Hemingway" exists, if not, add it
cursor.execute("SELECT id FROM authors WHERE name = 'Ernest Hemingway'")
author_id = cursor.fetchone()
if not author_id:
    cursor.execute("INSERT INTO authors (name, birth_year, country) VALUES ('Ernest Hemingway', 1899, 'USA')")
    author_id = cursor.lastrowid
else:
    author_id = author_id[0]

# Check if the genre "Literature" exists, if not, add it
cursor.execute("SELECT id FROM genres WHERE name = 'Literature'")
genre_id = cursor.fetchone()
if not genre_id:
    cursor.execute("INSERT INTO genres (name) VALUES ('Literature')")
    genre_id = cursor.lastrowid
else:
    genre_id = genre_id[0]

# Define the new book data
new_book = ('The Old Man and the Sea', author_id, genre_id, 1952, '978-0684801223')

# Insert the new book into the books table
cursor.execute('''
INSERT INTO books (title, author_id, genre_id, year, isbn)
VALUES (?, ?, ?, ?, ?)
''', new_book)

# Commit changes and close the connection
conn.commit()
conn.close()

print("The book 'The Old Man and the Sea' has been added to the database.")
