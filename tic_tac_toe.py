from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

clicked = True
count = 0
def disable_all_btns():
    for i in range(1,10):
        eval("b"+str(i)+".config(state  = DISABLED)")



def checkifwon():
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        winner = True
        b1["bg"] = "green"
        b2["bg"] = "green"
        b3["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        winner = True
        b4["bg"] = "green"
        b5["bg"] = "green"
        b6["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        winner = True
        b7["bg"] = "green"
        b8["bg"] = "green"
        b9["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        winner = True
        b1["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        winner = True
        b3["bg"] = "green"
        b5["bg"] = "green"
        b7["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        winner = True
        b1["bg"] = "green"
        b4["bg"] = "green"
        b7["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        winner = True
        b2["bg"] = "green"
        b5["bg"] = "green"
        b8["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()
    
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        winner = True
        b3["bg"] = "green"
        b6["bg"] = "green"
        b9["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","X wins!")
        disable_all_btns()


    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        winner = True
        b1["bg"] = "green"
        b2["bg"] = "green"
        b3["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()


    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        winner = True
        b4["bg"] = "green"
        b5["bg"] = "green"
        b6["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()


    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        winner = True
        b7["bg"] = "green"
        b8["bg"] = "green"
        b9["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()


    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        winner = True
        b1["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()


    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        winner = True
        b3["bg"] = "green"
        b5["bg"] = "green"
        b7["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()


    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        winner = True
        b1["bg"] = "green"
        b4["bg"] = "green"
        b7["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()


    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        winner = True
        b2["bg"] = "green"
        b5["bg"] = "green"
        b8["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()

    
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        winner = True
        b3["bg"] = "green"
        b6["bg"] = "green"
        b9["bg"] = "green"
        messagebox.showinfo("Tic Tac Toe","O wins!")
        disable_all_btns()



def reset():
    global clicked,count
    for i in range(1,10):
        eval("b"+str(i)+".config(text = \" \",state  = NORMAL,bg = \"SystemButtonFace\")")
    clicked = True
    count = 0


def buttonClicked(button):
    global clicked,count
    if clicked and button["text"] == " ":
        button["text"] = "X"
        clicked = False
    elif clicked == False and button["text"] == " ":
        button["text"] = "O"
        clicked = True
    else:
        messagebox.showerror("Tic Tac Toe","Hey ! \n You clicked it already")
    count+=1
    checkifwon()
    if count == 9:
        messagebox.showinfo("Tic Tac Toe","Draw!")
        disable_all_btns()


b1 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b1))
b2 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b2))
b3 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b3))

b4 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b4))
b5 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b5))
b6 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b6))

b7 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b7))
b8 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b8))
b9 = Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg = "SystemButtonFace",command= lambda: buttonClicked(b9))


my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label = "Menu",menu=options_menu)
options_menu.add_command(label="Reset",command=reset)

k = 1
for i in range(1,4):
    for j in range(3):
        eval("b"+str(k)+".grid(row = "+ str(i-1)+",column = "+str(j)+")")
        k+=1


root.mainloop()