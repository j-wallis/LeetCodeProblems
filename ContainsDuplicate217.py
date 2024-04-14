class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create hash set to hold numbers being checked
        checknumbers = set()

        #iterate through array and add to hashset using if statement to detect if next number is unique
        for num in nums:
            if num in checknumbers:
                return True
            checknumbers.add(num)
        return False
