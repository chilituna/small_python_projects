logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero!")
        return None
    return n1 / n2

Keys = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

Options = {
    "n": "To start over, type 'n'",
    "y": "To continue calculating with the above result, type 'y'",
    "q": "To quit, type 'q'"
}

Number = ["0","1","2","3","4","5","6","7","8","9", ".", "-"]

def get_number():
    n_valid = False
    while not n_valid:
        n_valid = True
        n = input("Insert the number: ")
        if n.strip() == "":
            print("Incorrect input. Please enter a valid number.\n")
            n_valid = False
            continue
        else:
            for letter in n:
                if letter not in Number:
                    print("Incorrect input. Please enter a valid number.\n")
                    n_valid = False
                    break

    return float(n)


def get_operator():
    for symbol in Keys:
        print(symbol)
    op = input("Select the operator: ")
    while op not in Keys:
        print("incorrect input\n")
        op = input("Select the operator: ")
    return op

def calculator():
    n1 = get_number()
    continue_calc = True
    while continue_calc:
        operator = get_operator()
        n2 = get_number()
        result = Keys[operator](n1, n2)
        if result is None:
            carry_on = input(f"{Options['n']}\n{Options['q']}\n")
            while carry_on == 'y' or carry_on not in Options:
                print("Wrong input!\n")
                carry_on = input(f"{Options['n']}\n{Options['q']}\n")
            if carry_on == 'q':
                    return
            else:
                return calculator()
        else:
            print(f"{n1} {operator} {n2} = {result}\n")
            carry_on = input(f"{Options['y']}\n{Options['n']}\n{Options['q']}\n")
            while carry_on not in Options:
                print("Wrong input!\n")
                carry_on = input(f"{Options['y']}\n{Options['n']}\n{Options['q']}\n")
            if carry_on == 'y':
                n1 = result
                print(f"\nNumber = {result}")
            elif carry_on == 'n':
                return calculator()
            elif carry_on == 'q':
                return

calculator()









