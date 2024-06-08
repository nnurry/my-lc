from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left, right = 0, length - 1

        # Setup 2 pointers at 2 ends
        while left != right:
            two_sum = numbers[left] + numbers[right]
            if two_sum < target:
                # increase the sum
                left += 1
            elif two_sum > target:
                # decrease the sum
                right -= 1
            else:
                return [left+1, right+1]
        