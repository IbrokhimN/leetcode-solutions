class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        last = 0
        for i in range(len(s)):
            if s[i] == " ":
                last = i
        if last == 0:
            return len(s)
        else:
            return len(s) - last - 1
