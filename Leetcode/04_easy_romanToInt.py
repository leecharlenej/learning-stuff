class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0

        roman_dict = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}
        
        length_s = len(s)
        # print(length_s)
        skip = False

        for i in range(length_s):
            if skip == True:
                skip = False
                continue

            elif i == length_s-1 and skip == False:
                answer += roman_dict[s[i]]

            elif s[i] == 'I' and s[i+1] == 'V':
                answer += 4
                skip = True

            elif s[i] == 'I' and s[i+1] == 'X':
                answer += 9
                skip = True
            
            elif s[i] == 'X' and s[i+1] == 'L':
                answer += 40
                skip = True

            elif s[i] == 'X' and s[i+1] == 'C':
                answer += 90
                skip = True

            elif s[i] == 'C' and s[i+1] == 'D':
                answer += 400
                skip = True

            elif s[i] == 'C' and s[i+1] == 'M':
                answer += 900
                skip = True

            else:
                answer += roman_dict[s[i]]
                skip = False
            
            #print(answer)
        
        return answer

if __name__ == "__main__":
    s1 = "III"
    s2 = "LVIII"
    s3 = "MCMXCIV"
    print(Solution().romanToInt(s1))
    print(Solution().romanToInt(s2))
    print(Solution().romanToInt(s3))