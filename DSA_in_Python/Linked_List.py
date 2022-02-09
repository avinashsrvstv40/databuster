class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def get_len(self):
        count = 0
        iter = self.head
        while iter:
            count += 1
            iter = iter.next

        return count

    def remove_at(self, index):

        if index < 0 or index >= self.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        counter = 0
        iter = self.head

        while iter:
            if counter == index - 1:
                iter.next = iter.next.next
                break

            iter = iter.next
            counter += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)

        counter = 0

        iter = self.head

        while iter:
            if counter == index - 1:
                node = Node(data, iter.next)
                iter.next = node
                break

            counter += 1
            iter = iter.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([33, 44, 62, 13])
    ll.remove_at(2)
    # ll.insert_at_beginning(22)
    # ll.insert_at_beginning(12)
    # ll.insert_at_end(89)
    ll.insert_at(0,"fang")
    ll.print()