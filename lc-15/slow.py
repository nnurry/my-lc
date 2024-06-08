from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        lefted = set()
        triplets = set()
        # [-1,0,1,2,-1,-4]
        for left in range(length - 2):
            left_ele = nums[left]
            hashmap = {}
            if left_ele not in lefted:
                for curr in range(left + 1, length):
                    curr_ele = nums[curr]
                    two_sum = left_ele + curr_ele
                    diff = -two_sum
                    if curr_ele in hashmap:
                        # perhaps there is a 3rd-element that is suitable for this
                        mid_ele_idx = hashmap[curr_ele]
                        mid_ele = nums[mid_ele_idx]
                        triplet = tuple(sorted((left_ele, mid_ele, curr_ele)))
                        triplets.add(triplet)

                    else:
                        # add to the hashmap and continue
                        hashmap[diff] = curr
                lefted.add(left_ele)

        return [list(triplet) for triplet in triplets]
