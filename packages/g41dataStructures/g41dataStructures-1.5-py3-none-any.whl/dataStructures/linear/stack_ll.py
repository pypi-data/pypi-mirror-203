from nodes.s_node import SNode
from linear.sll import SinglyLL

class LLStack(SinglyLL):
    def __init__(self):
        super().__init__()

    # Wrapper for the insert_head method with proper naming convention
    def push(self, node: SNode):
        super().insert_head(node)

    # Wrapper for the delete_head method with proper naming convention
    def pop(self):
        return super().delete_head()

    # Wrapper for the head method with proper naming convention
    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.head

    # Override detrimental methods with empty body methods
    def insert_tail(self, node: SNode):
        pass

    def insert(self, node: SNode, position: int):
        pass

    def sorted_insert(self, node: SNode):
        pass

    def sort(self):
        pass

    
    def delete_tail(self):
        pass

    def delete(self, node: SNode):
        pass

    def clear(self):
        pass

    def search(self, node: SNode):
        pass

    # Helper function to check if the stack is empty
    def is_empty(self):
        return self.head is None

    # Override Print method to display stack-specific information
    def Print(self):
        print(f"Stack size: {self.size}")
        print("Stack content:")

        current = self.head
        while current is not None:
            if current == self.head:
                print(f"{current.data} (top) ->", end=" ")
            elif current == self.tail:
                print(f"{current.data} (bottom) ->", end=" ")
            else:
                print(f"{current.data} ->", end=" ")

            current = current.next
        print("End of stack")
