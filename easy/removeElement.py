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