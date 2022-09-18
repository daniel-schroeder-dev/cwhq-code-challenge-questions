def display_books(library):
    print()
    print("Current Library Books:")
    print()
    print("#" * 20)
    for title, author in library.items():
        print()
        print(f"Title: {title}")
        print(f"Author: {author}")
        print()

    print("#" * 20)


library = {}
options = """
    Welcome to the Library!

    1.) Add a book
    2.) Update a book
    3.) Remove a book
    4.) Exit
"""

while True:
    display_books(library)
    user_choice = int(input(options))

    if user_choice == 1 or user_choice == 2:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library[title] = author 
    elif user_choice == 3:
        title_to_remove = input("Enter book title to remove: ") 
        author = library.pop(title_to_remove)
        print(f"Removed {title_to_remove} by {author}")
    elif user_choice == 4:
        print("Goodbye!")
        break



