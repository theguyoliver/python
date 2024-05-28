class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# node is an initial element in the linked list with data which can
# either be an integer, string, etc and next points to the next element


class LinkedList:

    def __init__(self):
        self.head = None

    # what happened here is that we created a parameter self which allows us to
    # create our linked list head. This head should be the first element or item in
    # the list...to be confirmed

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        # what happened here is that we want to add a node at the beginning of the list
        # meaning if we had a node already this new one will be in front of it
        # We call the node class to the variable and pass in the data we want to
        # add and also where we want the item to be linked to in this case it
        # will be the previous head and then we set the new head to the newly added node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next if itr.next.next else None
                break

            itr = itr.next

    def print(self):
        if self.head is None:
            print('Your linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '->' if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)


# Here we create a print method which we use to print or output all operations on our
# linked list. First we create a conditional to output above when the linked list
# is empty(self.head is None). If it isn't empty we create an itr variable pointing
# to the ll head and also a variable which converts all data input into a string
# which we can print after any iteration of the ll
# Next we iterate through the linked list using the while loop as long as it isn't empty
# p

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def print_forward(self):
        if self.head is None:
            print('Your list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(self.data) + '->' if itr.next else str(self.data)
            itr.next

        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_value(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
