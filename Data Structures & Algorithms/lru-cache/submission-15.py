class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    O(1) average time, which arrays use O(1) average time for get() and put().
    The LRU cache will be initialized with capacity up to 100. But the actual key can be up to 1000.
    
    Best approach is using a dict to store the items for O(1) get and put.

    Next we need to know when to evict items from the cache.
    Problem says if new cache.put(key) exceds the capacity, we must evict least recently used key.

    We'd have check len(dict) on the put call. If len is greater than capacity, then we must evict the LRU.

    To find the LRU, create a doubly linked list where it adds a new node when an item is used.
    Then check the head of the node to find the LRU.

    Maintain the LRU linked list by removing node if the item is already cached. So that it's updated to the
    end of the list. This must be done for both get() and put() operations.

    With a doubly linked list and cache storing nodes, remove_list_node() is now
    true O(1) — no traversal needed. We get the node directly from the cache
    and use prev/next pointers to delink it instantly.

    get()  -> O(1): cache lookup + O(1) node removal + O(1) tail append
    put()  -> O(1): same as above + O(1) eviction (head.next reassignment)
    """

    def __init__(self, capacity: int):
        self.cache = dict() # key -> Node for O(1) lookup to delink
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        if key in self.cache:
            # used key, so remove older ref and add new ref
            node = self.cache[key]
            self.remove_list_node(node)
            self.append_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # used key, so remove older ref and update value
            node = self.cache[key]
            node.val = value
            self.remove_list_node(node)
            self.append_tail(node)
        else:
            # add key
            node = Node(key, value)
            self.cache[key] = node
            self.append_tail(node)

            if len(self.cache) > self.capacity:
                # exceeds capacity, evict LRU
                self.evict()

    def evict(self):
        # delink head, which is the LRU
        lru = self.head
        self.remove_list_node(lru)

        # remove from cache
        del self.cache[lru.key]

    def remove_list_node(self, node):
        prev, nxt = node.prev, node.next

        # re-link neighbors
        if prev:
            prev.next = nxt
        else:
            # node was head
            self.head = nxt

        if nxt:
            nxt.prev = prev
        else:
            # node was tail
            self.tail = prev

        node.prev = None
        node.next = None

    def append_tail(self, node):
        if not self.tail:
            # initialize
            self.head = node
            self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node