class ListNode:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    head = None
    tail = None

    def push(self, value):
        if self.tail is None:
            node = ListNode(value, None, None)
            self.tail = node
            self.head = node
        else:
            node = ListNode(value, self.tail, None)
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self.tail is None:
            return None
        result = self.tail.value
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return result

    def shift(self, value):
        if self.head is None:
            node = ListNode(value, None, None)
            self.head = node
            self.tail = node
        else:
            node = ListNode(value, None, self.head)
            self.head.prev = node
            self.head = node

    def unshift(self):
        if self.head is None:
            return None
        result = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return result

    def head_to_tail_iterator(self):
        current_position = self.head
        while current_position is not None:
            yield current_position.value
            current_position = current_position.next

    def tail_to_head_iterator(self):
        current_position = self.tail
        while current_position is not None:
            yield current_position.value
            current_position = current_position.prev



lst = DoublyLinkedList()
lst.shift("Ехал")
lst.shift("Грека")
lst.shift("через")
lst.shift("реку")
print(list(lst.head_to_tail_iterator()))
print(list(lst.tail_to_head_iterator()))
print(lst.unshift())
print(lst.pop())
print(lst.pop())

