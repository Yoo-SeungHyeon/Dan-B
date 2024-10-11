import tkinter as tk
from tkinter import ttk
import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('example.db')
c = conn.cursor()

# 데이터베이스 테이블 생성 (만약 테이블이 없다면 생성)
c.execute('''CREATE TABLE IF NOT EXISTS vocabook (
    id INTEGER PRIMARY KEY,
    title TEXT,
    range INTEGER)''')
conn.commit()

# 단어장 등록 팝업창 함수
def open_register_popup():
    def register_vocabook():
        title = title_entry.get()
        range_value = range_entry.get()

        if title and range_value:
            try:
                range_value = int(range_value)
                c.execute("INSERT INTO vocabook (title, range) VALUES (?, ?)", (title, range_value))
                conn.commit()
                popup.destroy()
                show_data()  # 새로 등록된 데이터를 테이블에 반영
            except ValueError:
                error_label.config(text="범위는 숫자여야 합니다.")
        else:
            error_label.config(text="모든 필드를 입력해 주세요.")

    # 팝업창 생성
    popup = tk.Toplevel()
    popup.title("단어장 등록")

    # 제목 입력
    tk.Label(popup, text="단어장명").grid(row=0, column=0, padx=10, pady=10)
    title_entry = tk.Entry(popup)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    # 범위 입력
    tk.Label(popup, text="범위").grid(row=1, column=0, padx=10, pady=10)
    range_entry = tk.Entry(popup)
    range_entry.grid(row=1, column=1, padx=10, pady=10)

    # 등록 버튼
    register_button = tk.Button(popup, text="등록하기", command=register_vocabook)
    register_button.grid(row=2, column=0, columnspan=2, pady=10)

    # 에러 메시지 표시용 라벨
    error_label = tk.Label(popup, text="", fg="red")
    error_label.grid(row=3, column=0, columnspan=2)

# 데이터 표시 함수
def show_data():
    # 테이블에 있는 모든 항목 삭제
    for i in tree.get_children():
        tree.delete(i)

    # 데이터베이스에서 데이터 가져오기
    c.execute("SELECT * FROM vocabook")
    results = c.fetchall()

    # 데이터를 Treeview에 추가
    for row in results:
        tree.insert("", "end", values=row)

# tkinter GUI 생성
root = tk.Tk()
root.title("SQLite Vocabulary Book Viewer")

# Treeview 생성 (테이블 형태)
columns = ("ID", "단어장명", "범위")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("단어장명", text="단어장명")
tree.heading("범위", text="범위")

# Treeview 열 너비 설정
tree.column("ID", width=50, anchor="center")
tree.column("단어장명", width=200, anchor="w")
tree.column("범위", width=100, anchor="center")

tree.pack(pady=20)

# SQL 실행 버튼
show_button = tk.Button(root, text="Show Data", command=show_data)
show_button.pack(pady=10)

# 단어장 등록 버튼
register_button = tk.Button(root, text="단어장 등록", command=open_register_popup)
register_button.pack(pady=10)

# 메인 루프 실행
root.mainloop()

# 데이터베이스 연결 닫기
conn.close()
