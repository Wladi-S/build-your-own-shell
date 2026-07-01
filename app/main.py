import sys


def main():

    while True:

        sys.stdout.write("$ ")

        # wait for user input
        input_text = input()
        if input_text == "exit":
            break
        print(f"{input_text}: command not found")


if __name__ == "__main__":
    main()
