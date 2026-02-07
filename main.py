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
                file.write("import os\nimport sys\n")
        elif command == "run":
            os.system("python main.py")
        elif command == "help":
            display_help()
        else:
            print(f"Error: Unknown command '{command}'.")
            display_help()