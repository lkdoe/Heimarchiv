from tkinter import *
import sqlite3

root = Tk()
root.title('Heimarchiv')
root.geometry("400x400")

# Database

# Create a Database or connect to one
conn = sqlite3.connect('test_archive.db')

# Create cursor that can execute insertions, updates and retrievals
c = conn.cursor()

# Create table
c.execute(
    """CREATE TABLE IF NOT EXISTS media(
    title text,
    author text,
    category text,
    genre text,
    age integer
    )""")


# Submit function for database
def submit():
    conn = sqlite3.connect('test_archive.db')
    c = conn.cursor()

    # Insert into table
    c.execute("""INSERT INTO media VALUES 
            (:title, :author, :category, :genre, :age)""",
              {
                  'title': title.get(),
                  'author': author.get(),
                  'category': category.get(),
                  'genre': genre.get(),
                  'age': age.get()
              })
    conn.commit()
    conn.close()
    # Clear text boxes
    title.delete(0, END)
    author.delete(0,END)
    category.delete(0, END)
    genre.delete(0, END)
    age.delete(0, END)

# Text boxes
Label(root, text="").grid(row=0, column=0)  # Empty row
title = Entry(root, width=30)
title.grid(row=1, column=1, padx=20)
author = Entry(root, width=30)
author.grid(row=2, column=1)
category = Entry(root, width=30)
category.grid(row=3, column=1)
genre = Entry(root, width=30)
genre.grid(row=4, column=1)
age = Entry(root, width=30)
age.grid(row=5, column=1)

# Text box labels
title_label = Label(root, text="Title")
title_label.grid(row=1, column=0)
author_label = Label(root, text="Author")
author_label.grid(row=2, column=0)
category_label = Label(root, text="Category")
category_label.grid(row=3, column=0)
genre_label = Label(root, text="Genre")
genre_label.grid(row=4, column=0)
age_label = Label(root, text="Age")
age_label.grid(row=5, column=0)


# Submit button
submit_btn = Button(root, text="Add Entry to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
