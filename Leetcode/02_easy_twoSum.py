# -----------------------------------
# First attempt
# -----------------------------------

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(len(nums)):
                if i != j and nums[j] == complement:
                    return [i,j]
                
# -----------------------------------
# Second attempt
# -----------------------------------

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_set = set(nums)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_set:
                for j in range(len(nums)):
                    if i != j and nums[j] == complement:
                        return [i,j]
                


if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    
    # nums = [3,2,4]
    # target = 6

    nums = [3,3]
    target = 6

    result = Solution().twoSum(nums, target)
    print(result)