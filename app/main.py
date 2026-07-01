import sys


def main():

    while True:

        built_in_commands = ["echo", "exit", "type"]

        sys.stdout.write("$ ")

        # wait for user input
        command = input()

        if command == "exit":
            break

        elif command.startswith("type "):
            if command.split("type ", 1)[1] in built_in_commands:
                print(f"{command.split("type ", 1)[1]} is a shell builtin")
            else:
                print(f"{command.split("type ", 1)[1]}: not found")

        elif command.startswith("echo "):
            print(command.split("echo ", 1)[1])

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
