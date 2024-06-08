# 3Sum

[Problem link](https://leetcode.com/problems/3sum)

### IDEA:
1) Hashmap: 
- Convert to 2-sum problem with additional number on the left side of 2-sum window
2) 2-pointer:
- Sort the input array and convert into [2-sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)
- Upon finding appropriate 3-sum, squeeze left-side window and skip all duplicate element