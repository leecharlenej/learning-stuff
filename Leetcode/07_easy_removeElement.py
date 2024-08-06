# -----------------------------------
# First attempt
# -----------------------------------

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        count = 0

        for i in range(length):
            if nums[i] == val:
                nums[i] = 51

            if nums[i] != 51:
                count +=1
        
        nums.sort()

        return count
    
# -----------------------------------
# Second attempt: To try Linked List.
# -----------------------------------

if __name__ == "__main__":
    nums1, val1 = [3,2,2,3], 3
    nums2, val2 = [0,1,2,2,3,0,4,2], 2
    print(Solution().removeElement(nums1, val1))
    print(Solution().removeElement(nums2, val2))


