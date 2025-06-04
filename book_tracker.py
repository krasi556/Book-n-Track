titles = ['Lord of the rings','Harry Potter']
authors = ['j.r.r. tolkien', 'J. K. Rowling']
statuses = ['unread','read']

is_found = False


def add_book(title, author):
    titles.append(title)
    authors.append(author)
    statuses.append('Unread')
    print('Book-ed!')
def mark_as_read(title):
        if title in titles:
            index = titles.index(title)
            statuses[index] = 'Read'
            
        else:
            print('Title not found')

def mark_as_unread(title):
    if title in titles:
        index = titles.index(title)
        statuses[index] = 'Unread'
    else:
        print('Title not found')

def search_book(keyword):
    is_found = False
    for index, i in enumerate(titles):
        if keyword.lower() in i.lower() or keyword.lower() in authors[index].lower():
            is_found = True
            break
    if is_found:
        print(f'Title: {i}')
        print(f'Author: {authors[index]}')
        print(f'Status: {statuses[index]}')
    else:
        print('Nothing found')
def list_books():
    # Loop through all books
    # Print each title, author, and status with numbering

def suggest_book():
    # Find all books where status is "Unread"
    # If at least one unread book exists, pick one at random and suggest it
    # If all books are read, print "No unread books left."

def delete_book(title):
    # Loop through titles
    # If match found, remove the title, author, and status at the same index
    # Print confirmation or "Book not found."

def main():
    print("📚 Welcome to the Digital Book Collection Manager 📚\n")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new book")
        print("2. Mark a book as read")
        print("3. Mark a book as unread")
        print("4. Search for a book")
        print("5. List all books")
        print("6. Suggest a book to read")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            add_book(title, author)

        elif choice == '2':
            title = input("Enter the title of the book to mark as read: ")
            mark_as_read(title)

        elif choice == '3':
            title = input("Enter the title of the book to mark as unread: ")
            mark_as_unread(title)

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            search_book(keyword)

        elif choice == '5':
            list_books()

        elif choice == '6':
            suggest_book()

        elif choice == '7':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)

        elif choice == '8':
            print("Goodbye! Happy reading! 📖")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 8.")

if __name__ == "__main__":
    main()