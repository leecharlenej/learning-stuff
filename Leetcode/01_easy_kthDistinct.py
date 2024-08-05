# -----------------------------------
# First attempt
# -----------------------------------
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = {}
        distinct_strings = []
        
        for i in arr:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
        print(count)
        
        for i in arr:
            if count[i] == 1:
                distinct_strings.append(i)
        
        return distinct_strings[k-1] if k <= len(distinct_strings) else ""
    

# -----------------------------------
# Based on given intuition
# -----------------------------------

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        distinct_strings = []
        
        for i in range(len(arr)):
            flag = True
            for j in range(len(arr)):
                if i != j and arr[i] == arr[j]:
                    # print(arr[i], arr[j])
                    flag = False

            if flag == True:
                distinct_strings.append(arr[i])

        # print(distinct_strings)

        return distinct_strings[k-1] if k <= len(distinct_strings) else ""


if __name__ == "__main__":
    arr = ["d","b","c","b","c","a"]
    k = 2

    # arr =["aaa","aa","a"]
    # k = 1
    result = Solution().kthDistinct(arr, k)
    print(result)
        