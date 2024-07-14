# Library-Management-web-APP

**Overview**
This project is a comprehensive Library Management System built in Python, designed to manage both user authentication and book management using Excel files for data storage.

Key Features

1. User Authentication Management

    Login Functionality
        Verifies user credentials against stored data in an Excel file.
   
    Signup Functionality
        Allows new users to register.
   
    Checks for existing email IDs to prevent duplicates.
        Generates a unique user ID for each new user.
   
    Excel Integration
        User credentials (email, password, user ID) are stored in an Excel file.
   
    Functions to load and save user data to/from Excel files.

3. Book Management
   
    Add New Book
        Allows adding new books with details like ISBN, title, author, check-in date, and check-out date.
   
    Update Book
        Updates book details based on ISBN.
   
    Delete Book
        Deletes books based on ISBN.
   
    Show All Books
        Displays all books with their availability status.
   
    Show Book by ISBN
        Shows details and availability of a specific book based on ISBN.
   
    Show Books by Title or Author
        Displays books by title or author with their availability status.
   
    Return Book
        Updates the check-out date to mark a book as returned.
   
    Take Book
        Sets the check-in and check-out dates for borrowing a book.
   
   
    Show Available Books
        Displays a list of currently available books.
   
5. Ask AI Feature
      AI Assistant Interaction
          Allows users to ask questions to an AI assistant.


**Technical Details**

      Programming Language: Python
      
      Libraries Used:
      pandas: For handling Excel file operations and data manipulation.
      random and string: For generating unique user IDs.
      google.genai : help to use gemini API for AI interactions.
      

Data Storage:
  User credentials and book data are stored in separate Excel files.

![login](https://github.com/user-attachments/assets/da57be67-412d-4f43-98a1-8f41d4ddb5c1)
![Manage books](https://github.com/user-attachments/assets/67c0a4b1-8bb8-41c0-b4ee-93539572cd73)
![Manage users](https://github.com/user-attachments/assets/d5eb81ad-e53c-4a37-a845-1c9d1ee1f14f)
![AI](https://github.com/user-attachments/assets/0614b746-ed3c-45a8-9746-ff200ac38577)
![High Level Arch](https://github.com/user-attachments/assets/2c2898ae-7b76-4d2c-b1f6-61d689dff5c2)

