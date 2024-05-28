from collections import deque

# First question, reverse a string
s = 'We will conquer COVID-19'
print(s[::-1])
# An easy way to reverse a string is by assigning it to a variable and then using the
# above syntax

 
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(string):
    stack = Stack()

    for char in string:
        stack.push(char)

    rstr = ''
    while stack.size() != 0:
        rstr += stack.pop()

    return rstr
# Another way of reversing a string is  by creating a deque and then appending each
# character. Next we want to create an empty variable and while the len of our
# stack isn't empty we want to pop out those characters and add it to our variable
# containing the empty string. Then we return the function and call/print it in our
# main function

# Second question, check if parenthesis is balanced


def is_match(char1, char2):
    match_dict = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    return match_dict[char1] == char2


def is_balanced(string):
    stack = Stack()

    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char == ']':
            if stack.size() == 0:
                return False
            if not is_match(stack.pop(), char):
                return False

    return stack.size() == 0
# Basically how this works is that we first create a dictionary data structure in one function.
# This function takes up 2 parameters, the first being the key and the second being the value
# After creating the dict we return true or false to check if what we passed as our key and value
# are actually mapped to each other in the dictionary we created.
# Next we create our main function where we iterate through the string and if the character is an
# opening of any parenthesis we add it to our stack and if it isn't we check if we've added any
# character to our stack already i.e. stack length. If it is 0 we return false because it means
# we've accessed the closing of the parenthesis before the opening.
# N/B we always pull the last opening we entered to compare with the closing we are bring to
# ensure that they are mapped i our dict in the first function before outputting false.


if __name__ == '__main__':
    print(reverse_string('We will conquer COVID-19'))
    print(reverse_string("I'm learning gradually"))
    print(is_balanced("({a+b})"))
    print(is_balanced("({a+b))"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced(")("))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
