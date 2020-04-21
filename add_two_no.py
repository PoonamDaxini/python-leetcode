# problem: https://leetcode.com/problems/add-two-numbers/
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        
        #pointers for respective ll
        p1 = l1
        p2 = l2
        
        # new  ll
        result = head = ListNode(0)
        
        while p1 or p2 or carry:
            sum_val = carry
            sum_val += 0 if p1 is None else p1.val
            sum_val += 0 if p2 is None else p2.val
            
            if sum_val >=10:
                sum_val -= 10
                carry = 1
            else:
                carry = 0
            
            result.next = ListNode(sum_val)
            result = result.next
            
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
                
        
        return head.next
