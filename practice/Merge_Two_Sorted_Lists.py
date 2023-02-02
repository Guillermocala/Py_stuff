# Return the head of the merged linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = res = ListNode()
        for item in list1:
            res.next = ListNode(item)
        return head


list1 = [1, 2, 4]
list2 = [1, 3, 4]

solution = Solution().mergeTwoLists(list1, list2)
while solution.next != None:
    print(solution.val)
    solution = solution.next