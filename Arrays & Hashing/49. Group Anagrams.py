class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        lst = []
        for st in strs:
            st_sort = ''.join(sorted(st))

            if st_sort in dic:
                dic[st_sort].append(st)
            else:
                dic[st_sort] = []
                dic[st_sort].append(st)
        
        for key in dic:
            lst.append(dic[key])
        return lst
    
sol = Solution()
print(sol.groupAnagrams(strs = ["a"]))
            