from collections import deque

# Stack implementation using list to navigate browsing history

site_stack = ['http://cnn.com/', 'http://thewhitelabel.com/', 'http://redit.com/', 'http://web.facebook.com/']

print(site_stack.pop())
print(site_stack)
print(site_stack[-1])

# implementation of stack in python using deque() - recommended way
stack = deque()
stack.append('https://cnn.com/')
stack.append('https://cnn.com/world')
stack.append('https://cnn.com/china')
stack.append('https://cnn.com/india')
stack.append('https://cnn.com/Nigeria')
stack.pop()

print(stack)

