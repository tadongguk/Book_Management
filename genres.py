import sqlite3

conn = sqlite3.connect('book.db')  # 데이터베이스 파일 이름
cursor = conn.cursor()

cursor.execute("SELECT * FROM books")

books = []

genres = [
    "소설 (Fiction)", "비소설 (Non-Fiction)", "아동문학 (Children's Literature)", 
    "시 (Poetry)", "공포 (Horror)", "판타지 (Fantasy)", "SF (Science Fiction)", 
    "미스터리/추리 (Mystery/Detective)", "역사 (Historical)", "자기계발 (Self-help)", 
    "교육 (Educational)", "경제/경영 (Business/Economics)", "과학 (Science)", 
    "기술 (Technology)", "철학/종교 (Philosophy/Religion)", "예술 (Art)", 
    "요리 (Cooking)", "여행 (Travel)", "건강/의학 (Health/Medical)", 
    "스포츠 (Sports)"
]

def add_book():
    title = input("책 제목을 입력하세요: ")
    author = input("저자를 입력하세요: ")
    year = input("출판 연도를 입력하세요: ")
    publisher = input("출판사를 입력하세요: ")
    genres = input("장르를 입력하세요: ")

print("\n--- 장르 목록 ---")
for i, genre in enumerate(genres, 1):
    print(f"{i}. {genre}")
    
genre_choice = int(input("\n장르 번호를 선택하세요: ")) - 1
selected_genre = genres[genre_choice]

book = {
    "제목": title,
    "저자": author,
    "출판 연도": year,
    "출판사": publisher,
    "장르": selected_genre
    }

books.append(book)
print(f"|n'{title} 책이 추가되었습니다.|n")