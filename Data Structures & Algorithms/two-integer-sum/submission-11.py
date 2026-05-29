class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for i, num in enumerate(nums):

            m = target - num
            if(m in map):
                lst = [map[m], i]
                return lst

            map[num] = i 
        

            