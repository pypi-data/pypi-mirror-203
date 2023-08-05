from nodes.s_node import SNode


class SinglyLL:
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0


    def insert_head(self, node: SNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert_tail(self, node: SNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node: SNode, position: int):
        if position <= 0:
            self.insert_head(node)
            return
        if position >= self.size:
            self.insert_tail(node)
            return

        current = self.head
        prev = None
        count = 0
        while count < position and current:
            prev = current
            current = current.next
            count += 1

        node.next = current
        prev.next = node
        self.size += 1


    def sorted_insert(self, node: SNode):
        if not self.is_sorted():
            self.sort()
        if self.head is None:
            # If the list is empty, insert node as head
            self.head = node
            self.tail = node
            self.size += 1
            return

        if node.data < self.head.data:
            # If node is smaller than head, insert at head
            node.next = self.head
            self.head = node
            self.size += 1
            return

        current = self.head
        while current.next and current.next.data < node.data:
            # Traverse list until we find the correct insertion point
            current = current.next

        # Insert node after current node
        node.next = current.next
        current.next = node
        self.size += 1

        # Update tail node if necessary
        if node.next is None:
            self.tail = node

    def search(self, node: SNode):
        current = self.head
        position = 0
        while current:
            if current.data == node.data:
                return current  # Return the object
            current = current.next
        return None  # Node not found
    

    
    def delete_head(self):
        if self.head is None:
            return None  # List is already empty

        deleted_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None  # If the list is now empty, update the tail as well
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
        while current.next.next is not None:
            current = current.next

        deleted_node = current.next
        current.next = None
        self.tail = current
        self.size -= 1
        return deleted_node

    def delete(self, node: SNode):
        if self.head is None:
            print("List is empty")
            return None

        if self.head.data == node.data:
            deleted_node = self.head
            self.head = self.head.next
            self.size -= 1
            if self.head is None or self.head.next is None:
                self.tail = self.head
            return deleted_node

        current = self.head
        while current.next is not None:
            if current.next.data == node.data:
                deleted_node = current.next
                current.next = current.next.next
                self.size -= 1
                if current.next is None:
                    self.tail = current
                return deleted_node
            current = current.next

        print("Node not found in list")
        return None


    def sort(self):
        # Check if the linked list is empty or has only one node
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
                if tail is None:  # Update tail if this is the first node
                    tail = current
            else:
                runner = sorted_list
                while runner.next and runner.next.data < current.data:
                    runner = runner.next

                current.next = runner.next
                runner.next = current

                if runner.next.next is None:  # Update tail if this is the last node
                    tail = runner.next

            current = next_node

        self.head = sorted_list
        self.tail = tail


    def clear(self):
        # Set the head and tail nodes to None and reset the size of the list
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print(f"List length: {self.size}")
        print("Sorted status:", "Sorted" if self.is_sorted() else "Not sorted")

        print("List content:")
        current = self.head
        while current is not None:
            if current == self.head:
                print(f"{current.data} (head) ->", end=" ")
            elif current != self.tail:
                print(f"{current.data} ->", end=" ")
            else:
                print(f"{current.data} (tail)", end=" ")

            current = current.next
        print()





    # Helper functions
    def is_sorted(self):
        current = self.head
        count = 0
        max_count = self.size  # Maximum number of iterations
        while current and current.next and count < max_count:
            if current.data > current.next.data:
                return False
            current = current.next
            count += 1
        return True

