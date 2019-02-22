"""
This is a simple usage of linkedlist.
"""
class ListNode(object):
    """
    >>> ListNode(x)
    x
    >>> ListNode(3)
    3
    """
    def __init__(self, x):
        self.val = x
        self.next = None

class ReLinkList:
    """
    >>> test = ReLinkList()
    None
    >>> test.add_node(3)
    add 3
    >>> test.show_list()
    3
    """
    def __init__(self):
        self.cur_node = None
    def add_node(self, x):
        new_node = ListNode(x)
        new_node.next = self.cur_node
        self.cur_node = new_node

    def show_list(self):
        node = self.cur_node
        while node:
            print node.val
            node = node.next

class LinkList:
    """
    >>> test = ReLinkList()
    None
    >>> test.add_node(3)
    add 3
    >>> test.show_list()
    3
    """
    def __init__(self):
        self.first = None
        self.last = None
    def add_node(self, x):
        if self.first == None:
            self.first = ListNode(x)
            self.last = self.first
        elif self.first == self.last:
            self.last = ListNode(x)
            self.first.next = self.last
        else:
            current = ListNode(x)
            self.last.next = current
            self.last = current
    def show_list(self):
        if self.first != None:
            current = self.first
            while current:
                print current.val
                current = current.next


if __name__ == '__main__':
    """
    print
    3
    2
    1
    """
    FIRSTTEST = ReLinkList()
    FIRSTTEST.add_node(1)
    FIRSTTEST.add_node(2)
    FIRSTTEST.add_node(3)
    FIRSTTEST.show_list()
    """
    print
    1
    2
    3
    """
    SECONDTEST = LinkList()
    SECONDTEST.add_node(1)
    SECONDTEST.add_node(2)
    SECONDTEST.add_node(3)
    SECONDTEST.show_list()

