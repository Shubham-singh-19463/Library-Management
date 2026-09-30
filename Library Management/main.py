import remClasses as myprogram


def help_menu():
    l = ["Help Menu", "Add Books", "Display All Books", "Search Book", "Register Member", "Show Member", "Search Member", "Borrow Book", "Return Book","Exit"]
    print("=========================")
    for index, value in enumerate(l):
        print(index+1, ". ", value.strip())
    print("=========================")

help_menu()

Central_library = myprogram.Library()

while True:
    try:
        choose = int(input("please choose a choice: "))
        print("=========================")


        match (choose):
            case 1:
                help_menu()

            case 2:
                print("========================= Adding book in library =========================")
                print("To quit without adding books just hit enter two times or leave name and author blank")
                title = input("Please enter book name: ")
                author = input("Please enter book author name: ")
                if title and author:
                    Central_library.add_books(title, author)
                    print("book added succesfully!!!\n")

            case 3:
                print("========================= Displaying all books in library =========================")
                Central_library.display_books()

            case 4:
                print("========================= Searching books in library =========================")
                title = input("Please enter book name: ")
                if title:
                    print("Search Results")
                    Central_library.Search_books(title)
                else:
                    print("Name should not be empty!!!")

            case 5:
                print("========================= Registering Member in library =========================")
                print("To quit without adding members just hit enter or leave name empty")
                name = input("Please enter your name: ")
                                
                if name:
                    Central_library.register_member(name)
                    print("Member registered succesfully!!!\n")

            case 6:
                print("========================= Displaying all Members in library =========================")
                Central_library.display_members()

            case 7:
                print("========================= Searching Members in library =========================")
                name = input("Please enter member name: ")
                if name:
                    print("Search Results")
                    Central_library.Search_members(name)
                else:
                    print("Name should not be empty!!!")

            case 8:
                print("========================= Borrow Book for Member in library =========================")
                mem_id = int(input("enter member id: "))
                book_id = int(input("enter book id: "))
                Central_library.Borrow_books(mem_id, book_id)

            case 9:
                print("========================= Return Book for Member in library =========================")
                mem_id = int(input("enter member id: "))
                book_id = int(input("enter book id: "))
                Central_library.return_books(mem_id, book_id)
            case 10:
                print("Thank you for using this software!!!")
                break

    except Exception:
        print("Invalid input!!")