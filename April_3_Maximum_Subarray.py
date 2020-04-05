class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        new_nums=[nums[0]]
        prev_sum =nums[0]
        
        for i in range(1, len(nums)):
            summ = new_nums[i-1] + nums[i]
            #print(summ)
            new_nums.append(max(nums[i],summ))
        
        #print(new_nums)
        return max(new_nums)
        