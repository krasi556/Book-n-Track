titles = ['Lord of the rings', 'Harry Potter', 'The Witcher','World of Warcaft']
authors = ['J.R.R. Tolkien', 'J. K. Rowling', 'Andrzej Sapkowski','William King']
statuses = ['unread', 'read', 'unread','Read']
import random
import os

def add_book(title, author):
	for i in titles:
		if i.lower() == title.lower():
			print(f'The title "{title}" already exists!')
			return
	titles.append(title)
	authors.append(author)
	statuses.append('unread')
	print('Book-ed!')

def mark_as_read(title):
	lower_title =title.lower()
	for index,i in enumerate(titles):
		if i.lower() == lower_title:
			statuses[index] = 'read'
			break
	else:
		print('Title not found')


def mark_as_unread(title):
	lower_title = title.lower()
	for index,i in enumerate(titles):
		if i.lower() == lower_title:
			statuses[index] = 'unread'
			break
	else:
		print('Title not found')


def search_book(keyword):
	is_found = False
	for index, i in enumerate(titles):
		if keyword.lower() in i.lower() or keyword.lower() in authors[index].lower():
			print(f'\nTitle: {i}')
			print(f'Author: {authors[index]}')
			print(f'{statuses[index]}')
			is_found = True
	if not is_found:
		print('Not found')

def list_books():
	sorted_ = sorted(zip(titles, authors, statuses))
	sorted_books = sorted(sorted_, key=lambda book: book[0].lower())
	for title,author,status in sorted_books:
		print(f'\nTitle: {title}')
		print(f'Author: {author}')
		print(f'{status}')
		print()


def suggest_book():
	books_unread = []
	for index in range(len(statuses)):
		status = statuses[index].lower()
		if status == 'unread':
			book_title = titles[index]
			books_unread.append(book_title)
	if len(books_unread) == 0:
		print('No unread books left')
	else:
		selected_book = random.choice(books_unread)
		selected_index = titles.index(selected_book)
		selected_author = authors[selected_index]
		print(f'{selected_book},\n by\n   {selected_author}')


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

def saving_to_txt():
	with open('Books', 'w') as txt:
		for i in range (len(titles)):
			txt.write(f'{titles[i]} | {authors[i]}\n')

def main():
	print("📚 Welcome to the Digital Book Collection Manager 📚\n")
	while True:
		saving_to_txt()
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
			print("Invalid option. Please choose a number from 1 to 9.")


if __name__ == "__main__":
	main()
