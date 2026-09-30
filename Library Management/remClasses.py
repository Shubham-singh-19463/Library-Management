# 4. Library Management System ⭐

# Classes:

# Book
# Member
# Library

# Features:

# Add books
# Register members
# Borrow book
# Return book
# Search books
# Track which member borrowed which book
# Prevent borrowing an already borrowed book

# This is excellent because objects need to interact with each other.

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.borrowed_status = False


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    

    def __init__(self):
        self.books = []
        self.members = []
        self.count_book_id = 1
        self.count_register_id = 1

    def register_member(self, name):
            self.members.append(Member(name, self.count_register_id))
            self.count_register_id += 1

    def display_members(self):
        print("Member_id, Name")
        for i in self.members:
            print(i.member_id, i.name)

    def Search_members(self, m_name):
        print("Member_id, name")
        for i in self.members:
            if m_name.lower() in i.name.lower():
                print(i.member_id, i.name)


    def add_books(self, title, author):
        self.books.append(Book(title, author, self.count_book_id))
        self.count_book_id += 1

    
    def display_books(self):
        print("book_id, title, author, borrowed_status")

        for i in self.books:
            print(i.book_id, i.title, i.author, i.borrowed_status)

    

    def Search_books(self, book_name):
        print("book_id, title, author, borrowed_status")
        for i in self.books:
            if book_name.lower() in i.title.lower():
                print(i.book_id, i.title, i.author, i.borrowed_status)

    def Borrow_books(self, memberid, book_id):
        book_to_borrow = None
        member_to_borrow = None
        borrow_status = "Failed!"
        for i in self.books:
            if book_id == i.book_id and i.borrowed_status == False:
                book_to_borrow = i
                break

        if book_to_borrow:
            for j in self.members:
                if memberid == j.member_id:
                    member_to_borrow = j
                    break

        if member_to_borrow:
            book_to_borrow.borrowed_status = True
            member_to_borrow.borrowed_books.append(book_to_borrow)
            borrow_status = "Success!!!"

        print(borrow_status)


    def return_books(self, memberid, book_id):
        status = "Failed"

        for member in self.members:
            if memberid == member.member_id:
    
                for book in self.books:
                    if book_id == book.book_id:

                        if book in member.borrowed_books:

                            book.borrowed_status = False
                            member.borrowed_books.remove(book)
                            status = "Success"
                            break
                break
    
        print(status)

            
