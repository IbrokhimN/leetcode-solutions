import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        
        divisors_sum = 1
        root = int(math.sqrt(num))
        
        for i in range(2, root + 1):
            if num % i == 0:
                divisors_sum += i
                pair = num // i
                if pair != i:
                    divisors_sum += pair
        
        return divisors_sum == num
