class Node:
    def __init__(self, key, val=0, next = None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.cache = {}

        self.cap = capacity

    def addNode(self, node : Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        
    def delNode(self, node : Node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delNode(node)
            self.addNode(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delNode(self.cache[key])
        self.cache[key] = Node(key, value)
        self.addNode(self.cache[key])

        if len(self.cache) > self.cap:
            lru_node = self.tail.prev
            lru_key = lru_node.key
            self.delNode(lru_node)
            del self.cache[lru_key]

        
        
