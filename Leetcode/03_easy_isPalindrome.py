# -----------------------------------
# First attempt
# -----------------------------------

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = False
        string_x = str(x)
        reverse_string = string_x[::-1]

        if string_x == reverse_string:
            flag = True

        return flag


if __name__ == "__main__":
    x = -121
    result = Solution().isPalindrome(x)
    print(result)