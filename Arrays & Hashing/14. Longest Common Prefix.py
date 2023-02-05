class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        out = ""
        for i in range(len(strs[0])):
            for st in strs:
                if (i == len(st)) or (st[i] != strs[0][i]) :
                    return out
            out += strs[0][i]
        return out