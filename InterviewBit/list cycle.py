# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A==None or A.next==None:
            return None
        temp=A
        slow=A
        fast=A.next
        s=1
        while(slow!=fast):
            slow=slow.next
            s+=1
            if fast.next==None or fast.next.next==None:
                return None
            
            fast=fast.next.next
        
        temp=A
        slow=slow.next
        
        while slow!=temp:
            slow=slow.next
            temp=temp.next
            
        return temp
        
        
        
