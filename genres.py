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