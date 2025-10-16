import math

class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        logn = math.log(n, 4)
        return logn.is_integer()
