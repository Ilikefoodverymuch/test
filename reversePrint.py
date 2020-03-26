# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode):
        return self.reversePrint(head.next) + [head.val] if head else []

if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = node2 = ListNode(2)
    node2.next = node3 = ListNode(3)
    node3.next = node4 = ListNode(4)
    t = Solution()
    l1 =[2]
    l2 = [1]
    print(l1 + l2)
    print(t.reversePrint(node1))