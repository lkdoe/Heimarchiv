from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Heimarchiv')
root.geometry("500x500")

my_tree = ttk.Treeview(root)

# Define the columns
my_tree['columns'] = ("Title", "Category", "Author")

# Format the columns
my_tree.column("#0", width=120, minwidth=25)
my_tree.column("Title", anchor=W, width=120)
my_tree.column("Category", anchor=CENTER, width=80)
my_tree.column("Author", anchor=W, width=120)

# Headings for the columns
my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Title", text="Title", anchor=W)
my_tree.heading("Category", text="Category", anchor=W)
my_tree.heading("Author", text="Author", anchor=W)

# Add Data
my_tree.insert(
    parent='', index='end', iid=0, text="Parent", values=(
        "Game of Thrones", "Book", "G.R.R. Martin"))


my_tree.pack(pady=20)

root.mainloop()
