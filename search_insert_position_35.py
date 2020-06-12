#https://leetcode.com/problems/search-insert-position/
nums= [1,3,5,6]
target = 5
# Output: 2

class Solution:
    def searchInsert(self, nums: [], target: int) -> int:
        nums.append(target)
        # print(nums.index(target)) 
        return sorted(nums).index(target)

        