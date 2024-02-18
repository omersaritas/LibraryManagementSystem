class Library:
    #a+ dosya açılması
    def __init__(self):
        self.file = open("book_list.txt", "a+")    
    #a+ kapatma
        def __del__(self):
         self.file.close()
    
    #kitapları listeleme
    def list_books(self):
        self.file.seek(0)
        book_list = self.file.read().splitlines()
        for book in book_list:
            bookData = book.split(",")
            b_name, author = bookData[0],bookData[1]
            print(f"Book Name: {b_name}, Author: {author}")
    
    #kitap ekleme
    def add_book(self):
        b_name = input("Enter the book name: ")
        author = input("Enter the book's author: ")
        year = input("Enter the release year: ")
        page = input("Enter number of pages: ")
        self.file.seek(0)
        self.file.write(f"{b_name},{author},{year},{page}\n")
        print(f"The book that you wanted to add has been added successfully! '{b_name}' ")

    #kitap çıkarma
    def remove_book(self):
        b_name_to_remove = input("Enter the book name for to remove: ")
        self.file.seek(0) 
        book_list = self.file.read().splitlines()
        updated_books = []
        for book in book_list:
            if b_name_to_remove not in book:
                updated_books.append(book)
        self.file.seek(0) 
        self.file.truncate()
        for book in updated_books:
            self.file.write(f"{book}\n")
        print(f"Book that you have choosen has been removed from library: '{b_name_to_remove}' ")

    #Programı kapatma
    def close_LMS(self):
        q = exit()

#Menü oluşturma
lib = Library()

while True:
    print("--------MENU--------")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    print("--------------------")

    choice = input("What is your choice? Write it here --> ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q':
        lib.close_LMS()
    else:
        print("Invalid choice. Please try again.")
