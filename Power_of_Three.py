import math

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        logn = math.log(n, 3)
        return abs(round(logn) - logn) < 1e-10
