class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds, dt = {}, {}

        for letter in s:
            ds[letter] = 1 + ds.get(letter,0)
        
        for letter in t:
            dt[letter] = 1 + dt.get(letter,0)

        return ds == dt