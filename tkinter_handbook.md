# Tkinter

## Tk()
import tkinter as tk
root = tk.Tk()  # 메인 윈도우 생성
root.mainloop()  # 이벤트 루프 시작

## Label()
label = tk.Label(root, text="Hello, World!")
label.pack()  # 위젯 배치

## Button()
button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked!"))
button.pack()

## Entry
entry = tk.Entry(root)
entry.pack()


## Text
text_box = tk.Text(root, height=5, width=30)
text_box.pack()

## Frameframe = tk.Frame(root)
frame = tk.Frame(root)
frame.pack()

## Canvas
canvas = tk.Canvas(root, width=200, height=200)
canvas.create_line(0, 0, 200, 200)
canvas.pack()

## Listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.pack()

## Checkbutton
var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me", variable=var)
checkbox.pack()

## Radiobutton
var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
radiobutton1.pack()
radiobutton2.pack()

## Scale
scale = tk.Scale(root, from_=0, to=100)
scale.pack()

## Menu
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")

## Geometry 관리자
### 1. pack()
widget.pack()
---
**예시**
import tkinter as tk

root = tk.Tk()

# 위젯을 위에서 아래로 쌓는 방식
label1 = tk.Label(root, text="Label 1", bg="red")
label1.pack(side="top", fill="x")  # 위쪽에 수평으로 꽉 채움

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.pack(side="top", fill="x")  # 그 다음 위쪽에 배치

root.mainloop()

### 2. grid()
widget.grid(row=0, column=0)
---
**예시**
import tkinter as tk

root = tk.Tk()

# 행과 열로 위젯 배치
label1 = tk.Label(root, text="Label 1", bg="red")
label1.grid(row=0, column=0)  # (0, 0) 위치에 배치

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.grid(row=0, column=1)  # (0, 1) 위치에 배치

label3 = tk.Label(root, text="Label 3", bg="green")
label3.grid(row=1, column=0, columnspan=2, sticky="ew")  # 두 열에 걸쳐 수평 확장

root.mainloop()

### 3. place()
widget.place(x=100, y=50)
---
**예시**
import tkinter as tk

root = tk.Tk()

# 절대 좌표로 배치
label1 = tk.Label(root, text="Label 1", bg="red")
label1.place(x=50, y=50, width=100, height=50)  # (50, 50) 위치에 크기 100x50으로 배치

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.place(x=200, y=100, width=150, height=100)  # (200, 100) 위치에 크기 150x100으로 배치

root.mainloop()
