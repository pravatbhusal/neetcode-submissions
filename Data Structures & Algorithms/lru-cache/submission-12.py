class Node:
    def __init__(self, key):
        self.key = key
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
    end of the list. This must be done for both get() and put() operations. This is only worst-case O(N).
    """

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        if key in self.cache:
            # used key, so remove older ref and add new ref
            self.remove_list_key(key)
            self.add_list_key(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:   
        if key in self.cache:
            # used key, so remove older ref
            self.remove_list_key(key)

        # add key
        self.add_list_key(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # exceeds capacity, evict LRU
            self.evict()

    def evict(self):
        # delink head, which is the LRU
        lru = self.head.key
        if self.tail == self.head:
            # edge case, only 1 item in linked list
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
        
        # remove from cache
        del self.cache[lru]

    def remove_list_key(self, key):
        if not self.head:
            return

        if self.head.key == key:
            # remove head
            self.head = self.head.next

            # remove tail too if head no longer exists
            if not self.head:
                self.tail = None
            return

        # find the key in list
        cur = self.head
        while cur.next and cur.next.key != key:
            cur = cur.next

        # delink key
        if cur.next == self.tail:
            # remove the old tail
            self.tail = cur
        else:
            # simple delink
            cur.next = cur.next.next

    def add_list_key(self, key):
        if not self.head:
            # initialize
            self.init_list(key)
            return

        node = Node(key)
        self.tail.next = node
        self.tail = node

    def init_list(self, key):
        head = Node(key)
        self.head = head
        self.tail = head
        
