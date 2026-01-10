class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        size=len(nums)
        req_freq=size//2
        ans=nums[0]
        freq=1
        if size==1:
            return ans
        for i in range(size):
            if nums[i]==nums[i-1]:
                freq=freq+1
            else:
                freq=1
                ans=nums[i]
            if freq>req_freq:
                return ans
