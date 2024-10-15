# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
        
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        val_cnt = 0
        original_len_nums = len(nums)
         
        result_list =[]
        
        while val in nums:
            nums.remove(val)
            val_cnt +=1
                
        nums=result_list.copy()
        
        return original_len_nums - val_cnt
        
        
        
        
        # 2 variant - in comment - because - not approve leetCode for nums3
        # val_cnt = 0
        # curr_idx = 0 
        # ins_idx = len(nums)-1
        
        
        # while curr_idx < len(nums) and ins_idx > 0 :
            
        #     if  nums[curr_idx] == val:
        #         if nums[ins_idx] != val:#and curr_idx < ins_idx:
        #             nums[curr_idx] = nums[ins_idx]
        #             curr_idx +=1
        #             val_cnt +=1
        #             ins_idx -=1
        #         else:
        #             ins_idx -=1
        #             nums[ins_idx]=val+1
        #     else:
        #         curr_idx +=1
        # result = len(nums) - val_cnt
        # if result == len(nums):
        #  return len(nums) - val_cnt        
            
            
            
            
            
            

nums1 = [3,2,2,3]
val1 = 3
#Output: 2, nums = [2,2,_,_]

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
#Output: 5, nums = [0,1,4,0,3,_,_,_]


nums3 = [1,1,1,1,1]
val3 = 1


print(nums1,val1)     
n1 = Solution()
print(n1.removeElement(nums1,val1))
print(nums1)
print("===")

print(nums2,val2)      
n2 = Solution()
print(n2.removeElement(nums2,val2))
print(nums2)
print("===")        

print(nums3,val3)      
n3 = Solution()
print(n3.removeElement(nums3,val3))
print(nums3)
print("===")