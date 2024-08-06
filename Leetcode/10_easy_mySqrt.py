class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        end = x
        start = 1
        mid = x//2

        if mid**2 > x:
            end = mid
        else:
            start = mid

        print(start, mid, end)
            
        return

if __name__ == "__main__":
    x0 = 4
    x1 = 8
    print(Solution().mySqrt(x0))
    print(Solution().mySqrt(x1))
