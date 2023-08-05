from nodes.d_node import DNode
from linear import DoublyLinkedList


class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self, head=None):
        super().__init__(head)
        if head:
            self.head.prev = self.tail
            self.tail.next = self.head

    def is_sorted(self):
        if self.size < 2:
            return True
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if self.size < 2:
            return

        sorted_head = self.head
        unsorted_head = self.head.next
        sorted_head.next = sorted_head.prev = None
        sorted_size = 1

        while sorted_size < self.size:
            current = unsorted_head
            unsorted_head = unsorted_head.next
            current.next = current.prev = None

            if current.data <= sorted_head.data:
                current.next = sorted_head
                sorted_head.prev = current
                sorted_head = current
            else:
                sorted_tail = sorted_head
                while sorted_tail.next and sorted_tail.next.data < current.data:
                    sorted_tail = sorted_tail.next

                if sorted_tail.next:
                    current.next = sorted_tail.next
                    sorted_tail.next.prev = current
                else:
                    current.next = None
                current.prev = sorted_tail
                sorted_tail.next = current

            sorted_size += 1

        self.head = sorted_head
        self.tail = self.head
        while self.tail.next:
            self.tail = self.tail.next

        # Update circular links
        self.head.prev = self.tail
        self.tail.next = self.head

    def sorted_insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = node
            node.next = node
            self.size += 1
            return

        if not self.is_sorted():
            self.sort()

        current = self.head
        for _ in range(self.size):
            if current.data >= node.data:
                if current.prev is not None:
                    current.prev.next = node
                    node.prev = current.prev
                else:
                    self.head = node
                node.next = current
                current.prev = node
                self.size += 1
                break

            if current.next == self.head:
                current.next = node
                node.prev = current
                self.tail = node
                self.size += 1
                break

            current = current.next

        # Update the circular links
        self.head.prev = self.tail
        self.tail.next = self.head




    def search(self, node: DNode):
        current = self.head
        while current:
            if current.data == node.data:
                return current  # Return the node object
            current = current.next
            if current == self.head:
                break
        return None  # Node not found

    def insert_head(self, node: DNode):
        super().insert_head(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def insert_tail(self, node: DNode):
        super().insert_tail(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def insert(self, node: DNode, position: int):
        super().insert(node, position)
        self.head.prev = self.tail
        self.tail.next = self.head

    def delete_head(self):
        deleted_node = super().delete_head()
        if self.head:
            self.head.prev = self.tail
            self.tail.next = self.head
        return deleted_node

    def delete_tail(self):
        deleted_node = super().delete_tail()
        if self.tail:
            self.head.prev = self.tail
            self.tail.next = self.head
        return deleted_node

    def delete(self, node: DNode):
        deleted_node = super().delete(node)
        if self.head and self.tail:
            self.head.prev = self.tail
            self.tail.next = self.head
        return deleted_node

    def clear(self):
        super().clear()
        self.head = None
        self.tail = None

    def Print(self):
        print(f"List length: {self.size}")
        print("List content:")
        #print("Is sorted", self.is_sorted())
        current = self.head
        for _ in range(self.size):
            if current == self.head:
                print(f"{current.data} (head) <->", end=" ")
            elif current == self.tail:
                print(f"{current.data} (tail)")
            else:
                print(f"{current.data} <->", end=" ")
            current = current.next

