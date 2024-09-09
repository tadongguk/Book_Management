import sqlite3

# 데이터베이스 연결 및 커서 생성
conn = sqlite3.connect('book.db')
cursor = conn.cursor()

def update_book(book_id, new_title=None, new_author_id=None, new_genre_id=None, new_year=None, new_isbn=None):
    update_fields = []
    params = []
    
    if new_title:
        update_fields.append("title = ?")
        params.append(new_title)
    if new_author_id:
        update_fields.append("author_id = ?")
        params.append(new_author_id)
    if new_genre_id:
        update_fields.append("genre_id = ?")
        params.append(new_genre_id)
    if new_year:
        update_fields.append("year = ?")
        params.append(new_year)
    if new_isbn:
        update_fields.append("isbn = ?")
        params.append(new_isbn)
    
    if update_fields:
        params.append(book_id)
        cursor.execute(f"UPDATE books SET {', '.join(update_fields)} WHERE id = ?", params)
        if cursor.rowcount > 0:
            print(f"ID {book_id} 책이 수정되었습니다.")
        else:
            print(f"ID {book_id} 책을 찾을 수 없습니다.")
    else:
        print("수정할 정보가 없습니다.")
    
    conn.commit()
    show_book_list()

def add_book(title, author_id, genre_id, year, isbn):
    try:
        cursor.execute("INSERT INTO books (title, author_id, genre_id, year, isbn) VALUES (?, ?, ?, ?, ?)", 
                       (title, author_id, genre_id, year, isbn))
        print(f"'{title}' 책이 추가되었습니다.")
    except sqlite3.IntegrityError as e:
        print(f"책을 추가하는 데 오류가 발생했습니다: {e}")
    
    conn.commit()
    show_book_list()

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    if cursor.rowcount > 0:
        print(f"ID {book_id} 책이 삭제되었습니다.")
    else:
        print(f"ID {book_id} 책을 찾을 수 없습니다.")
    
    conn.commit()
    show_book_list()

def show_book_list():
    cursor.execute("SELECT b.id, b.title, a.name, g.name, b.year, b.isbn FROM books b " +
                   "LEFT JOIN authors a ON b.author_id = a.id " +
                   "LEFT JOIN genres g ON b.genre_id = g.id")
    books = cursor.fetchall()
    print("\n현재 책 목록:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}, ISBN: {book[5]}")
    print()

def main():
    action = input("책을 수정하려면 '수정', 추가하려면 '추가', 삭제하려면 '삭제'를 입력하세요: ").strip()
    
    if action == "수정":
        book_id = int(input("수정할 책의 ID를 입력하세요: ").strip())
        new_title = input("새 책 제목을 입력하세요 (수정하지 않으려면 빈칸으로 두세요): ").strip() or None
        new_author_id = input("새 저자 ID를 입력하세요 (수정하지 않으려면 빈칸으로 두세요): ").strip() or None
        new_genre_id = input("새 장르 ID를 입력하세요 (수정하지 않으려면 빈칸으로 두세요): ").strip() or None
        new_year = input("새 출판 연도를 입력하세요 (수정하지 않으려면 빈칸으로 두세요): ").strip() or None
        new_isbn = input("새 ISBN을 입력하세요 (수정하지 않으려면 빈칸으로 두세요): ").strip() or None
        
        # 입력된 ID 값들이 실제 숫자인지 확인
        if new_author_id: new_author_id = int(new_author_id)
        if new_genre_id: new_genre_id = int(new_genre_id)
        if new_year: new_year = int(new_year)
        
        update_book(book_id, new_title, new_author_id, new_genre_id, new_year, new_isbn)
    
    elif action == "추가":
        title = input("추가할 책 제목을 입력하세요: ").strip()
        author_id = int(input("저자 ID를 입력하세요: ").strip())
        genre_id = int(input("장르 ID를 입력하세요: ").strip())
        year = int(input("출판 연도를 입력하세요: ").strip())
        isbn = input("ISBN을 입력하세요: ").strip()
        
        add_book(title, author_id, genre_id, year, isbn)
    
    elif action == "삭제":
        book_id = int(input("삭제할 책의 ID를 입력하세요: ").strip())
        delete_book(book_id)
    
    else:
        print("잘못된 입력입니다. '수정', '추가', 또는 '삭제'를 입력하세요.")

    conn.close()

if __name__ == "__main__":
    main()
