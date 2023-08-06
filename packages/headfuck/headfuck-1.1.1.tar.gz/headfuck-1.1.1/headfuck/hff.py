from headfuck import interpreter
import sys
def read_from_file():
    try:
        f = open(sys.argv[1], "r")
        result = interpreter.interpret(f.read())
        print(result)
        quit()
    except IndexError:
        print("Error: You did not name a file to interpret.")
    except FileNotFoundError:
        print("Error: The file you named does not exist.")
read_from_file()