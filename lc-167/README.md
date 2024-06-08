# Two Sum II - Input Array Is Sorted

[Problem link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)

### IDEA
- Array is sorted -> the element is getting larger forward and smalled backward
- Given 2 pointers at both side, compare the sum with expected sum. 
- If less than -> left number is not big enough -> move the pointer to the right -> the sum gets bigger
- If greater than -> right number is not big enough -> move the pointer to the left -> the sum gets smaller
