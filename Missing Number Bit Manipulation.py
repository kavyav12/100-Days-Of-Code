class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        for i in range(1,n+1):
            ans ^=i
        for num in nums:
            ans ^=num
        return ans
        
sol=Solution()
print(sol.missingNumber([3,0,1]))
            
