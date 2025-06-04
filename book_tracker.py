titles = ['Lord of the rings', 'Harry Potter', 'The Witcher']  # List of book titles
authors = ['J.R.R. Tolkien', 'J. K. Rowling', 'Andrzej Sapkowski']  # List of book authors
statuses = ['unread', 'read', 'unread']  # List of read statuses: "Read" or "Unread"

import random


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
		print(f'{statuses[index]}')


def list_books():
	for i in range(len(titles)):
		print(f'\n{i + 1}. Titles: {titles[i]}')
		print(f'Author: {authors[i]}')
		print(f'Status: {statuses[i]}')
		print()


def suggest_book():
	is_found = False
	books_unread = []
	for index, i in enumerate(statuses):
		if 'unread' in i.lower():
			books_unread.append(titles[index])
		else:
			is_found = True
	if not is_found:
		print('No unread books left')
	else:
		selected_book = random.choice(books_unread)
		selected_index = titles.index(selected_book)
		selected_author = authors[selected_index]
		print(f'{selected_book},\n by\n  {selected_author}')


def delete_book(title):
	for index, i in enumerate(titles):
		if title.lower() == i.lower():
			print(f'{titles[index]} cleared !')
			authors.pop(index)
			statuses.pop(index)
			titles.pop(index)
			break
	else:
		print('Book not found')


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