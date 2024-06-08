from typing import Optional, List

class LinkedListNode:
    """Simple 2-way linked list node with key-value as data
    """
    def __init__(
            self, 
            key: int, 
            value: int, 
            prev=None, 
            next=None
        ) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
    
    def __str__(self) -> str:
        return f"node({self.key},{self.value})"

class LinkedList:
    """Basic linked list comprised of 2-way nodes and head/tail pointers 
    """
    def __init__(self) -> None:
        """Constructor of linked list 
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        temp = self.head
        nodes = []
        while temp:
            nodes.append(f"({temp.key},{temp.value})")
            temp = temp.next
        str_nodes = "<->".join([node for node in nodes])
        return f"head={self.head};tail={self.tail};length={self.length};{str_nodes}"

    def append(self, key: int, value: int) -> bool:
        # Append new node to tail
        new_node = LinkedListNode(key, value)
        if not self.length:
            # Have no element -> init new node -> set both head & tail to it
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

        self.length += 1

        return True

    def get_node(self, key) -> LinkedListNode:
        temp = self.tail
        if temp.key == key:
            return temp

        temp = self.head
        if temp.key == key:
            return temp

        while temp.key != key:
            temp = temp.next
        
        return temp
    
    def pop_key(self, key) -> Optional[LinkedListNode]:
        if not self.length:
            # Got no element -> no popping
            return None
        
        node = self.get_node(key)

        if node == self.head:
            return self.pop_head()
        
        if node == self.tail:
            return self.pop_tail()
        
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        node.prev = None
        node.next = None

        self.length -= 1

        return node

    def pop_tail(self) -> LinkedListNode:
        node = self.tail
        self.tail = self.tail.prev
        node.prev = None
        self.length -= 1

        return node

    def pop_head(self) -> LinkedListNode:
        node = self.head
        self.head = self.head.next
        node.next = None
        self.length -= 1

        return node
    
    def reorder(self, key):
        node = self.pop_key(key)

        if node:
            self.append(node.key, node.value)
            node = None
    
    def update(self, key, value):
        node = self.pop_key(key)

        if node:
            self.append(node.key, value)
            node = None

class LRUCache:
    """Basic LRU cache with 1-level linked list and hashmap for fast-retrieval
    """
    def __init__(self, capacity: int):
        """Constructor of basic LRU cache

        Args:
            capacity (int): Capacity of LRU cache, once about to overcap, remove the oldest node from cache
        """
        self.capacity = capacity
        self.hashmap = {}
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        """Retrieve the value given node's key, return -1 if not exist, otherwise an int

        Args:
            key (int): Key of to-be-retrieved node

        Returns:
            int: Value of that node
        """
        if key not in self.hashmap:
            return -1
        
        self.linked_list.reorder(key)
        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        """Put new key-value into LRU cache if not exist, otherwise update

        Args:
            key (int): Key of the node
            value (int): Value of the node
        """
        if key in self.hashmap:
            # Update and reorder
            self.linked_list.update(key, value)
        else:
            # Add
            if self.linked_list.length == self.capacity:
                # trunc
                old_head = self.linked_list.pop_head()
                self.hashmap.pop(old_head.key)

            self.linked_list.append(key, value)

        self.hashmap[key] = value

    def __str__(self) -> str:
        return f"hashmap={self.hashmap};linkedlist={self.linked_list}"


########################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################

def test_exec(op: str, param: List[int], lru: Optional[LRUCache]):
    exec_str = f"{op.upper()} {param}"
    print(exec_str)
    if op == "LRUCache":
        return LRUCache(*param)
    if op == "put":
        return lru.put(*param)
    if op == "get":
        return lru.get(*param)
    
    raise Exception(f"Incorrect instruction: {exec_str}")

testcases = [
    (
        ["LRUCache", "put","put","get","put","get","put","get","get","get"],
        [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]],
    ),
    (
        ["LRUCache","put","get","put","get","get"],
        [[1],[2,1],[2],[3,2],[2],[3]],
    ),
    (
        ["LRUCache","put","put","put","put","get","get"],
        [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]],
    ),
    (
        ["LRUCache","get","put","get","put","put","get","get"],
        [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]],
    ),
    (
        ["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"],
        [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]],
    ),
]

lru = None

for idx, testcase in enumerate(testcases[:]):
    print(f"Executing testcase {idx+1}")
    testcase_output = []
    for op, param in zip(*testcase):
        output = test_exec(op, param, lru)
        testcase_output.append(output)
        if isinstance(output, LRUCache):
            lru = output

        print(lru)

    print("Testcase output:", testcase_output)
    print("-"*100)
    print("-"*100)
