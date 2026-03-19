import sys
import os


def check_path(cmnd):
    for p in os.environ["PATH"].split(":"):
        full = os.path.join(p,cmnd)
        
        if os.path.exists(full):
            print(f'{full}\n')



def type(string):
    builtin = ['exit' , 'echo' , 'type']
    if string in builtin :
        sys.stdout.write(f'{string} is a shell builtin\n')
    elif True:
        check_path(string)
    else:
        sys.stdout.write(f'{string}: not found\n')

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
            case command if command.startswith('type '):
                type(command[5:])
            case _:
                print(f'{command}: command not found')


if __name__ == "__main__":
    main()
