class Node:
    """ Represents one node of a linked list"""

    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    """Singly Linked List Implementation"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _create_first_node(self, value):
        self.head = Node(value, None)
        self.tail = self.head

    # Time complexity = O(1)
    def prepend(self, value):
        """insert item at index 0"""
        # for first item only
        if self.length == 0:
            self._create_first_node(value)
        else:
            self.head = Node(value, self.head)
        self.length += 1

    # Time complexity = O(1)
    def append(self, value):
        """insert item to end of linked list"""
        new_node = Node(value, None)
        # for first item only
        if self.length == 0:
            self._create_first_node(value)
        else:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next
        self.length += 1

    # Used in insert and delete to travese to index
    def _traverse_to_index(self, index):
        """traverses to find the node at the given index"""
        i = 0
        current = self.head
        while i < index-1:
            current = current.next
            i += 1
        return current

    # Time complexity = O(n)
    def insert(self, index, value):
        """insert item to given index"""
        # --- checking cornor cases ---
        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")
        elif index == self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            current = self._traverse_to_index(index)
            new_node = Node(value, current.next)
            current.next = new_node
        self.length += 1

    # Time complexity = O(n)
    def delete(self, index):
        """delete item at given index"""
        # --- checking cornor cases ---
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        elif index == 0:
            unwanted_node = self.head
            self.head = self.head.next
            del unwanted_node
        else:
            current = self._traverse_to_index(index)
            unwanted_node = current.next
            current.next = unwanted_node.next
            del unwanted_node
        self.length -= 1

    # Time complexity = O(n) | (just for visulization)
    def print(self):
        """prints linked list"""
        print("Head:",self.head.value, "|","Tail:",self.tail.value)
        current = self.head
        while current != None:
            print(current.value, "--> ", end="")
            current = current.next
        print(None)

    # Time complexity = O(n)
    def reverse(self):
        """reverses the linked list"""
        if self.length > 1:
            first = self.head
            second = first.next
            while second:
                third = second.next
                second.next = first
                first = second
                second = third
            self.tail = self.head
            self.tail.next = None
            self.head = first


# --- Comment these out --- #

# # Creating new linked list
# linked_list = LinkedList()
#
# # Prepending items
# linked_list.prepend(15)
# linked_list.prepend(20)
# linked_list.prepend(25)
# linked_list.prepend(45)
#
# # Appending items
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
#
# # Printing linked list
# linked_list.print()
#
# # Insert
# linked_list.insert(2,100)
# linked_list.insert(0,5)
# linked_list.print()
#
# # Delete
# linked_list.delete(2)
# linked_list.delete(0)
# linked_list.print()
#
# # Reverse
# linked_list.reverse()
# linked_list.print()
