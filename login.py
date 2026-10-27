import getpass
import sys

# Simple user database with predefined credentials (username: password)
USERS = {
    "admin": "admin123",
    "user": "password123",
    "alice": "wonderland"
}

def login(username, password):
    """Authenticate user with given username and password."""
    if username in USERS and USERS[username] == password:
        return True
    return False

def main():
    print("=== Simple Login System ===")
    
    # Allow command-line credentials or interactive prompt
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
    else:
        try:
            username = input("Enter username: ").strip()
            if sys.stdin.isatty():
                password = getpass.getpass("Enter password: ")
            else:
                password = sys.stdin.readline().rstrip("\r\n")
        except (KeyboardInterrupt, EOFError):
            print("\nLogin cancelled.")
            sys.exit(1)

    if login(username, password):
        print(f"\nLogin successful! Welcome, {username}.")
        return 0
    else:
        print("\nLogin failed! Invalid username or password.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
