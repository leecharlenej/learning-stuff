# -----------------------------------
# First attempt
# -----------------------------------

class Solution(object):
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digit_string = ''
        
        for i in digits:
            digit_string+=str(i)
            
        new_digit = int(digit_string) + 1

        answer = []

        for i in str(new_digit):
            answer.append(int(i))
        
        return answer
    
# -----------------------------------
# Second attempt: To try case by case.
# -----------------------------------


if __name__ == "__main__":
    #digits0 = [1,2,3]
    #digits1 = [4,3,2,1]
    #digits2 = [9]
    #digits3 = [0]
    digits4 = [1]
    #print(Solution().plusOne(digits0))
    #print(Solution().plusOne(digits1))
    #print(Solution().plusOne(digits2))
    #print(Solution().plusOne(digits3))
    print(Solution().plusOne(digits4))
