from nodes.d_node import DNode


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head if head else None
        self.size = 1 if head else 0

    def insert_head(self, node: DNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_tail(self, node: DNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
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
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = DoublyLinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            current.prev = None
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head
        self.tail = sorted_list.tail

    def sorted_insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        if not self.is_sorted():
            self.sort()

        current = self.head
        while current:
            if current.data > node.data:
                if current.prev is not None:
                    current.prev.next = node
                    node.prev = current.prev
                else:
                    self.head = node
                node.next = current
                current.prev = node
                break

            if current.next is None:
                current.next = node
                node.prev = current
                self.tail = node
                break

            current = current.next

    def delete_head(self):
        if self.head is None:
            return None

        deleted_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return deleted_node

    def delete_tail(self):
        if self.tail is None:
            return None

        deleted_node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return deleted_node

    def delete(self, node: DNode):
        if self.head is None:
            return None

        if self.head.data == node.data:
            return self.delete_head()

        current = self.head
        while current.next is not None:
            if current.next.data == node.data:
                deleted_node = current.next
                if current.next.next is not None:
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
        return None  # Node not found


    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Print(self):
        print(f"List length: {self.size}")
        print("List Sorted:", self.is_sorted())
        print("List content:")
        current = self.head
        while current is not None:
            if current == self.head:
                print(f"{current.data} (head) <->", end=" ")
            elif current == self.tail:
                print(f"{current.data} (tail)")
            else:
                print(f"{current.data} <->", end=" ")
            current = current.next

