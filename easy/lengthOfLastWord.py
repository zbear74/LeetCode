# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(" ")
        no_space_cnt = 0
        for i in range (len(s)-1,-1,-1):
            print(len(s),i,s[i])
            if s[i] != " ":
                no_space_cnt +=1
            else:
                return no_space_cnt
        
        return no_space_cnt    



#Example 1:
#s1 = "Hello World"
s1 =""
#Output: 5

#Example 2:
s2 = "   fly me   to   the moon  "
#Output: 4

#Example 3:
s3 = "luffy is still joyboy"
#Output: 6

print(s1,"Output:",Solution().lengthOfLastWord(s1))
print(s2,"Output:",Solution().lengthOfLastWord(s2))
print(s3,"Output:",Solution().lengthOfLastWord(s3))
        