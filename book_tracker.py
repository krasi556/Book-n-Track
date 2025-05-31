titles = []      # List of book titles
authors = []     # List of book authors
statuses = []    # List of read statuses: "Read" or "Unread"

def add_book(title, author):
    titles.append(title) # Append the title to titles list
    authors.append(author)# Append the author to authors list
    statuses.append('Unread')# Append "Unread" to statuses list
    print('Book-ed!')# Print a message confirming the addition

def mark_as_read(title):
        if title in titles:
            index = titles.index(title)
            statuses[index] = 'Read'
        # Loop through the titles list
        # If the title is found, update the corresponding status to "Read"
        # Print confirmation or error if not

def mark_as_unread(title):
# Same logic as mark_as_read, but set status to "Unread"

def search_book(keyword):
    # Loop through the titles and authors
    # If keyword is found in title or author (case-insensitive), print book info
    # If no matches, print "No books found."

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