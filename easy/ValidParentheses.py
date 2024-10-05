# class Solution:
#     def isValid(self, s: str) -> bool:
        
class Solution:
    def isValid(self, s: str):
        count = 0
        
        is_changed_last_loop = False   
        
        while s != "":
            is_changed_last_loop = False
            if s != s.replace("()",""):
                count +=1
                is_changed_last_loop = True
                s=s.replace("()","")
            if s != s.replace("[]",""):
                count +=1
                is_changed_last_loop = True
                s=s.replace("[]","")
            if s != s.replace("{}",""):
                count +=1
                is_changed_last_loop = True
                s=s.replace("{}","")
            if is_changed_last_loop == False :
                break

        if count > 0 and is_changed_last_loop != False:
            return True
        else :
            return False
      
str1 = "[]{}(){{}}"  
str2 = ""
str3 = "()[]{}"
str4 = "(]"
str5 = "([])"
str6 = "([]){}{}{]}"

print("\"",str1,"\" = ",Solution().isValid(str1))
print("\"",str2,"\" = ",Solution().isValid(str2))
print("\"",str3,"\" = ",Solution().isValid(str3))    
print("\"",str4,"\" = ",Solution().isValid(str4))
print("\"",str5,"\" = ",Solution().isValid(str5))
print("\"",str6,"\" = ",Solution().isValid(str6))
    
    
        