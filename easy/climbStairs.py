# class Solution:
#     def climbStairs(self, n: int) -> int:
        
    
class Solution:
    # sequence Fibonachi - math
    def climbStairs(self, n: int) -> int:
        prev1 = 0
        prev2 = 1
        result = 1
        for i in range (0,n-1):
            prev1 = prev2
            prev2 = result
            result = prev1 + prev2
        return result
    


print(Solution().climbStairs(7))

# Fibonachi

# def climbStairs(n):
#         prev1 = 1
#         prev2 = 1 
#         temp = 0

#         for i in range(n-1):
#             temp = prev1 
#             prev1 = prev1+prev2
#             prev2 = temp
#           
#         return prev1
            
# print(climbStairs(6))




