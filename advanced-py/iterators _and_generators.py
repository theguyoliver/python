# There are used to iterate over iterables like lists, tuples and dict
# Example is the changing of channels in a remote controller
import time


class RemoteController:
    def __init__(self):
        self.channels = ['African Magic', 'Dove TV', 'CNN', 'Cartoon Network', 'France 24']
        self.index = -1

    # Self.index of -1 means that the tv is off and not showing any channels

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

    def previous(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration

        return self.channels[self.index]


# This blocks of code are very simple, we create our class with properties such as list of channels
# and the corresponding index of each channel in the list, next we create our a method(our in-built iter method)
# that returns an instance of the class and a next function that returns all the elements in the list
# the previous function isn't in-built, but we can use it to navigate to our previous channel just
# like is possible in normal remotes


# r = RemoteController()
# itr = iter(r)
# print(next(itr))
# print(next(itr))
# print(r.previous())
# print(r.previous())


# Generators are a simple way of creating iterators. Comparing the block of code we have below for
# generators and above for iterators we can see how generators really simplify the process of iteration.
# shorter block of code.
def remote_control_next():
    yield 'African Magic'
    yield 'Dove TV'
    yield 'CNN'
    yield 'Cartoon Network'
    yield 'France 24'


# Implementing the fibonacci series using generators
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# The above code is very easy we set the values of a and b to 0 and 1 initially, then we yield the value
# of 'a' each time we call the function and update the value of a as b while updating the value of our
# b as the sum of a and b. We then take care of the infinite loop below by specifying the values of a
# we want to stop printing


for i in fib():
    if i > 100:
        break
    print(i)

if __name__ == '__main__':
    itr = remote_control_next()
    print(next(itr))
    print(next(itr))
    # for i in remote_control_next():
    #     print(i)
