import sqlite3

conn = sqlite3.connect('book.db')
cursor = conn.cursor()

def update_genre(existing_name, new_name):
    cursor.execute("UPDATE genres SET name = ? WHERE name = ?", (new_name, existing_name))
    if cursor.rowcount > 0:
        print(f"'{existing_name}' 장르가 '{new_name}'으로 수정되었습니다.")
    else:
        print(f"'{existing_name}' 장르를 찾을 수 없습니다.")
    conn.commit()
    show_genre_list()

def add_genre(new_name):
    try:
        cursor.execute("INSERT INTO genres (name) VALUES (?)", (new_name,))
        print(f"'{new_name}' 장르가 추가되었습니다.")
    except sqlite3.IntegrityError:
        print(f"'{new_name}' 장르는 이미 존재합니다.")
    conn.commit()
    show_genre_list()

def delete_genre(id, name):
    cursor.execute("DELETE FROM genres WHERE id = ? AND name = ?", (id, name))
    if cursor.rowcount > 0:
        print(f"ID {id} 및 이름 '{name}'의 장르가 삭제되었습니다.")
    else:
        print(f"ID {id} 및 이름 '{name}'의 장르를 찾을 수 없습니다.")
    conn.commit()
    show_genre_list()

def show_genre_list():
    cursor.execute("SELECT id, name FROM genres")
    genres = cursor.fetchall()
    print("\n현재 장르 목록:")
    for genre in genres:
        print(f"ID: {genre[0]}, Name: {genre[1]}")
    print()

def get_genre_id_by_name(name):
    cursor.execute("SELECT id FROM genres WHERE name = ?", (name,))
    result = cursor.fetchone()
    return result[0] if result else None

def main():
    action = input("장르를 수정하려면 '수정', 추가하려면 '추가', 삭제하려면 '삭제'를 입력하세요: ").strip()
    
    if action == "수정":
        existing_name = input("수정할 장르 이름을 입력하세요: ").strip()
        new_name = input("새 장르 이름을 입력하세요: ").strip()
        update_genre(existing_name, new_name)
    elif action == "추가":
        new_name = input("추가할 장르 이름을 입력하세요: ").strip()
        add_genre(new_name)
    elif action == "삭제":
        name = input("삭제할 장르 이름을 입력하세요: ").strip()
        genre_id = get_genre_id_by_name(name)
        if genre_id:
            delete_genre(genre_id, name)
        else:
            print(f"'{name}' 장르를 찾을 수 없습니다.")
    else:
        print("잘못된 입력입니다. '수정', '추가', 또는 '삭제'를 입력하세요.")

    conn.close()

if __name__ == "__main__":
    main()