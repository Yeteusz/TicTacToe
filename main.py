import tkinter as tk
from tkinter import Menu, messagebox
from tkinter.constants import DISABLED
okno = tk.Tk()  

# X Zaczyna
clicked = True
count = 0

# wyłącznie wszystkich guzików
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# sprawdzanie kto wygral
def checkifwon():
    global winner
    winner = False
    
    # sprawdzanie wygranej X w poziomie
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")                                                  # pierwszy poziom
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")                                                  # drugi poziom
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")                                                  # trzeci poziom
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()

    # sprawdzanie wygranej X w pionie
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")                                                  # pierwszy pion
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")                                                  # drugi pion
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")                                                  # trzeci pion
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()

    # sprawdzenie wygranej X po ukosie
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")                                                  # pierwszy ukos
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")                                                  # drugi ukos
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","X Wygrywa \nGratulacje!!")
        disable_all_buttons()

#########################################################################################################

    # sprawdzanie wygranej O w poziomie
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")                                                  # pierwszy poziom
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")                                                  # drugi poziom
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")                                                  # trzeci poziom
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()

    # sprawdzanie wygranej O w pionie
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")                                                  # pierwszy pion
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")                                                  # drugi pion
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")                                                  # trzeci pion
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()

    # sprawdzenie wygranej O po ukosie
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")                                                  # pierwszy ukos
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")                                                  # drugi ukos
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","O Wygrywa \nGratulacje!!")
        disable_all_buttons()

# sprawdz czy jest remis
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "REMIS!!!")
        disable_all_buttons()


# wciskanie guzika
def b_click(b):
    global clicked, count
    b.config(fg="green")
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "to miejsce juz jest zaznaczone!")

# funkcja reset game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    # guziki
    b1 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1) )
    b2 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2) )  #pierwszy wers
    b3 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3) )

    b4 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4) )
    b5 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5) )  #drugi wers
    b6 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6) )

    b7 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7) )
    b8 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8) )  #trzeci wers
    b9 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9) )
        
    # umiejscowienie guzikow
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)   # pierwszy wers
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)   # drugi wers
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)   # trzeci wers
    b9.grid(row=2, column=2)


# guziki
b1 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1) )
b2 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2) )  #pierwszy wers
b3 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3) )

b4 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4) )
b5 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5) )  #drugi wers
b6 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6) )

b7 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7) )
b8 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8) )  #trzeci wers
b9 = tk.Button(okno, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9) )
        
# umiejscowienie guzikow
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)   # pierwszy wers
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)   # drugi wers
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)   # trzeci wers
b9.grid(row=2, column=2)

# tworzenie menu
my_menu = Menu(okno)
okno.config(menu=my_menu)

# tworzenie opcji w menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
reset()

okno.title("Tic Tac Toe")
okno.geometry("315x350")
okno.resizable(False,False)
okno.mainloop()
