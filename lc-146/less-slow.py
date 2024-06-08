from typing import Optional, List, Dict
class LinkedListNode:
    def __init__(
            self, 
            key: int, 
            value: int,
        ) -> None:
        self.key, self.value = key, value
        self.prev = self.next = None
    
    def __str__(self) -> str:
        return f"node({self.key},{self.value})"
    
class LinkedList:
    def __init__(self) -> None:
        self.lru: LinkedListNode = None
        self.mru: LinkedListNode = None

    def __str__(self) -> str:
        temp = self.lru
        nodes = []
        while temp:
            nodes.append(temp)
            temp = temp.next

        output_str = ""

        if nodes:
            output_str = "<->".join([
                str(node)
                for node in nodes
            ])
        
        return "[" + output_str + "]"

    def pop(self, node: LinkedListNode):
        if node == self.lru:
            # cut head and shift right
            self.lru = self.lru.next
            node.next = None

        elif node == self.mru:
            # cut tail and shift left
            self.mru = self.mru.prev
            node.prev = None
        else:
            # bridge 2 adjacent nodes
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

    def append(self, node: LinkedListNode):
        if self.lru is None:
            # empty head
            self.lru = self.mru = node
        else:
            self.mru.next = node
            node.prev = self.mru
            self.mru = self.mru.next

class LRUCache:
    def __init__(self, capacity: int):
        self.ll = LinkedList()
        self.cache: Dict[int, LinkedListNode] = {}
        self.capacity = capacity

    def __str__(self) -> str:
        return f"\t-ll={self.ll}\n\t-cache={list(self.cache.keys())}"

    def remove(self, node: LinkedListNode):
        self.ll.pop(node)

    def insert(self, node: LinkedListNode):
        self.ll.append(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value
            self.insert(self.cache[key])

        else:
            mru = LinkedListNode(key, value)
            if len(self.cache) == self.capacity:
                # remove -> insert
                lru = self.ll.lru
                # clear LRU
                self.cache.pop(lru.key)
                self.remove(lru)
                # add MRU
                self.insert(mru)
                self.cache[key] = mru
            else:
                # insert
                self.insert(mru)
                self.cache[key] = mru

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
