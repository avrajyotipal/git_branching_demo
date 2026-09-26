def login_user(username, password):
    if username == "admin" and password == "admin123":
        print("Authentication successful.")
        return True

    print("Authentication failed.")
    return False
