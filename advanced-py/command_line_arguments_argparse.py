import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # we can add arguments through
    parser.add_argument('--number1', help='first number')
    parser.add_argument('--number2', help='second number')
    parser.add_argument('--operation', help='operation', \
                        choices=['add', 'subtract', 'multiply'])
    # we add -- in front of the name of our argument to make it an optional argument as shown below
    # when we remove it we get a positional argument
    # Also the choices list above ties the user to only being able to use the following operations
    # hence when an operation outside that list is entered, it outputs an error immediately

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    # convert all inputs in command line from strings back to int
    result = None
    if args.operation == 'add':
        result = n1 + n2
    elif args.operation == 'subtract':
        if n1 > n2:
            result = n1 - n2
        else:
            result = n2 - n1
    elif args.operation == 'multiply':
        result = n1*n2

    print('Result:', result)

    # To run our command line in PyCharm, navigate just above to where we have the three dots after the
    # debug icon, select it and click edit, from there enter script parameters in this format
    # '--number1 24 --number2 32 --operation subtract' and run the code.
