#Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first_last =[1]
        last_first=[1]
        final = []
        for i in range(len(nums)):
            first_last.append(first_last[i] * nums[i])
        for i in range(1,len(nums)):
            last_first.append(last_first[-1] * nums[-i])
        for x,y in zip(first_last,last_first[::-1]):
            final.append(x * y)
        return final