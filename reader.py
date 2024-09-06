import sqlite3

# Function to connect to the database
def connect_db():
    return sqlite3.connect('book.db')

# CREATE - Add a new reader
def add_reader(name, email, phone):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO readers (name, email, phone) VALUES (?, ?, ?)",
                   (name, email, phone))
    conn.commit()
    print(f"Added reader: {name}")
    conn.close()

# READ - Read all readers
def get_all_readers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM readers")
    readers = cursor.fetchall()
    conn.close()
    return readers

# READ - Find reader by name
def find_reader_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM readers WHERE name LIKE ?", ('%' + name + '%',))
    readers = cursor.fetchall()
    conn.close()
    return readers

# UPDATE - Update reader information
def update_reader(reader_id, name, email, phone):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE readers SET name=?, email=?, phone=? WHERE id=?",
                   (name, email, phone, reader_id))
    conn.commit()
    print(f"Updated reader with ID: {reader_id}")
    conn.close()

# DELETE - Delete a reader
def delete_reader(reader_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM readers WHERE id=?", (reader_id,))
    conn.commit()
    print(f"Deleted reader with ID: {reader_id}")
    conn.close()

# # Main function to test the features
# def main():
#     # Add a new reader
#     add_reader("Alice Johnson", "alice@example.com", "123-456-7890")
    
#     # Display all readers
#     print("\nAll readers:")
#     for reader in get_all_readers():
#         print(reader)
    
#     # Find reader by name
#     print("\nFind reader with name 'Alice':")
#     for reader in find_reader_by_name("Alice"):
#         print(reader)
    
#     # Update reader information
#     update_reader(3, "Alice J. Smith", "alicesmith@example.com", "098-765-4321")
    
#     # Delete reader
#     delete_reader(3)
    
#     # Display all readers again after update and delete
#     print("\nReaders list after update and delete:")
#     for reader in get_all_readers():
#         print(reader)

# if __name__ == "__main__":
#     main()

# print("CRUD operations have been performed for the readers table.")

# # Created/Modified files during execution:
# print("book.db")