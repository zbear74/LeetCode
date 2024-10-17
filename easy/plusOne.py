# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        dig=0
        #print(s,digits,dig)
        s = s.join(str(element) for element in digits)
        dig = int(s)+1
        s = str(dig)
        digits =list(s)
        for i in range(0,len(digits)):            
            #digits.pop(i)
            digits.insert(i, int(digits[i]))
            digits.pop(i+1)
        
        #print(s,digits,dig)
        return digits
        


# Example 1:
digits1 = [1,2,3]
#Output1: [1,2,4]

#Example 2:
digits2 = [4,3,2,1]
#Output: [4,3,2,2]

#Example 3:
digits3 = [9]
#Output: [1,0]


print("Input1:", digits1,"Output1:",Solution().plusOne(digits1))
print("Input2:", digits2,"Output2:",Solution().plusOne(digits2))
print("Input3:", digits3,"Output3:",Solution().plusOne(digits3))