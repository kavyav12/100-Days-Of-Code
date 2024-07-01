class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sumn=((n)*(n+1))/2
        for i in (nums):
            sumn=sumn-i
        return sumn
sol=Solution()
print(sol.missingNumber([3,0,1]))
            
