import sys
import os

def create_directory(name):
    """Creates a new directory if it doesn't exist."""
    try:
        os.makedirs(name, exist_ok=True)
        print(f"Directory '{name}' created successfully (or already exists).")
    except OSError as e:
        print(f"Error creating directory '{name}': {e}")

def delete_file(name):
    """Deletes a file if it exists."""
    try:
        if os.path.exists(name):
            os.remove(name)
            print(f"File '{name}' deleted successfully.")
        else:
            print(f"Error: File '{name}' not found.")
    except OSError as e:
        print(f"Error deleting file '{name}': {e}")

def display_help():
    """Displays the help message for the CLI."""
    print("Usage: python file_cli.py [command] [name]")
    print("\nCommands:")
    print("  create <dir_name>  Create a new directory.")
    print("  delete <file_name> Delete a file.")
    print("  help               Show this help message.")

if __name__ == "__main__":
    # sys.argv contains all command-line arguments
    if len(sys.argv) < 2:
        display_help()
    else:
        command = sys.argv[1]
        if command == "create":
            if len(sys.argv) > 2:
                create_directory(sys.argv[2])
            else:
                print("Error: Missing directory name.")
        elif command == "delete":
            if len(sys.argv) > 2:
                delete_file(sys.argv[2])
            else:
                print("Error: Missing file name.")
        elif command == "help":
            display_help()
        else:
            print(f"Error: Unknown command '{command}'.")
            display_help()
