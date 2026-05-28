# Definition for singly-linked list.

from subprocess import list2cmdline
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    #runtime 30ms, memory 7.7mb
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res : Optional[ListNode] = None
        copy: Optional[ListNode] = None

        while list1 is not None or list2 is not None:
            next_node = None
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    next_node = list1
                    list1 = list1.next
                else:
                    next_node = list2
                    list2 = list2.next
            elif list1 is not None:
                next_node = list1
                list1 = list1.next
            elif list2 is not None:
                next_node = list2
                list2 = list2.next
            else:
                break
            
            if res is None:
                res = next_node
                copy = res
            else:
                copy.next = next_node
                copy = copy.next
        return res

    # Refactored
    # runtime 28ms, memory 8.0mb
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next