import sys
from automat_controller.AutomatController import AutomatController


ERROR_NOT_ENOUGH_ARGUMENTS = 'The number of arguments does not match the task condition\nInput should look: TransformationAutomat.exe <input file> <output file>\n'


def main():
    try:
        # if len(sys.argv) != 3:
        #     print(ERROR_NOT_ENOUGH_ARGUMENTS)
        #     return

        automat_controller = AutomatController('input1.txt', 'o.txt')
        automat_controller.process_command()
    except Exception as error:
        raise(error)

if __name__ == "__main__":
    main()
