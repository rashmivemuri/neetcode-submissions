class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in set(nums[i+1:]):

                return [i,nums.index(target-nums[i],i+1)]
                break
            
        else:
            return 0

        