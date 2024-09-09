import sqlite3

# Connect to the database
conn = sqlite3.connect('book.db')
cursor = conn.cursor()


# Create
def add_author(name, birth_year, country):
    cursor.execute("INSERT INTO authors (name, birth_year, country) VALUES (?, ?, ?)", (name, birth_year, country))
    conn.commit()
    print(f"\nAuthor '{name}' added.\n")


# Read
def get_all_authors():
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()

    print("\nList of Authors : ")
    for author in authors:
        print(f"ID : {author[0]}, Name : {author[1]}, Birth Year : {author[2]}, Country : {author[3]}")
    print("")

# Update
def update_author(author_id, name=None, birth_year=None, country=None):
    query = "UPDATE authors SET "
    params = []

    if name:
        query += "name = ?, "
        params.append(name)
    if birth_year:
        query += "birth_year = ?, "
        params.append(birth_year)
    if country:
        query += "country = ?, "
        params.append(country)

    query = query.rstrip(", ")
    query += " WHERE id = ?"
    params.append(author_id)

    cursor.execute(query, params)
    conn.commit()
    print(f"\nAuthor with ID {author_id} updated.")


# Delete
def delete_author(author_id):
    cursor.execute("DELETE FROM authors WHERE id = ?", (author_id,))
    conn.commit()
    print(f"\nAuthor with ID {author_id} deleted.")



# Main
while True:
    command = int(input("Create : 1, Read : 2, Update : 3, Delete : 4, Exit : 5   : "))

    if command == 1:
        name = input("name : ")
        birth_year = int(input("birth_year : "))
        country = input("country : ")
        add_author(name, birth_year, country)

    elif command == 2:
        get_all_authors()

    elif command == 3:
        id = int(input("input id : "))
        name = input("name : ").strip()
        birth_year = input("birth_year : ").strip()
        country = input("country : ").strip()

        name = name if name else None
        birth_year = int(birth_year) if birth_year else None
        country = country if country else None

        update_author(id, name, birth_year, country)
        get_all_authors()

    elif command == 4:
        id = int(input("input id : "))
        delete_author(id)
        get_all_authors()

    elif command == 5:
        break

    else:
        continue