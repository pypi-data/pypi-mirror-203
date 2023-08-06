'''
Dnode class represents a double node in a double-linked list.
Has three attributes...
'data'
'prev'
'next'

'''


class DNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
