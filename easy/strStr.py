# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
 
 


#Example 1:
haystack1 = "sadbutsad"
needle1 = "sad"

#Example 2:
haystack2 = "leetcode"
needle2 = "leeto"
 

print("Example1: ",haystack1,needle1,Solution().strStr(haystack1,needle1))
print("===")
print("Example2: ",haystack2,needle2,Solution().strStr(haystack2,needle2))
