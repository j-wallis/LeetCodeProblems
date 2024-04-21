class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make a hashmap of every value before current being checked
        map1 = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in map1:
                return [map1[difference],i]
            map1[n] = i
        return
        
