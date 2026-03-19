import sys

def type(string ->str):
    builtin = ['exit' , 'echo' , 'type']
    if string in builtin :
        sys.stdout.write(f'{string} is a shell builtin')
    else:
        sys.stdout.write(f'{command}: not found')

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        match command:
            case 'exit':
                break
            case command if command.startswith('echo '):
                sys.stdout.write(f'{command[5:]}\n')
            case command if command.startswith('type  '):
                type(command[5:])
            case _:
                print(f'{command}: command not found')


if __name__ == "__main__":
    main()
