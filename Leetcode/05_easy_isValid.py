class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_dict = {'(': ')',
                         '{': '}',
                         '[': ']'}
        
        stack = []

        for i in s:
            # print('i:', i)
            if i in brackets_dict:
                stack.append(i)
            else:
                if stack == []:
                    return False
                elif brackets_dict[stack[-1]] == i:
                    stack.pop()
                else:
                    return False

        return True if stack == [] else False        

if __name__ == "__main__":
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    print(Solution().isValid(s1))
    print(Solution().isValid(s2))
    print(Solution().isValid(s3))
