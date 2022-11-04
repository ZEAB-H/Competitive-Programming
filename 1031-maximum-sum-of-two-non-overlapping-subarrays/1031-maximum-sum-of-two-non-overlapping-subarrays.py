class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(len(nums)-1):
            nums[i+1]+=nums[i]
        nums = [0] + nums
        def maxSum(l,m):
            maxL = 0
            ans = 0
            for i in range(firstLen+secondLen, len(nums)):
                maxL = max(maxL, nums[i-m]-nums[i-m-l])
               
                ans = max(ans, maxL+ nums[i]-nums[i-m])
            return ans
        
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))