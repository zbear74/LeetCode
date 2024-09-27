# in HARD
#class Solution:
#    def isPalindrome(self, x: int) -> bool:
        
class Solution:
    def isPalindrome(self, x: int):
        s1 = str(x)
        s2 = ''
        l1 = list(s1)
        l2 = l1.copy()
        l2.reverse()
        for i in range(0,len(l1)):
            s2 += str(l2[i])
        
       
        # ###print(x)
        # print(s1)
        # print(l1) 
        # print('=====')
        # print(s2)
        # print(l2) 
        
        if s1 == s2: 
            return True
        else:
            return False
         
        
        
        
        
        
        
        
print(Solution().isPalindrome(19232912))



# x1 = 100
# s1 = str(x1)
# s2=''
# l1 = list(s1)
# l2 = l1.copy()
# l2.reverse()
# for i in range(0,len(l2)):
#     s2 = s2+str(l2[i])
# x2 = int(s2)

# print(x1)
# print(s1)
# print(l1) 
# print('=====')
# print(x2)
# print(s2)
# print(l2) 


