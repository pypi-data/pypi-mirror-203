
from nodes.s_node import SNode
'''
class CircularSinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 1 if head else 0
        if head:
            self.tail.next = self.head

    def insert_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1

    def insert_tail(self, node):
        if not self.head:
            self.insert_head(node)
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            self.size += 1

    def insert(self, node, position):
        if position <= 0 or not self.head:
            self.insert_head(node)
        elif position >= self.size:
            self.insert_tail(node)
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def delete_head(self):
        if not self.head:
            return
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1

    def delete_tail(self):
        if not self.head:
            return
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
        self.size -= 1

    def delete(self, node):
        if not self.head:
            return
        elif self.head.data == node.data:
            self.delete_head()
        elif self.tail.data == node.data:
            self.delete_tail()
        else:
            current = self.head
            while current.next and current.next.data != node.data:
                current = current.next
            if current.next:
                current.next = current.next.next
                self.size -= 1

    def sorted_insert(self, node):
        if not self.is_sorted():
            self.sort()
        if not self.head or self.head.data >= node.data:
            self.insert_head(node)
        else:
            current = self.head
            while current.next != self.head and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            if current == self.tail:
                self.tail = node
            self.size += 1

    def is_sorted(self):
        current = self.head
        for _ in range(self.size - 1):
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if self.size > 1:
            current = self.head
            while current.next != self.head:
                next_node = current.next
                while next_node != self.head:
                    if current.data > next_node.data:
                        current.data, next_node.data = next_node.data, current.data
                    next_node = next_node.next
                current = current.next

    def search(self, node):
        current = self.head
        for _ in range(self.size):
            if current.data == node.data:
                return current
            current = current.next
        return None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        print("Sorted: ", self.is_sorted)
        print("List content:")
        for _ in range(self.size):
            print(f"{current.data}", end=" -> ")
            current = current.next
        print("head")
        print(f"List length: {self.size}")
'''
from nodes import SNode
from . import SinglyLL

class CircularSinglyLinkedList(SinglyLL):
    def __init__(self, head=None):
        super().__init__(head)
        if self.head is not None:
            self.tail.next = self.head  # Update tail.next to point to head

    def insert_head(self, node: SNode):
        super().insert_head(node)
        self.tail.next = self.head  # Update tail.next to point to head

    def insert_tail(self, node: SNode):
        super().insert_tail(node)
        self.tail.next = self.head  # Update tail.next to point to head

    def delete_head(self):
        if self.head is None:
            return None  # List is already empty

        deleted_node = self.head

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.size -= 1
        return deleted_node


    def delete_tail(self):
        if self.head is None:
            return None  # List is already empty

        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return deleted_node

        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next

        deleted_node = current
        prev.next = self.head
        self.tail = prev
        self.size -= 1
        return deleted_node


    def clear(self):
        super().clear()
        if self.tail is not None:
            self.tail.next = None  # Break the circular connection


    def delete(self, node: SNode):
        if self.head is None:
            print("List is empty")
            return None

        if self.head.data == node.data:
            return self.delete_head()

        elif self.tail.data == node.data:
            return self.delete_tail()

        current = self.head
        prev = None
        while current.next != self.head:
            if current.next.data == node.data:
                deleted_node = current.next
                current.next = current.next.next
                self.size -= 1
                return deleted_node
            prev = current
            current = current.next

        print("Node not found in list")
        return None


    def sort(self):
        if self.head is None or self.head.next is None:
            return 

        sorted_list = None
        tail = None

        current = self.head
        while current:
            next_node = current.next

            if sorted_list is None or sorted_list.data > current.data:
                current.next = sorted_list
                sorted_list = current
                if tail is None:
                    tail = current
            else:
                runner = sorted_list
                while (runner.next != sorted_list) and (runner.next.data < current.data):
                    runner = runner.next

                current.next = runner.next
                runner.next = current

                if runner.next.next is None:
                    tail = current

            current = next_node
            if current == self.head:  # Break the loop when the original head is reached
                break

        self.head = sorted_list
        self.tail = tail
        self.tail.next = self.head





    def sorted_insert(self, node: SNode):
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = self.head
        elif node.data < self.head.data:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        else:
            current = self.head
            while current.next != self.head and current.next.data < node.data:
                current = current.next

            node.next = current.next
            current.next = node
            if node.next == self.head:
                self.tail = node

        self.size += 1





    def is_sorted(self):
        # If the list is empty or has only one element, it is considered sorted
        if not self.head or not self.head.next:
            return True

        # Call the parent class's is_sorted() method
        sorted_status = super().is_sorted()

        # Check if the tail data is less than the head data, which indicates a circular break
        if sorted_status and self.tail.data > self.head.data:
            return False

        return sorted_status



    def Print(self):
        if self.head is None:
            print("List is empty")
            return

        print(f"List length: {self.size}")
        print("Sorted status:", "Sorted" if self.is_sorted() else "Not sorted")

        print("List content:")
        current = self.head
        count = 0
        while current is not None and count < self.size:
            if current == self.head:
                print(f"{current.data} (head) ->", end=" ")
            elif current != self.tail:
                print(f"{current.data} ->", end=" ")
            else:
                print(f"{current.data} (tail)", end=" ")

            current = current.next
            count += 1
        print("-> (head)")



