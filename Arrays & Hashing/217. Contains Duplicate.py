class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        set1 = set()
        for num in nums:
            if num in set1:
                return True
            else:
                set1.add(num)
        return False

        #------Another Solution------#
        # len1 = len(nums)
        # len2 = len(set(nums))
        # if(len1 == len2):
        #     return False
        # else:
        #     return True





