#custom exception handling
class LinkedListError(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Empty List")
            return
        
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def delete_n(self, n):
        if self.head is None:
            raise LinkedListError("List is empty, nothing to delete")
        if n < 1:
            raise LinkedListError("Position must be >= 1")
        current = self.head
        if n == 1:
            self.head = current.next
            return
        for i in range(1, n - 1):
            if current.next is None:
                raise LinkedListError(f"Position {n} is out of range")
            current = current.next        
        if current.next is None:
            raise LinkedListError(f"Position {n} is out of range")       
        current.next = current.next.next

main_list = LinkedList()

elements = ["Ten", 20, 30, 40, 50, 60]
for element in elements:
    main_list.insert(element)

print("Original List = ", end="")
main_list.display()

try:
    user = int(input("\nEnter position of node to delete: "))
    main_list.delete_n(user)
    print("\nDeleted element at position", user)
except ValueError:
    print("\nPlease enter a valid integer")
except LinkedListError as e:
    print(f"\nError: {e}")
except Exception as e:
    print(f"\nUnexpected error: {e}")
finally:
    print("\nNew List = ", end="")
    main_list.display()