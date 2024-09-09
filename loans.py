import sqlite3
from datetime import datetime, timedelta

# Function to connect to the database
def connect_db():
    return sqlite3.connect('book.db')

# CREATE - Add a new loan record
def add_loan(book_id, reader_id, loan_date=None, return_date=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if loan_date is None:
        loan_date = datetime.now().strftime('%Y-%m-%d')
    if return_date is None:
        return_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    
    cursor.execute("INSERT INTO loans (book_id, reader_id, loan_date, return_date) VALUES (?, ?, ?, ?)",
                   (book_id, reader_id, loan_date, return_date))
    loan_id = cursor.lastrowid
    conn.commit()
    print(f"Added loan record: ID {loan_id}")
    conn.close()
    return loan_id

# READ - Read all loan records
def get_all_loans():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loans")
    loans = cursor.fetchall()
    conn.close()
    return loans

# READ - Find loan records by reader ID
def find_loans_by_reader(reader_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM loans WHERE reader_id = ?", (reader_id,))
    loans = cursor.fetchall()
    conn.close()
    return loans

# UPDATE - Update loan information
def update_loan(loan_id, book_id, reader_id, loan_date, return_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE loans SET book_id=?, reader_id=?, loan_date=?, return_date=? WHERE id=?",
                   (book_id, reader_id, loan_date, return_date, loan_id))
    conn.commit()
    print(f"Updated loan record with ID: {loan_id}")
    conn.close()

# DELETE - Delete a loan record
def delete_loan(loan_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM loans WHERE id=?", (loan_id,))
    conn.commit()
    print(f"Deleted loan record with ID: {loan_id}")
    conn.close()

# Main function to test the features
# def main():
#     # Add a new loan record
#     new_loan_id = add_loan(1, 1)  # Assume book_id=1 and reader_id=1
    
#     # Read all loan records
#     print("\nAll loan records:")
#     for loan in get_all_loans():
#         print(loan)
    
#     # Find loan records by reader ID
#     print("\nLoan records for reader with ID 1:")
#     for loan in find_loans_by_reader(1):
#         print(loan)
    
#     # Update a loan record
#     update_loan(new_loan_id, 1, 1, '2023-01-01', '2023-01-15')
    
#     # Delete a loan record
#     delete_loan(new_loan_id)
    
#     # Check again after updating and deleting
#     print("\nLoan records after update and delete:")
#     for loan in get_all_loans():
#         print(loan)

# if __name__ == "__main__":
#     main()

# print("CRUD operations for the loans table have been performed.")

# # Created/Modified files during execution:
# print("book.db")