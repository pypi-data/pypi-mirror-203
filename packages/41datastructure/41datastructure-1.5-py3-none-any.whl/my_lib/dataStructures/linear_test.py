
from nodes.s_node import SNode
from nodes.d_node import DNode


from linear.sll import SinglyLL
from linear.dll import DoublyLinkedList
from linear.csll import CircularSinglyLinkedList
from linear.cdll import CircularDoublyLinkedList
from linear.stack_ll import LLStack
from linear.queue_ll import LLQueue


def test_sll():
    print("Testing Singly Linked List")

    print("\nCreating a new Singly Linked List")
    sll = SinglyLL()
    sll.Print()

    print("\nInserting nodes at the head")
    sll.insert_head(SNode(3))
    sll.insert_head(SNode(2))
    sll.insert_head(SNode(1))
    sll.Print()

    print("\nInserting nodes at the tail")
    sll.insert_tail(SNode(4))
    sll.insert_tail(SNode(5))
    sll.Print()

    print("\nInserting nodes at specified positions")
    sll.insert(SNode(0), 0)
    sll.insert(SNode(3.5), 4)
    sll.insert(SNode(6), 10)
    sll.insert(SNode(100), -1)
    sll.Print()

    print("\nSearching for nodes")
    search_node = sll.search(SNode(3))
    if search_node:
        print("Node found:", search_node.data)
    else:
        print("Node not found")
    
    print("\nTesting is_sorted")
    sll.insert_head(SNode(100))
    sll.Print()

    print("\nInserting nodes into a sorted list")
    sll.clear()
    sll.sorted_insert(SNode(5))
    sll.sorted_insert(SNode(3))
    sll.sorted_insert(SNode(1))
    sll.sorted_insert(SNode(4))
    sll.sorted_insert(SNode(2))
    sll.Print()

    print("\nTesting sorted_insert with new nodes")
    sll.clear()
    nodes = [SNode(3), SNode(1), SNode(4), SNode(2), SNode(5)]
    for node in nodes:
        sll.sorted_insert(node)
    sll.Print()

    print("\nDeleting head node")
    sll.delete_head()
    sll.Print()

    print("\nDeleting tail node")
    sll.delete_tail()
    sll.Print()

    print("\nDeleting specific node")
    sll.delete(SNode(3))
    sll.Print()

    print("\nSorting the list")
    sll.insert_head(SNode(6))
    sll.insert_head(SNode(8))
    sll.sort()
    sll.Print()

    print("\nClearing the list")
    sll.clear()
    sll.Print()



def test_dll():
    print("Testing Doubly linked list\n")

    # Create an empty doubly linked list
    dll = DoublyLinkedList()
    dll.Print()

    # Insert nodes at the head
    print("\nInserting nodes at the head")
    dll.insert_head(DNode(3))
    dll.insert_head(DNode(2))
    dll.insert_head(DNode(1))
    dll.Print()

    # Insert nodes at the tail
    print("\nInserting nodes at the tail")
    dll.insert_tail(DNode(7))
    dll.insert_tail(DNode(5))
    dll.Print()

    # Insert nodes at specific positions
    print("\nInserting nodes at specific positions")
    dll.insert(DNode(0), 0)
    dll.insert(DNode(3.5), 4)
    dll.insert(DNode(6), 7)
    dll.insert(DNode(4), 3)
    dll.Print()
    print("\n")
    ## Sort
    # sorted_insert
    dll_sort = DoublyLinkedList()

    #insert nodes with random data
    nodes = [DNode(3), DNode(1), DNode(4), DNode(2), DNode(5)]
    for node in nodes:
        dll_sort.insert_tail(node)
    

    print("Original list:")
    dll_sort.Print()

    #test sort method
    dll_sort.sort()
    print("Sorted list using sort():")
    dll_sort.Print()

    print("\n\n\n")

    #test sorted_insert method
    new_node = DNode(3)
    dll_sort.sorted_insert(new_node)
    print(f"List after inserting {new_node.data} using sorted_insert():")
    dll_sort.Print()

    
    #Test sorted_insert with a new list...
    dll2 = DoublyLinkedList()
    nodes2 = [DNode(10), DNode(5), DNode(8), DNode(2), DNode(12)]
    for node in nodes2:
        dll2.sorted_insert(node)

    print("New list created using sorted_insert() for each node:")
    dll2.Print()    

    ## Search
    # Search for nodes in the list
    search_node = DNode(4)
    found_node = dll.search(search_node)

    if found_node:
        print(f"Node found: {found_node.data}")
    else:
        print("Node not found")

    # Search for a node not in the list
    search_node = DNode(99)
    found_node = dll.search(search_node)
    if found_node:
        print(f"Node found: {found_node.data}")
    else:
        print("Node not found")

    ## Delete
    # Delete nodes
    print("\nDeleting nodes")
    dll.delete(DNode(0))
    dll.delete(DNode(6))
    dll.Print()

    # Delete head and tail nodes
    print("\nDeleting head and tail nodes")
    dll.delete_head()
    dll.delete_tail()
    dll.Print()

    # Clear the list
    print("\nClearing the list")
    dll.clear()
    dll.Print()

