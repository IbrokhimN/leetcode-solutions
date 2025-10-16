class Solution(object):
    def addBinary(self, a, b):
        abin = int(a, 2)
        bbin = int(b, 2)
        return bin(abin+bbin)[2:]
