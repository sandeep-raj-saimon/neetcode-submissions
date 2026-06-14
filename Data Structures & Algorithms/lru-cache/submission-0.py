class Node:
    # we are using double linkedlist
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    # we need to have least recent node and most recent node to keep track
    # of least recent and most recently used key respectively.
    def __init__(self, capacity: int):
        self.capacity = capacity
        # this are dummy nodes which are acting as pointer
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.cache = {}
        # initially this nodes are connected to each other
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # prev node will point to node's next
        # node'next will point to node's prev
        # 4 pointers to change
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = node.next, prev

    def insert(self, node):
        # we need to add node at the end of list
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if self.cache.get(key) is None:
            return -1
        else:
            # we need the position of node to recently used
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # we need to update the cache
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            node = self.left.next
            self.remove(node)

            del self.cache[node.key]

        
