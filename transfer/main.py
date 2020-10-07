import sys
from automat_controller import AutomatController


ERROR_NOT_ENOUGH_ARGUMENTS = 'Invalid arguments input\nInput should look: main.py ' \
                             '<input file> <output file>\n '


def main():
    try:
        if len(sys.argv) != 3:
            print(ERROR_NOT_ENOUGH_ARGUMENTS)
            return

        automat_controller = AutomatController(sys.argv[1], sys.argv[2])
        automat_controller.process_command()
    except Exception as error:
        raise error


if __name__ == "__main__":
    main()
