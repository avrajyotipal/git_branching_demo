from login import login_user
from profile import show_profile
from dashboard import show_dashboard


def main():
    print("=== User Management Application ===")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if login_user(username, password):
        print("\nLogin successful!")

        show_profile(username)
        show_dashboard(username)
    else:
        print("\nInvalid username or password.")


if __name__ == "__main__":
    main()