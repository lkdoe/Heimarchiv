import sqlite3
from MediaClasses import Media

conn = sqlite3.connect('ProtoArchive.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS media(
   Title text,
   Author text,
   Director text,
   Year text,
   Category text,
   Genre text,
   Players integer,
   Age integer
)''')

# c.execute("DROP TABLE IF EXISTS media")
# Write new entries

m_1 = Media("Der Herr der Ringe")
m_1.set_attr('author', 'Tolkien')
m_1.category = "Book"
m_2 = Media("Die Kobolde")
m_2.category = "Book"
m_2.set_attr('author', 'Witzko')

# c.execute("INSERT INTO media VALUES (?, '', '', '', ?, '', 0, 0)",
#           (m_1.title, m_1.category))
# c.execute("INSERT INTO media VALUES (:Title, :Author, :Medium)",
#           {'Title': m_2.title, 'Author': m_2.author, 'Medium': m_2.category})
# c.execute("INSERT INTO media VALUES
#   ('Der Räuber Hotzenplotz', 'Ottfried Preußler', '', '', 'Book', 'Kinderbuch',0, 0)")
# c.execute('''
#    INSERT INTO media VALUES ('Frettchen zur See', 'Richard Bach',
#    '', '', 'Book', 'Kinderbuch', 0, 0)''')

def insertion(med):
    c.execute('''INSERT INTO media VALUES (?, '', '', '', ?, '', 0, 0)''',
              (med.title, med.category))

# insertion(m_2)
# Update entries

conn.commit()
# Delete entries

conn.commit()
# Retrieve entries
c.execute("SELECT * FROM media WHERE category='Book'")

print(c.fetchall())

# End retrieval and close the database

conn.close()
