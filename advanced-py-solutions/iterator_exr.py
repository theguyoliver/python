class FibCalc:
    def __init__(self, limit):
        self.arr = [0, 1]
        self.size = range(0, 100)
        self.index = -1
        self.limit = limit
        for i in self.size:
            self.arr.append(self.arr[i] + self.arr[i + 1])

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.limit:
            raise StopIteration

        return self.arr[self.index]


f = FibCalc(20)
itr = iter(f)
# while True:
#     try:
#         print(next(itr))
#     except StopIteration:
#         break


# print(next(itr))
# print(next(itr))


def square_cal():
    for i in range(1, 21):
        yield i * i


for n in square_cal():
    if n > 36:
        break
    print(n)


# itr = iter(square_cal())
# while True:
#     try:
#         print(next(itr))
#     except StopIteration:
#         break
