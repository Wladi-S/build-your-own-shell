import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")

    # wait for user input
    input_text = input()
    print(f"{input_text}: command not found")


if __name__ == "__main__":
    main()
