from typing import List

class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        triplets = set()

        nums.sort()

        for base_idx, base_ele in enumerate(nums):
            if base_idx > 0 and base_ele == nums[base_idx - 1]:
                continue

            # base + 2sum with 2-ptr
            left_idx, right_idx = base_idx + 1, length - 1
            while left_idx < right_idx:
                three_sum = base_ele + nums[left_idx] + nums[right_idx]
                if three_sum > 0:
                    right_idx -= 1
                elif three_sum < 0:
                    left_idx += 1
                else:
                    triplet = (base_ele, nums[left_idx], nums[right_idx])
                    if triplet not in triplets:
                        triplets.add(triplet)
                    left_idx += 1
                    while nums[left_idx] == nums[left_idx] - 1 and left_idx < right_idx:
                        left_idx += 1

        return [list(triplet) for triplet in triplets]
            