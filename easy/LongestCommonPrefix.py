#class Solution:
#    def longestCommonPrefix(self, strs: List[str]) -> str:

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]    

class Solution():
    def longestCommonPrefix(self, l_str) -> str:
        result =""
        template_str = l_str[0]
        for item in l_str:
            result=""   
            for i in range(0,len(item)):
                if i< len(template_str) and item[i] ==  template_str[i]:
                    result += item[i]                
            template_str= result
        return result            

print("res = [",Solution().longestCommonPrefix(strs1),"]")
print("res = [",Solution().longestCommonPrefix(strs2),"]")
