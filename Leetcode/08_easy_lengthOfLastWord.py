class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split(" ")
        flag = False

        while flag == False:
            x = word_list.pop()
            if len(x) == 0:
                continue
            else:
                break

        return len(x)

if __name__ == "__main__":
    s0 = "Hello World"
    s1 = "   fly me   to   the moon  "
    s2 = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s0))
    print(Solution().lengthOfLastWord(s1))
    print(Solution().lengthOfLastWord(s2))
