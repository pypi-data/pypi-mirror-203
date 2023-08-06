from linear.sll import SinglyLL
from nodes.s_node import SNode

class LLQueue(SinglyLL):
    def __init__(self, head=None):
        super().__init__(head)

    def enqueue(self, node: SNode):
        super().insert_tail(node)

    def dequeue(self):
        return super().delete_head()

    def front(self):
        return self.head

    def is_empty(self):
        return self.size == 0

    # Override any methods from SinglyLL that are not applicable to queues
    def insert_head(self, node: SNode):
        pass

    def insert(self, node: SNode, position: int):
        pass

    def sorted_insert(self, node: SNode):
        pass

    def search(self, node: SNode):
        pass

    def delete(self, node: SNode):
        pass

    def sort(self):
        pass

    def clear(self):
        super().clear()

    def Print(self):
        print(f"Queue size: {self.size}")
        print("Queue content:")
        current = self.head
        while current is not None:
            if current == self.head:
                print(f"{current.data} (front) ->", end=" ")
            elif current == self.tail:
                print(f"{current.data} (rear) ->", end=" ")
            else:
                print(f"{current.data} ->", end=" ")

            current = current.next
        print("End of queue")

