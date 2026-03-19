import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        match command:
            case 'exit':
                break
            case command.startwith('echo ') == True:
                print(f'\n{command[5:]}')
            case _:
                print(f'{command}: command not found')


if __name__ == "__main__":
    main()
