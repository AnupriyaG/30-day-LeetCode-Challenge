# Perform String Shifts
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        #print(len(shift))
        for temp in shift:
            print(temp)
            #print(temp)
            #shifty = temp[1]
            #s_1 = s[:temp[1]+1]
            #print(s[2:])
            if(temp[0]==0):
                s_1 = s[:temp[1]]
                #print(s_1)
                s = s[temp[1]:]
                s = s + s_1
                print(s)
            else:
                s_1= s[-temp[1]:]
                #print(s_1)
                s = s[:-temp[1]]
                s = s_1 + s
                print(s)
        return s