import streamlit as st
import pandas as pd
import random
import string
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


def manage_books():
    st.subheader("Book Management")
    choice = st.selectbox("Choose an action", [
        "Add a book",
        "Update a book",
        "Delete a book",
        "Show all books",
        "Show book by ISBN",
        "Show books by title",
        "Show books by author",
        "Return a book",
        "Take a book",
        "Show all books available at current datetime"
    ])

    if choice == "Add a book":
        isbn = st.text_input("Enter ISBN")
        title = st.text_input("Enter title")
        author = st.text_input("Enter author")
        if st.button("Add Book"):
            book_manager.add_book(isbn, title, author)

    elif choice == "Update a book":
        isbn = st.text_input("Enter ISBN")
        title = st.text_input("Enter title (leave blank if no change)")
        author = st.text_input("Enter author (leave blank if no change)")
        if st.button("Update Book"):
            book_manager.update_book(isbn, title, author)

    elif choice == "Delete a book":
        isbn = st.text_input("Enter ISBN")
        if st.button("Delete Book"):
            book_manager.delete_book(isbn)

    elif choice == "Show all books":
        book_manager.show_all_books()

    elif choice == "Show book by ISBN":
        isbn = st.text_input("Enter ISBN")
        if st.button("Show Book"):
            book_manager.show_book_by_isbn(isbn)

    elif choice == "Show books by title":
        title = st.text_input("Enter title")
        if st.button("Show Books"):
            book_manager.show_books_by_title(title)

    elif choice == "Show books by author":
        author = st.text_input("Enter author")
        if st.button("Show Books"):
            book_manager.show_books_by_author(author)

    elif choice == "Return a book":
        isbn = st.text_input("Enter ISBN")
        if st.button("Return Book"):
            book_manager.return_book(isbn)

    elif choice == "Take a book":
        title = st.text_input("Enter title")
        check_out_date = st.text_input("Enter check-out date (YYYY-MM-DD)")
        if st.button("Take Book"):
            book_manager.take_book(title, check_out_date)

    elif choice == "Show all books available at current datetime":
        out_sab = book_manager.show_available_books()
        st.write(out_sab)
        print('----------',out_sab)





def manage_users():
    st.subheader("User Management")
    choice = st.selectbox("Choose an action", [
        "Add a user", 
        "Update a user",
        "Delete a user",
        "Show all users",
    ])

    if choice == "Add a user":
        user_id = st.text_input("Enter user ID: ")
        name = st.text_input("Enter name: ")
        isbn = st.text_input("Enter ISBN (optional): ")

        if st.button("Add User"):
            user_manager.add_user(user_id, name, isbn)
            st.success('user added')


    elif choice == "Update a user":
        user_id = st.text_input("Enter user ID: ")
        name = st.text_input("Enter name (leave blank if no change): ")
        isbn = st.text_input("Enter ISBN (leave blank if no change): ")
        if st.button("Update user"):
            user_manager.update_user(user_id, name, isbn)
            st.success('user changed')


    elif choice == "Delete a user":
        user_id = st.text_input("Enter user ID: ")
        if st.button("Delete user"):
            user_manager.delete_user(user_id)
            st.success('user Deleted')


    elif choice == "Show all users":
            if st.button("All user"):
                out_sau = user_manager.show_all_users()
                st.write(out_sau)              


def st_ai():
    query = st.text_area('Enter your prompt ')
    st_ai_out = Ask_AI(query)
    if st.button('ask'):
        st.write(st_ai_out)




def main():
    st.title("Library Management System")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_email = None

    if st.session_state.logged_in:
        st.sidebar.subheader(f"Welcome, {st.session_state.user_email}")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = None
            st.sidebar.empty()
            st.experimental_rerun()

        st.subheader("Main Menu")
        choice = st.selectbox("Choose Action", ["Manage Books", "Manage Users","Ask AI"])

        if choice == "Manage Books":
            manage_books()

        elif choice == "Manage Users":
            manage_users()

        elif choice == "Ask AI":
            st_ai()


    else:
        choice = st.sidebar.selectbox("Choose Action", ["Login", "Signup"])

        if choice == "Login":
            st.subheader("Login")
            email = st.text_input("Enter your email")
            password = st.text_input("Enter your password", type="password")
            if st.button("Login"):
                if user_auth_manager.login_user(email, password):
                    st.success("Login successful.")
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.experimental_rerun()
                else:
                    st.error("Login unsuccessful. Email or password incorrect.")
        
        elif choice == "Signup":
            st.subheader("Signup")
            email = st.text_input("Enter your email")
            password = st.text_input("Enter your password", type="password")
            if st.button("Signup"):
                success, message = user_auth_manager.signup_user(email, password)
                if success:
                    st.success(message)
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.experimental_rerun()
                else:
                    st.error(message)
                    

if __name__ == "__main__":
    main()
