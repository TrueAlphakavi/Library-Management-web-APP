import pandas as pd
import random
import string

class UserAuthManager:
    def __init__(self, users_file_path):
        self.users_file_path = users_file_path

    # Function to load user credentials from the Excel file
    def load_user_credentials(self):
        try:
            df = pd.read_excel(self.users_file_path)
            return df
        except FileNotFoundError:
            print(f"File {self.users_file_path} not found.")
            return None

    # Function to save user credentials to the Excel file
    def save_user_credentials(self, df):
        df.to_excel(self.users_file_path, index=False)

    # Function to generate a random unique ID
    @staticmethod
    def generate_unique_id():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Function to handle user login
    def login_user(self, email, password):
        df = self.load_user_credentials()
        if df is not None:
            user = df[(df['email id'] == email) & (df['password'] == password)]
            if not user.empty:
                return True
        return False

    # Function to handle user signup
    def signup_user(self, email, password):
        df = self.load_user_credentials()
        if df is not None and email in df['email id'].values:
            return False, "Email ID already exists. Move to login or continue with signup."
        new_user_id = self.generate_unique_id()
        new_user = pd.DataFrame({'email id': [email], 'password': [password], 'user id': [new_user_id]})
        if df is not None:
            df = pd.concat([df, new_user], ignore_index=True)
        else:
            df = new_user
        self.save_user_credentials(df)
        return True, f"User with email {email} signed up successfully with User ID {new_user_id}."




