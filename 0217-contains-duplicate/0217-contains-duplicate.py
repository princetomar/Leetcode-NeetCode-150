class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a hashset
        val = set()
        # iterate over nums
        for i in nums:
            if i in val:
                return True
            val.add(i)

        return False
        