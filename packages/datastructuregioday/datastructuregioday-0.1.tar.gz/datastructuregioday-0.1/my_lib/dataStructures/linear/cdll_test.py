from nodes.d_node import DNode



class CircularDoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head if head else None
        self.size = 1 if head else 0
        if head:
            self.head.prev = self.tail
            self.tail.next = self.head

    def insert_head(self, node: DNode):
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size += 1

    def insert_tail(self, node: DNode):
        if self.head is None:
            self.insert_head(node)
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size += 1

    def insert(self, node: DNode, position: int):
        if position <= 0:
            self.insert_head(node)
            return
        if position >= self.size:
            self.insert_tail(node)
            return

        current = self.head
        count = 0
        while count < position and current:
            current = current.next
            count += 1

        node.prev = current.prev
        node.next = current
        current.prev.next = node
        current.prev = node
        self.size += 1

    def is_sorted(self):
        if self.head is None:
            return True
        
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head.next
        while current != self.head:
            node_to_insert = current
            current = current.next
            node_to_insert.prev.next = node_to_insert.next
            node_to_insert.next.prev = node_to_insert.prev

            temp = self.head
            while temp.next != self.head and temp.next.data < node_to_insert.data:
                temp = temp.next

            node_to_insert.prev = temp
            node_to_insert.next = temp.next
            temp.next.prev = node_to_insert
            temp.next = node_to_insert

            if node_to_insert.next is None:
                self.tail = node_to_insert

    def sorted_insert(self, node: DNode):
        if not self.is_sorted():
            self.sort()

        if self.head is None:
            node.prev = node
            node.next = node
            self.head = node
            self.tail = node
            self.size += 1
            return

        current = self.head
        while current != self.tail and current.data < node.data:
            current = current.next

        if current.data >= node.data:
            node.prev = current.prev
            node.next = current
            current.prev.next = node
            current.prev = node
            if current == self.head:
                self.head = node
        else:
            node.prev = self.tail
            node.next = self.head
            self.head.prev = node
            self.tail.next = node
            self.tail = node
        self.size += 1



    def delete_head(self):
        if self.head is None:
            return None

        deleted_node = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1
        return deleted_node

    def delete_tail(self):
        if self.tail is None:
            return None

        deleted_node = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size -= 1
        return deleted_node

    def delete(self, node: DNode):
        if self.head is None:
            return None

        if self.head.data == node.data:
            return self.delete_head()

        current = self.head
        while current.next != self.head:
            if current.next.data == node.data:
                deleted_node = current.next
                if current.next.next != self.head:
                    current.next.next.prev = current
                else:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return deleted_node
            current = current.next

        return None

    def search(self, node: DNode):
        current = self.head
        while current:
            if current.data == node.data:
                return current  # Return the node object
            current = current.next
            if current == self.head:
                break
        return None  # Node not found

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print("List information:")
        print(f"List length: {self.size}")
        print("Sorted status: Sorted" if self.is_sorted() else "Sorted status: Not sorted")
        print("List content:")
        current = self.head
        while current:
            if current == self.head:
                print(f"{current.data} (head) <->", end=" ")
            elif current == self.tail:
                print(f"{current.data} (tail) <->", end=" ")
            else:
                print(f"{current.data} <->", end=" ")
            if current == self.tail:
                break
            current = current.next
        if self.head:
            print(f"{self.head.data} (head)")
        else:
            print("Empty list")




