from tkinter import *
from tkinter.font import Font

root = Tk()
root.configure(background="#A020f0")
root.title('To-Do List Application')
root.geometry("750x500")

my_font = Font(family="Arial", size=22, weight="bold")
my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame, font=my_font, width=40, height=7, bg="#cf9fff", bd=0, fg="#5c4033", highlightthickness=0, selectbackground="#ff0000", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Arial", 22), width=26, bg='#cf9fff')
my_entry.pack(pady=20)

button_frame = Frame(root, bg='#a020f0')
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(my_list.curselection(), fg="#5c4033")
    my_list.selection_clear(0, END)

def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1

def delete_list():
    my_list.delete(0, END)

delete_button = Button(button_frame, text="Delete Item", command=delete_item, bg="#e7305b", font=("arial", 12, "bold"))
add_button = Button(button_frame, text="Add Item", command=add_item, bg="#e7305b", font=("arial", 12, "bold"))
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item, bg="#e7305b", font=("arial", 12, "bold"))
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item, bg="#e7305b", font=("arial", 12, "bold"))
delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed, bg="#e7305b", font=("arial",12, "bold"))

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()
