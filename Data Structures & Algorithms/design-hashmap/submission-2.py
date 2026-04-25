class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.cap = 1000
        self.map = [None] * self.cap

    def hash(self, key):
        return key % self.cap

    def put(self, key, value):
        idx = self.hash(key)
        if not self.map[idx]:
            self.map[idx] = Node(key, value)
            return

        curr = self.map[idx]
        while True:
            if curr.key == key:
                curr.value = value
                return
            if not curr.next:
                break
            curr = curr.next

        curr.next = Node(key, value)

    def get(self, key):
        idx = self.hash(key)
        curr = self.map[idx]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key):
        idx = self.hash(key)
        curr = self.map[idx]

        if not curr:
            return

        if curr.key == key:
            self.map[idx] = curr.next
            return

        prev = curr
        curr = curr.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next