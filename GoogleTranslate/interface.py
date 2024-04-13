
from tkinter import *
from PIL import Image, ImageTk  # chèn ảnh
from googletrans import Translator  # dịch

# Tạo phụ tùng trước nền
root = Tk()
root.title("Google Galaxy")
root.geometry("500x630")
root.iconbitmap("logo.ico")

# Mở ảnh và gán cho biến load
load = Image.open("background.png")
render = ImageTk.PhotoImage(load)

# Hiển thị hình ảnh
img = Label(root, image=render)
img.place(x=0, y=0)

# Thiết lập font cho nhãn "Translate"
name = Label(root, text="Translate", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)  # cách top 10 đơn vị x,y

box = Text(root, width=28, height=8, font=("Roboto", 16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)  # Nút sẽ dưới box đầu tiên


def clear():
    box.delete(1.0, END)  # trong thằng này bắt đầu từ 1.0
    box1.debug(1.0, END)


def translate():
    INPUT = box.get(1.0, END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT,src="vi",dest="en")
    b = a.text
    box1.insert(END,b)
clear_button = Button(
    button_frame,
    text="Clear text",
    font=("Arial", 10, "bold"),
    bg="#303030",
    fg="#FFFFFF",
    command=clear,
)
clear_button.place(x=150, y=310)
trans_button = Button(
    button_frame,
    text="Translate",
    font=("Arial", 10, "bold"),
    bg="#303030",
    fg="#FFFFFF",
    command=translate,
)
trans_button.place(x=290, y=310)

box1 = Text(root, width=28, height=8, font=("Roboto", 16))
box1.pack(pady=50)
root.mainloop()