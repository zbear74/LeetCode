# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pass
        result_nums=[]
    
        for i in range(0,len(nums2)):
            nums1[i+m] =nums2[i]
        
        nums1.sort()    
            
            

#Example 1:
nums11 = [1,2,3,0,0,0]
m1 = 3
nums21 = [2,5,6]
n1 = 3

# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

#Example 2:

nums12 = [1]
m2 = 1
nums22 = []
n2 = 0

# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].


#Example 3:
nums13 = [0]
m3 = 0
nums23 = [1]
n3 = 1

# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Solution().merge(nums11,m1,nums21,n1)
print(nums11)

Solution().merge(nums12,m2,nums22,n2)
print(nums12)

Solution().merge(nums13,m3,nums23,n3)
print(nums13)