def test_csll():
    print("Testing Circular Singly Linked List:")
    
    # Test Insert
    cll = CircularSinglyLinkedList()
    nodes = [SNode(3), SNode(1), SNode(4), SNode(2), SNode(5)]
    for i, node in enumerate(nodes):
        cll.insert_tail(node)
        print(f"Inserting {node.data} at the tail:")
        cll.Print()

    
    # Test Search
    print("\nTesting search:")
    target_node = SNode(4)
    result = cll.search(target_node)
    if result:
        print(f"Found node with data {result.data}")
    else:
        print("Node not found")

    # Test Delete
    print("\nTesting delete:")
    cll.delete(SNode(4))
    cll.Print()

    # Test insert_head
    print("\nTesting Insert Head")
    cll.insert_head(SNode(10))
    cll.Print()

    # Test Sorted Insert
    print("\nTesting sorted insert:")
    cll.sorted_insert(SNode(3))
    cll.Print()

    # Test Sorted Insert with a new list called cll_sorted
    print("\nTesting sorted_insert with a new list")
    cll_sorted = CircularSinglyLinkedList()
    nodes = [SNode(5), SNode(3), SNode(8), SNode(1), SNode(2), SNode(7), SNode(4), SNode(6)]
    for node in nodes:
        cll_sorted.sorted_insert(node)
    
    cll_sorted.Print()

    # Test Sort
    print("\nTesting sort:")
    cll.insert_head(SNode(10.5))
    cll.sort()
    cll.Print()

    # Test Delete Head
    print("\nTesting delete head:")
    cll.delete_head()
    cll.Print()


    # Test Delete Tail
    print("\nTesting delete tail:")
    cll.delete_tail()
    cll.Print()


    # Test Clear
    print("\nTesting clear:")
    cll.clear()
    cll.Print()

