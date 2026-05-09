import time

class BrowserHistory:
        def __init__(self):
            self.URL = None
            self.visit_time = time.time()
            self.mark_fl = bool()

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

        def insert_at_beginning(self, data):
            new_node = DoubleNode(data)
            if  not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.size += 1

        def insert_at_end(self, data):
            new_node = DoubleNode(data)
            if not self.tail:
                self.head = self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            self.size += 1

        def delete_at_beginning(self):

            if not self.head:
                return None

            data = self.head.data
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            else:
                self.tail = None

            self.size -= 1
            return data

        def delete_at_end(self):
            if not self.tail:
                return None

            data = self.tail.data
            self.tail = self.tail.prev

            if self.tail:
                self.tail.next = None
            else:
                self.head = None

            self.size -= 1
            return data

        def delete_by_value(self, value):
            current = self.head

            while current:

                if current.data == value:

                    if current.prev:
                        current.prev.next = current.next
                    else:
                        self.head = current.next

                    if current.next:
                        current.next.prev = current.prev
                    else:
                        self.tail = current.prev

                    self.size -= 1
                    return True
                current = current.next
            return False

        def display_forward(self):
            elements = []
            current = self.head
            while current:
                elements.append(str(current.data))
                current = current.next
            print(" ⇄ ".join(elements))

        def display_backward(self):
            elements = []
            current = self.tail
            while current:
                elements.append(str(current.data))
                current = current.prev
            print(" ⇄ ".join(elements))
