import sys
import os




def find_executable(cmd):
    for p in os.environ["PATH"].split(":"):
        full = os.path.join(p, cmd)

        if os.path.exists(full) and os.access(full, os.X_OK):
            return full   # STOP here

    return None



def type(string):
    builtin = ['exit' , 'echo' , 'type']
    if string in builtin :
        sys.stdout.write(f'{string} is a shell builtin\n')
    elif True:
        print(find_executable(string))
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
