
'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
1st April Wednesday'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = dict()
        
        for ele in nums:
            if ele not in my_dict.keys():
                my_dict[ele] = 1
            else:
                my_dict[ele] = my_dict[ele] + 1
        for key, value in my_dict.items():
            if (value == 1):
                 return_value = key
        return return_value