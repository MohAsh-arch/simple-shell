import sys
import os
import subprocess




def find_executable(cmd):
    for p in os.environ["PATH"].split(":"):
        full = os.path.join(p, cmd)

        if os.path.exists(full) and os.access(full, os.X_OK):
            return full   # STOP here

    return f'{cmd}: not found'



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
                import shlex

                parts = shlex.split(command)
                exe_path = find_executable(parts[0])

                if exe_path.endswith("not found"):
                    sys.stdout.write(f'{parts[0]}: command not found')
                else:
                    subprocess.run([exe_path, *parts[1:]],executable=exe_path)


if __name__ == "__main__":
    main()
