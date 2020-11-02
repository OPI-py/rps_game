from tkinter import Tk, Label, Button, messagebox
import random

win = Tk()
win.title("Камінь, Ножиці, Бумага")
win.resizable(0, 0)
win.iconbitmap('favicon.ico')

result = Label(win, text="Виберіть штучку", font=("Arial Black", 30),
               width=20, bg="#ffdba1", pady=20)
result.grid(row=0, column=0, columnspan=4, sticky="nsew")

def message1():
    messagebox.showinfo("Вітаємо", "    Ви виграли ;)    ")
    
def message2():
    messagebox.showinfo("Хехе", "       Нічия        ")
    
def message3():
    messagebox.showinfo("Жиш", "    Не повезло :)   ")

def scissors():
    ai_choice = random.randint(1, 3)
    
    if ai_choice == 1:
        return message2()
    elif ai_choice == 2:
        return message3()
    elif ai_choice == 3:
        return message1()
    else:
        return "Error"
b_scissors = Button(win, text="Ножиці", bg="#ff7171", width=20,
                    font=("Arial Black", 20), command=scissors)
b_scissors.grid(row=1, column=0, columnspan=1, sticky="nsew")

def stone():
    ai_choice = random.randint(1, 3)
    
    if ai_choice == 2:
        return message2()
    elif ai_choice == 3:
        return message3()
    elif ai_choice == 1:
        return message1()
    else:
        return "Error"

b_stone = Button(win, text="Камінь", bg="#3d3d3b", fg="White",
                 width=20, font=("Arial Black", 20), command=stone)
b_stone.grid(row=1, column=1, columnspan=1, sticky="nsew")

def paper():
    ai_choice = random.randint(1, 3)
    
    if ai_choice == 3:
        return message2()
    elif ai_choice == 1:
        return message3()
    elif ai_choice == 2:
        return message1()
    else:
        return "Error"

b_paper = Button(win, text="Бумага", bg="#ffffc9",
                 width=20, font=("Arial Black", 20), command=paper)
b_paper.grid(row=1, column=3, columnspan=1, sticky="nsew")

ex = Button(win, text="Вихід", width=20, font=("Arial Black", 20),
                                                command=win.destroy)
ex.grid(row=2, columnspan=4, sticky="nsew")


win.mainloop()