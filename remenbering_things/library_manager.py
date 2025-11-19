"""
Gestionnaire de Bibliothèque - Niveau intermédiaire
    Manipuler des listes de dictionnaires
    Utiliser des sets pour les genres
    Créer des compréhensions pour filtrer et transformer
"""

def add_save_book(name, author, genre, year):
    add_to_dico = {
        "name": name,
        "author": author,
        "genre": genre,
        "year": year
    }
    with open("library.txt", "a") as file:
        file.write(str(add_to_dico) + "\n")
    print("The book has been saved.")



def list_books():
    with open("library.txt", "r") as file:
        books = file.readlines()
    for book in books:
        print(book.strip())


def borrow_book(name):
    
    borrow_list = []
    with open("borrow_list.txt", 'r') as b_file:
        borrow_lines = b_file.readlines()
        b_list = []
        for line in borrow_lines: 
            b = line.strip()
            b_list.append(b)

    if b_list.count("['" + name + "']") > 0:
        print("This book is already borrowed.")
    else:
        print("You've borrowed a book :", name)
        borrow_list.append(name)

    with open("borrow_list.txt", 'a') as b_file:
        b_file.write(str(borrow_list) + "\n")
    
def give_back_book(name):
    with open("borrow_list.txt", 'r') as b_file:
        borrow_lines = b_file.readlines()
        for line in borrow_lines:
            b = line.strip()
            if b == "['" + name + "']":
                borrow_lines.remove(line)
                break

def check_library_info():
    with open("library.txt", "r") as file:
        books = file.readlines()
    total_books = len(books)
    
    print("Total number of books in the library:", total_books)

    with open("borrow_list.txt", "r") as b_file:
        borrow_lines = b_file.readlines()
    borrowed_books = sum(1 for line in borrow_lines if line.strip() != "[]")

    print("Number of borrowed books:", borrowed_books) 
print(
    "1- Search book(s) by name or author or genre or year\n"
    "2- Add book(s)\n"
    "3- Borrow book(s)\n"
    "4- Give back book(s)\n"
    "5- List book(s)\n"
    "6- Check library info\n"
    "7- Delete book(s)\n"
)

option = int(input("Choose a number of what you want : "))

if option == 2:
    name = input("Enter the book name : ")
    author = input("Enter the book author : ")
    genre = input("Enter the book genre : ")
    year = input("Enter the book year : ")
    add_save_book(name, author, genre, year)

elif option == 5:
    list_books()

elif option == 3:
    list_books()
    name = input("Enter the book name you want to borrow : ")
    borrow_book(name)

elif option == 4:
    list_books()
    name = input("Enter the book name you want to give back : ")
    print("You've given back the book :", name)
    give_back_book(name)
elif option == 6:
    check_library_info()
elif option == 1:
    criterion = input("Search by name, author, genre, or year: ").strip().lower()
    value = input(f"Enter the {criterion} to search for: ").strip().lower()

    with open("library.txt", "r") as file:
        books = file.readlines()

    matching_books = []
    for book in books:
        book_dict = eval(book.strip())
        if criterion in book_dict and str(book_dict[criterion]).lower() == value:
            matching_books.append(book_dict)

    if matching_books:
        print("Matching books found:")
        for book in matching_books:
            print(book)
    else:
        print("No matching books found.")

elif option == 7:
    name = input("Enter the book name you want to delete : ")
    with open("library.txt", "r") as file:
        books = file.readlines()
    with open("library.txt", "w") as file:
        for book in books:
            book_dict = eval(book.strip())
            if book_dict["name"] != name:
                file.write(str(book_dict) + "\n")
    print(f"The book '{name}' has been deleted from the library.")