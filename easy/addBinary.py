# class Solution:
#     def addBinary(self, a: str, b: str) -> str:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # print(int(a,base=2))
        # print(int(b,base=2))
        # print(int(a,base=2)+int(b,base=2))
        # print(format(( int(a,base=2)+int(b,base=2) ),'b'))
       return format(( int(a,base=2)+int(b,base=2) ),'b')



#Example 1:
#Input: 
a1 = "11"
b1 = "1"
#Output: "100"

#Example 2:
#Input: 
a2 = "1010"
b2 = "1011"
Output: "10101"
 

i1 = Solution().addBinary(a1,b1)
i2 = Solution().addBinary(a2,b2)

