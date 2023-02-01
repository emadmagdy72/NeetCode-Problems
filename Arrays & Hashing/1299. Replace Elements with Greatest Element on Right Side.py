class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        mx = -1
        n = len(arr)
        for i in range(n-1,-1,-1):
            curr = arr[i]
            arr[i] = mx
            mx = max(mx,curr)
        
        return arr

    #---------Another Solution--------#
    # def replaceElements(self, arr):
    #     """
    #     :type arr: List[int]
    #     :rtype: List[int]
    #     """
    #     maximum = max(arr)
    #     for i in range(1,len(arr)):
    #         if arr[i-1] == maximum:
    #             maximum = max(arr[i:])
    #         arr[i-1] = maximum      
    #     arr[-1] = -1    
    #     return arr


