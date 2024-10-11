# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#class Solution:
#    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        #print("define = ",val)
    
    def printListNode(self):
        print(self.val)
        if ( self.next is not None):
            self.next.printListNode()
    


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2 
                list2 = list2.next 
            else:
                curr.next = list1
                list1 =list1.next 
            curr = curr.next 
        
        if not list1:
            curr.next =list2 

        else:
            curr.next = list1 
        return dummy.next




c=ListNode(4)       
b=ListNode(2,c)        
a=ListNode(1,b)  

z=ListNode(4)
y=ListNode(3,z)
x=ListNode(1,y)

print("**********")


a.printListNode()    
x.printListNode() 

d = Solution().mergeTwoLists(a,x)

print("= RESULT =")

d.printListNode() 



    
    
    
       
        
    
    

            
        
        

# ### TEST

# list11 = [1,2,4]
# list12 = [1,3,4]

# list21 = []
# list22 = []

# list31 = []
# list32 = [0]

