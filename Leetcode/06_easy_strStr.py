class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        
        return -1

if __name__ == "__main__":
    haystack1, needle1 = 'sadbutsad', 'sad'
    haystack2, needle2 = 'leetcode', 'leeto'
    print(Solution().strStr(haystack1, needle1))
    print(Solution().strStr(haystack2, needle2))

