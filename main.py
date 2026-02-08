import os
import sys
import shutil


def display_help():
    """Displays the help message for the CLI"""
    print("Usage: cliche [command]")
    print("\nCommands:")
    print("     init  Create a new project")
    print("     run   Run the project")
    print("     help  View this help message")

def initProject(name):
    os.mkdir(name)
    shutil.copy("test.py", f"{name}/main.py")
    os.chdir(name)

def runProject(name):
    os.system(f"python {name}/main.py")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        display_help()
    else:
        command = sys.argv[1]
        if command == "init":
            if len(sys.argv) > 2:
                initProject(sys.argv[2])
            else:
                print("Error: Missing project name.")
            
        elif command == "run":
            if len(sys.argv) > 2:
                runProject(sys.argv[2])
            else:
                print("Error: Missing project name.")
        elif command == "help":
            display_help()
        else:
            print(f"Error: Unknown command '{command}'.")
            display_help()