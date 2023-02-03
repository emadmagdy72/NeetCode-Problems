class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] != ' ' :
                count += 1
            elif count > 0 :
                break
        return count
    