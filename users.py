import pandas as pd

class UserManager:
    def __init__(self, users_file_path):
        self.users_file_path = users_file_path
        self.users = self.load_users_from_excel()

    # Function to load users from the Excel file
    def load_users_from_excel(self):
        try:
            df = pd.read_excel(self.users_file_path)
            users = df.to_dict('records')
        except FileNotFoundError:
            print(f"File {self.users_file_path} not found. Returning empty list of users.")
            users = []
        return users

    # Function to save users to the Excel file
    def save_users_to_excel(self):
        df = pd.DataFrame(self.users)
        df.to_excel(self.users_file_path, index=False)

    # Function to add a new user
    def add_user(self, user_id, name, isbn=None):
        user = {
            'user id': user_id,
            'name': name,
            'isbn': isbn
        }
        self.users.append(user)
        self.save_users_to_excel()
        print(f"User with ID {user_id} added.")

    # Function to update an existing user based on user ID
    def update_user(self, user_id, name=None, isbn=None):
        for user in self.users:
            if user['user id'] == user_id:
                if name:
                    user['name'] = name
                if isbn:
                    user['isbn'] = isbn
                self.save_users_to_excel()
                print(f"User with ID {user_id} updated.")
                return
        print(f"No user found with ID {user_id}.")

    # Function to delete an existing user based on user ID
    def delete_user(self, user_id):
        self.users = [user for user in self.users if user['user id'] != user_id]
        self.save_users_to_excel()
        print(f"User with ID {user_id} deleted.")

    # Function to show all users
    def show_all_users(self):
        if not self.users:
            print("No users.")
            return ["No users."]
        for user in self.users:
            print(user)
        return self.users


