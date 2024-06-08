# LRU CACHE
[Problem link](https://leetcode.com/problems/lru-cache/description/)

### Idea
- Linked list for O(1) append and pophead
- Doubly linked list for easy traversal
- Hash table for fast lookup of linked list node and available key-value pair
- On putting a key-value pair, append (if not exist) or reposition to the end of the linked list (if exist)
- If full capacity, pop leftmost (head) of linked list