def test_cdll():
    print("Testing Circular Doubly linked list\n")

    # Create an empty circular doubly linked list
    cdll = CircularDoublyLinkedList()
    cdll.Print()

    # Insert nodes at the head
    print("\nInserting nodes at the head")
    cdll.insert_head(DNode(3))
    cdll.insert_head(DNode(2))
    cdll.insert_head(DNode(1))
    cdll.Print()

    # Insert nodes at the tail
    print("\nInserting nodes at the tail")
    cdll.insert_tail(DNode(7))
    cdll.insert_tail(DNode(5))
    cdll.Print()

    # Insert nodes at specific positions
    print("\nInserting nodes at specific positions")
    cdll.insert(DNode(0), 0)
    cdll.insert(DNode(3.5), 4)
    cdll.insert(DNode(6), 7)
    cdll.insert(DNode(4), 3)
    cdll.Print()
    print("\n")
    
    ## Sort
    # sorted_insert
    cdll_sort = CircularDoublyLinkedList()

    #insert nodes with random data
    nodes = [DNode(3), DNode(1), DNode(4), DNode(2), DNode(5)]
    for node in nodes:
        cdll_sort.insert_tail(node)
    
    print("Original list:")
    cdll_sort.Print()

    #test sort method
    cdll_sort.sort()
    print("Sorted list using sort():")
    cdll_sort.Print()

    print("\n\n\n")

    #test sorted_insert method
    new_node = DNode(3)
    cdll_sort.sorted_insert(new_node)
    print(f"List after inserting {new_node.data} using sorted_insert():")
    cdll_sort.Print()

    #Test sorted_insert with a new list...
    cdll2 = CircularDoublyLinkedList()
    nodes2 = [DNode(10), DNode(5), DNode(8), DNode(2), DNode(12)]
    for node in nodes2:
        cdll2.sorted_insert(node)

    print("\nNew list created using sorted_insert() for each node:")
    cdll2.Print()    

    ## Search
    # Search for nodes in the list
    search_node = DNode(4)
    found_node = cdll.search(search_node)

    if found_node:
        print(f"Node found: {found_node.data}")
    else:
        print("Node not found")

    # Search for a node not in the list
    search_node = DNode(99)
    found_node = cdll.search(search_node)
    if found_node:
        print(f"Node found: {found_node.data}")
    else:
        print("Node not found")

    ## Delete
    # Delete nodes
    print("\nDeleting nodes")
    cdll.delete(DNode(0))
    cdll.delete(DNode(6))
    cdll.Print()

    # Delete head and tail nodes
    print("\nDeleting head and tail nodes")
    cdll.delete_head()
    cdll.delete_tail()
    cdll.Print()

    # Clear the list
    print("\nClearing the list")
    cdll.clear()
    cdll.Print()

def test_llstack():
    print("Testing LLStack\n")

    # Create an empty stack
    stack = LLStack()
    stack.Print()

    # Push nodes onto the stack
    print("\nPushing nodes onto the stack")
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.Print()

    # Pop nodes from the stack
    print("\nPopping nodes from the stack")
    popped_node = stack.pop()
    print(f"Popped node: {popped_node.data}")
    popped_node = stack.pop()
    print(f"Popped node: {popped_node.data}")
    stack.Print()

    # Peek at the top of the stack
    print("\nPeeking at the top of the stack")
    top_node = stack.peek()
    print(f"Top node: {top_node.data}")
    stack.Print()

    # Check if the stack is empty
    print("\nChecking if the stack is empty")
    print(f"Stack empty? {stack.is_empty()}")
    stack.pop()
    print("Popped last node")
    print(f"Stack empty? {stack.is_empty()}")
    stack.Print()

def test_llqueue():
    print("Testing LLQueue")
    queue = LLQueue()

    print("\nInitial queue")
    queue.Print()

    print("\nEnqueueing nodes")
    queue.enqueue(SNode(1))
    queue.enqueue(SNode(2))
    queue.enqueue(SNode(3))
    queue.Print()

    print("\nDequeueing nodes")
    dequeued_node = queue.dequeue()
    print(f"Dequeued node: {dequeued_node.data}")
    dequeued_node = queue.dequeue()
    print(f"Dequeued node: {dequeued_node.data}")
    queue.Print()

    print("\nChecking the front of the queue")
    front_node = queue.front()
    print(f"Front node: {front_node.data}")
    queue.Print()

    print("\nChecking if the queue is empty")
    print(f"Queue empty? {queue.is_empty()}")
    print("Dequeueing last node")
    dequeued_node = queue.dequeue()
    print(f"Dequeued node: {dequeued_node.data}")
    print(f"Queue empty? {queue.is_empty()}")
    queue.Print()



def main():
    test_sll()
    test_dll()
    test_csll()
    test_cdll()
    test_llstack()
    test_llqueue()

    pass

if __name__ == "__main__":
    main()




