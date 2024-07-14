import pandas as pd
from login import *
from books import *
from users import *
from AI import Ask_AI


users_file_path = 'C:/Users/HP/Downloads/techolution/storage_excels/credentials.xlsx'
user_auth_manager = UserAuthManager(users_file_path)

file_path = 'C:/Users/HP/Downloads/techolution/storage_excels/book_storage.xlsx'
book_manager = BookManager(file_path)

users_file_path = 'C:/Users/HP/Downloads/techolution/storage_excels/users.xlsx'
user_manager = UserManager(users_file_path)


# Function to manage books
def manage_books():
    while True:
        print("\nBook Management")
        print("1. Add a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Show all books")
        print("5. Show book by ISBN")
        print("6. Show books by title")
        print("7. Show books by author")
        print("8. Return a book")
        print("9. Take a book")
        print("10. show all book available at current datetime")
        print("11. Back to main menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            book_manager.add_book(isbn, title, author)
        elif choice == '2':
            isbn = input("Enter ISBN: ")
            title = input("Enter title (leave blank if no change): ")
            author = input("Enter author (leave blank if no change): ")
            book_manager.update_book(isbn, title, author)
        elif choice == '3':
            isbn = input("Enter ISBN: ")
            book_manager.delete_book(isbn)
        elif choice == '4':
            book_manager.show_all_books()
        elif choice == '5':
            isbn = input("Enter ISBN: ")
            book_manager.show_book_by_isbn(isbn)
        elif choice == '6':
            title = input("Enter title: ")
            book_manager.show_books_by_title(title)
        elif choice == '7':
            author = input("Enter author: ")
            book_manager.show_books_by_author(author)
        elif choice == '8':
            isbn = input("Enter ISBN: ")
            book_manager.return_book(isbn)
        elif choice == '9':
            title = input("Enter title: ")
            check_out_date = input("Enter check-out date (dd/mm/yyyy): ")
            book_manager.take_book(title, check_out_date)

        elif choice == '10':
            book_manager.show_available_books()

        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")



# Function to manage users
def manage_users():
    while True:
        print("\nUser Management")
        print("1. Add a user")
        print("2. Update a user")
        print("3. Delete a user")
        print("4. Show all users")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            isbn = input("Enter ISBN (optional): ")
            user_manager.add_user(user_id, name, isbn)
        elif choice == '2':
            user_id = input("Enter user ID: ")
            name = input("Enter name (leave blank if no change): ")
            isbn = input("Enter ISBN (leave blank if no change): ")
            user_manager.update_user(user_id, name, isbn)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            user_manager.delete_user(user_id)
        elif choice == '4':
            user_manager.show_all_users()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to handle user login/signup and navigation
def main():
    authenticated = False
    
    while not authenticated:
        choice = input("Welcome! Enter 'login' or 'signup': ").lower()
        if choice == 'login':
            while True:
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                if user_auth_manager.login_user(email, password):
                    print("Login successful.")
                    authenticated = True
                    break
                else:
                    print("Login unsuccessful. Email or password incorrect.")
                    break
        elif choice == 'signup':
            while True:
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                success, message = user_auth_manager.signup_user(email, password)
                print(message)
                if success:
                    authenticated = True
                    break
                else:
                    print("Email ID already exists. Move to login or continue with signup.")
                    break
        else:
            print("Invalid choice. Please enter 'login' or 'signup'.")

    while authenticated:
        print("\nMain Menu")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Ask AI")
        print("4. Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            manage_books()
        elif choice == '2':
            manage_users()
        elif choice == '3':
            input_query = input('enter your pompt ')
            ai_out = Ask_AI(input_query)
            print(ai_out)
        elif choice == '4':
            print("Logged out.")
            authenticated = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
