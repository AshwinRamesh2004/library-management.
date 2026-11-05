import mysql.connector
conn = mysql.connector.connect(
    host="localhost", user="root", password="Ashwin@123", database="library_db"
)
cur = conn.cursor()


def create_book():
    title = input("Title: ")
    author = input("Author: ")
    copies = int(input("Copies: "))
    cur.execute(
        "INSERT INTO books (title, author, total_copies, available_copies) VALUES (%s,%s,%s,%s)",
        (title, author, copies, copies),
    )
    conn.commit()
    print("Book added")



def read_books():
    cur.execute("SELECT book_id, title, author, available_copies FROM books")
    for row in cur.fetchall():
        print(row)


def update_book():
    book_id = input("Book ID to update: ")
    title = input("New title: ")
    author = input("New author: ")
    cur.execute(
        "UPDATE books SET title=%s, author=%s WHERE book_id=%s",
        (title, author, book_id),
    )
    conn.commit()
    print("Book updated")

def delete_book():
    book_id = input("Book ID to delete: ")
    cur.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
    conn.commit()
    print("Book deleted")


while True:
    print("\n1.Create  2.Read  3.Update  4.Delete  0.Exit")
    choice = input("Choice: ")
    if choice == "1":
        create_book()
    elif choice == "2":
        read_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "0":
        break
    else:
        print("Wrong choice")

conn.close()