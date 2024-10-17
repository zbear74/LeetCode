# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
        

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start_idx = 0
        finish_idx = len(nums)-1
        curr_idx = int((finish_idx - start_idx)/2) + start_idx
        
        
        result = 0
        
        print("Input =",nums,"Target =",target)
        
        if target <= nums[start_idx]:
            return start_idx
        if target > nums[finish_idx]:
            return finish_idx +1
            
        
        while curr_idx != finish_idx:
            
            # if exclude
            if target <= nums[start_idx]:
                return start_idxs
            if target > nums[finish_idx]:
                return finish_idx +1
            
            
            
            # search target
            if target < nums[curr_idx]:
                finish_idx = curr_idx
            elif target > nums[curr_idx]:
                if start_idx == curr_idx: # exclude before begin
                    return start_idx+1
                start_idx = curr_idx                
            else:
                result = curr_idx
                return result
                       
            
            # new itteration
            curr_idx = int((finish_idx - start_idx)/2) + start_idx
            #curr_idx = int((finish_idx - start_idx)/2) + (finish_idx - start_idx)%2
            #curr_idx = int((finish_idx - start_idx)/2)    
            
        
        
        



#Example 1:
nums1 = [1,3,5,6]
target1 = 5
#Output: 2

#Example 2:

nums2 = [1,3,5,6]
target2 = 2
#Output: 1

#Example 3:
nums3 = [1,3,5,6]
target3 = 7
#Output: 4

nums4 = [1]
target4 = 2 # must 0

nums5 = [1,3]
target5 = 3 # must 1

nums6 = [1,3,5]
target6 = 4 # must 1

nums7 = [2,7,8,9,10]
target7 = 9


print("Output1 =",Solution().searchInsert(nums1,target1))
print("Output2 =",Solution().searchInsert(nums2,target2))
print("Output3 =",Solution().searchInsert(nums3,target3))
print("Output4 =",Solution().searchInsert(nums4,target4))
print("Output5 =",Solution().searchInsert(nums5,target5))
print("Output6 =",Solution().searchInsert(nums6,target6))
print("Output7 =",Solution().searchInsert(nums7,target7))