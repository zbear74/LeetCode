# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
        
class Solution:
         
    def removeDuplicates(self, nums: [int] ) :
        uniq_val = nums[0]
        unique_cnt = 1
        curr_idx = 0 
        
        while curr_idx < len(nums):
            
            if uniq_val != nums[curr_idx]: # found new uniq_val
                unique_cnt += 1
                nums[unique_cnt-1] = nums[curr_idx] 
                uniq_val = nums[curr_idx]
            
            curr_idx +=1
        return unique_cnt        
            
            

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]       

print(nums1)     
n1 = Solution()
print(n1.removeDuplicates(nums1))
print(nums1)
print("===")
print(nums2)      
n2 = Solution()
print(n2.removeDuplicates(nums2))
print(nums2)