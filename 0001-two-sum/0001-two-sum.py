class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a map for nums[i] : i
        temp = {}
        for i, n in enumerate(nums):
            #calculate difference b/w target and current
            diff = target - n
            if diff in temp:
                return [temp[diff], i]
            temp[n] = i
        return