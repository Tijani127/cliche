import os
import sys


def display_help():
    """Displays the help message for the CLI"""
    print("Usage: cliche [command]")
    print("\nCommands:")
    print("     init  Create a new project")
    print("     run   Run the project")
    print("     help  View this help message")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        display_help()
    else:
        command = sys.argv[1]
        if command == "init":
            os.mkdir("cliche_project")
            os.chdir("cliche_project")
            with open("main.py", 'w') as file:
                file.write("import sys\nimport os\ndef create_directory(name):\n\ntry:\nos.makedirs(name, exist_ok=True)\nprint(f"Directory '{name}' created successfully (or already exists).")\nexcept OSError as e:\nprint(f"Error creating directory '{name}': {e}")\ndef delete_file(name):\n\ntry:\nif os.path.exists(name):\nos.remove(name)\nprint(f"File '{name}' deleted successfully.")\nelse:\nprint(f"Error: File '{name}' not found.")\nexcept OSError as e:\nprint(f"Error deleting file '{name}': {e}")\ndef display_help():\n\nprint("Usage: python file_cli.py [command] [name]")\nprint("Commands:")\nprint("  create <dir_name>  Create a new directory.")\nprint("  delete <file_name> Delete a file.")\nprint("  help               Show this help message.")\nif __name__ == "__main__":\n# sys.argv contains all command-line arguments\nif len(sys.argv) < 2:\ndisplay_help()\nelse:\ncommand = sys.argv[1]\nif command == "create":\nif len(sys.argv) > 2:\ncreate_directory(sys.argv[2])\nelse:\nprint("Error: Missing directory name.")\nelif command == "delete":\nif len(sys.argv) > 2:\ndelete_file(sys.argv[2])\nelse:\nprint("Error: Missing file name.")\nelif command == "help":\ndisplay_help()\nelse:\nprint(f"Error: Unknown command '{command}'.")\ndisplay_help()")
        elif command == "run":
            os.system("python main.py")
        elif command == "help":
            display_help()
        else:
            print(f"Error: Unknown command '{command}'.")
            display_help()