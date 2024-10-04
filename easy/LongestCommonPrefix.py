#class Solution:
#    def longestCommonPrefix(self, strs: List[str]) -> str:

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]    
strs3 = ["cir","car"]
strs4 = ["flower","fkow"]
strs5 = ["abab","aba",""]
strs6 = ["acbb","a"]
           
class Solution:
    def longestCommonPrefix(self, l_str) -> str:        
        result = l_str[0]
        for item in l_str:
            if result == "":
                return ""
            for i in range(len(result),0,-1):                
                if item.startswith(result):                                        
                    break
                else:
                    result = result[:len(result)-1]
        return result     

a = Solution().longestCommonPrefix(strs6)

print("res = [",Solution().longestCommonPrefix(strs1),"]")
print("res = [",Solution().longestCommonPrefix(strs2),"]")
print("res = [",Solution().longestCommonPrefix(strs3),"]")
print("res = [",Solution().longestCommonPrefix(strs4),"]")
print("res = [",Solution().longestCommonPrefix(strs5),"]")
print("res = [",Solution().longestCommonPrefix(strs6),"]")