class Solution:
    def twoSum(self, nums, target):# -> List[int]:
        i=0
        j=0
        num_result=[]
        found = False
        
        for i in range (0 , len(nums)):
          if found == False:
            
            for j in range(0, len(nums)):
                if i!= j and nums[i]+ nums[j]== target:
                   found = True
                   num_result.append(i)
                   num_result.append(j) 
                   break                 
          else: 
              break          
        return num_result     
        
        
a=Solution()  

print(a.twoSum([1,2,3,4,5,6],4))