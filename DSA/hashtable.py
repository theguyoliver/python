class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    # Here we define the size of our array and then create an array of that size using
    # list comprehension

    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.MAX

    # Here, to calculate the index in the array where the value corresponding to a particular
    # key will be stored, we first calculate the sum of the ASKI number corresponding to each
    # character in the ASKI table. This number is gotten by calling the ord() func on the
    # character. We then calculate the mod of the sum of that number with the array size
    # i.e. self.MAX or 100
 
    def __setitem__(self, key, value):
        i = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[i]):
            if len(element) == 2 and element[0] == key:
                self.arr[i][idx] = (key, value)
                found = True
                break
            if not found:
                self.arr[i].append((key, value))

    # i = self.get_hash(key)
    # self.arr[i] = value   -> with collision handling
    # Here, we use the __setitem__ operator to add key-value pairs to the hash table
    # First by determining the index using the hash function and then by initailize
    # the value of the key at that index

    def __getitem__(self, key):
        i = self.get_hash(key)
        for element in self.arr[i]:
            if element[0] == key:
                return element[1]

    # i = self.get_hash(key)
    # return self.arr[i]
    # Here we make use of the __getitem__ operator to find the value corresponding
    # to a key

    def __delitem__(self, key):
        i = self.get_hash(key)
        for idx, element in enumerate(self.arr[i]):
            if element == key:
                del self.arr[i][idx]

    # i = self.get_hash(key)
    # self.arr[i] = None


#     Without the collision handling

if __name__ == '__main__':
    h = HashTable()
    h['age'] = 24
    print(h.arr)
    del h['age']
    print(h.arr)

#     Rewriting our code to handle collisions in hash tables
