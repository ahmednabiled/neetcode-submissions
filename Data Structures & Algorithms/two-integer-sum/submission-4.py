class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            for j in range(len(nums)):
                if(i != j and nums[j] == m):
                    return [i, j]
                    

            