class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str1=""
        str2=""
        for s in S:
            if(s =="#" and str1!=""):
                str1 = str1[0:-1]
            elif(s != "#"):
                str1 += s
        
        for t in T:
            if(t =="#" and str2!=""):
                str2 = str2[0:-1]
            elif(t != "#"):
                str2 += t
                
        return str1==str2
            
            
                
                    
                
        