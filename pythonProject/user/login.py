# Python Console Application for User Login Workflow with Validations

import re

class UserService:
    def login(self):
        print("Login Process")
        username_email = input("Enter your username or email: ")
        password = input("Enter your password: ")
        remember_me = input("Remember Me (yes/no): ").lower() == 'yes'

        # Validate inputs
        if not username_email:
            print("Username or email is required.")
            return
        if not password:
            print("Password is required.")
            return

        # Simulate validation and authentication
        if self.validate_login(username_email, password):
            print("Login successful! Redirecting to dashboard...")
        else:
            print("Login failed! Please check your credentials.")

    def password_recovery(self):
        print("Password Recovery Process")
        email = input("Enter your registered email: ")

        # Simulate email validation and sending recovery email
        if self.validate_email(email):
            print("Password recovery email sent! Please check your inbox.")
        else:
            print("Invalid email format.")

    def password_reset(self):
        print("Password Reset Process")
        new_password = input("Enter your new password: ")
        confirm_password = input("Re-enter your new password: ")

        # Simulate password validation and update
        if self.validate_passwords(new_password, confirm_password):
            print("Password reset successful! Redirecting to login...")
        else:
            print("Passwords do not match or do not meet criteria.")

    def register(self):
        print("Registration Process")
        full_name = input("Enter your full name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        confirm_password = input("Re-enter your password: ")

        # Simulate registration validation and account creation
        if self.validate_registration(full_name, email, password, confirm_password):
            print("Registration successful! Redirecting to login...")
        else:
            print("Registration failed! Please check your input.")

    def validate_login(self, username_email, password):
        # Placeholder for actual validation logic
        # For demonstration, assume valid credentials are "user@example.com" and "password123"
        return username_email == "user@example.com" and password == "password123"

    def validate_email(self, email):
        # Basic email format validation
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def validate_passwords(self, new_password, confirm_password):
        # Check if passwords match and meet criteria
        return new_password == confirm_password and len(new_password) >= 8

    def validate_registration(self, full_name, email, password, confirm_password):
        # Check all registration fields
        return all([
            full_name,
            self.validate_email(email),
            password == confirm_password,
            len(password) >= 8
        ])

def main():
    user_service = UserService()
    while True:
        print("\nUser Controller")
        print("1. Login")
        print("2. Password Recovery")
        print("3. Password Reset")
        print("4. Register")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            user_service.login()
        elif choice == '2':
            user_service.password_recovery()
        elif choice == '3':
            user_service.password_reset()
        elif choice == '4':
            user_service.register()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
