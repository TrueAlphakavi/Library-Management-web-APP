import pandas as pd
from datetime import datetime

class BookManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = self.load_books_from_excel()

    # Function to load books from the Excel file
    def load_books_from_excel(self):
        df = pd.read_excel(self.file_path)
        books = df.to_dict('records')
        return books

    # Function to save books to the Excel file
    def save_books_to_excel(self):
        df = pd.DataFrame(self.books)
        df.to_excel(self.file_path, index=False)

    # Function to add a new book
    def add_book(self, isbn, title, author, check_in_date=None, check_out_date=None):
        book = {
            'isbn': isbn,
            'title': title,
            'author': author,
            'check in date': check_in_date,
            'check out date': check_out_date
        }
        self.books.append(book)
        self.save_books_to_excel()
        print(f"Book with ISBN {isbn} added.")

    # Function to update an existing book based on ISBN
    def update_book(self, isbn, title=None, author=None, check_in_date=None, check_out_date=None):
        for book in self.books:
            if book['isbn'] == isbn:
                if title:
                    book['title'] = title
                if author:
                    book['author'] = author
                if check_in_date:
                    book['check in date'] = check_in_date
                if check_out_date:
                    book['check out date'] = check_out_date
                self.save_books_to_excel()
                print(f"Book with ISBN {isbn} updated.")
                return
        print(f"No book found with ISBN {isbn}.")

    # Function to delete an existing book based on ISBN
    def delete_book(self, isbn):
        self.books = [book for book in self.books if book['isbn'] != isbn]
        self.save_books_to_excel()
        print(f"Book with ISBN {isbn} deleted.")

    # Function to show all books with availability status
    def show_all_books(self):
        if not self.books:
            print("No books available.")
            return
        
        current_date_time = datetime.now()
        
        for book in self.books:
            title = book['title']
            check_out_date = book['check out date']
            
            if pd.isnull(check_out_date) or check_out_date <= current_date_time:
                print(f"Book '{title}' is currently available.")
            else:
                formatted_check_out_date = check_out_date.strftime('%d/%m/%Y %H:%M:%S')
                print(f"Book '{title}' is not available. It will be available after {formatted_check_out_date}.")

    # Function to show a book based on ISBN with availability status
    def show_book_by_isbn(self, isbn):
        for book in self.books:
            if book['isbn'] == isbn:
                title = book['title']
                check_out_date = book['check out date']
                
                if pd.isnull(check_out_date) or check_out_date <= datetime.now():
                    print(f"Book '{title}' is currently available.")
                else:
                    formatted_check_out_date = check_out_date.strftime('%d/%m/%Y %H:%M:%S')
                    print(f"Book '{title}' is not available. It will be available after {formatted_check_out_date}.")
                return
        print(f"No book found with ISBN {isbn}.")

    # Function to show books based on title with availability status
    def show_books_by_title(self, title):
        found_books = [book for book in self.books if book['title'].lower() == title.lower()]
        if not found_books:
            print(f"No books found with title '{title}'.")
            return
        
        current_date_time = datetime.now()
        
        for book in found_books:
            check_out_date = book['check out date']
            
            if pd.isnull(check_out_date) or check_out_date <= current_date_time:
                print(f"Book '{title}' is currently available.")
            else:
                formatted_check_out_date = check_out_date.strftime('%d/%m/%Y %H:%M:%S')
                print(f"Book '{title}' is not available. It will be available after {formatted_check_out_date}.")

    # Function to show books based on author with availability status
    def show_books_by_author(self, author):
        found_books = [book for book in self.books if book['author'].lower() == author.lower()]
        if not found_books:
            print(f"No books found by author '{author}'.")
            return
        
        current_date_time = datetime.now()
        
        for book in found_books:
            title = book['title']
            check_out_date = book['check out date']
            
            if pd.isnull(check_out_date) or check_out_date <= current_date_time:
                print(f"Book '{title}' is currently available.")
            else:
                formatted_check_out_date = check_out_date.strftime('%d/%m/%Y %H:%M:%S')
                print(f"Book '{title}' is not available. It will be available after {formatted_check_out_date}.")

    # Function to return a book (update check out date to current date and time)
    def return_book(self, isbn):
        current_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        for book in self.books:
            if book['isbn'] == isbn:
                book['check out date'] = current_date_time
                self.save_books_to_excel()
                print(f"Book with ISBN {isbn} returned on {current_date_time}.")
                return
        print(f"No book found with ISBN {isbn}.")

    # Function to take a book (update check in date to current date and time and set the check out date)
    def take_book(self, title, check_out_date):
        current_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        for book in self.books:
            if book['title'].lower() == title.lower():
                if not book['check out date'] or datetime.strptime(book['check out date'], '%d/%m/%Y %H:%M:%S') <= datetime.now():
                    book['check in date'] = current_date_time
                    book['check out date'] = check_out_date
                    self.save_books_to_excel()
                    print(f"Book '{title}' taken. Check-in date: {current_date_time}, Check-out date: {check_out_date}.")
                    return
                else:
                    print(f"Book '{title}' is currently checked out and will be available after {book['check out date']}.")
                    return
        print(f"No book found with title '{title}'.")

    # Function to show available books
    def show_available_books(self):
        out_list = []
        current_date_time = datetime.now()
        available_books = [book for book in self.books if not book['check out date'] or book['check out date'] <= current_date_time]
        if not available_books:
            print("No books are currently available.")
            out_list.append(['No books are currently available.'])
            return out_list
        print(f"Books available as of {current_date_time.strftime('%d/%m/%Y %H:%M:%S')}:")
        for book in available_books:
            print(book['title'])
            out_list.append(book['title'])
        return out_list


