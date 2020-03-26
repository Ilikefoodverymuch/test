# class ListNode:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#
# # class sigleLinkList(object):
# #     def __init__(self,node = None):
# #         self.__head = node
# #
# #     def add(self,item):
# #         node = ListNode(item)
# #         node.next = self.__head
# #         self.__head = node
# #
# #     def travel(self):
# #         node = self.__head
# #         while node != None:
# #             print(node.val,end=' ')
# #             node = node.next
#
# class addTwoNumbers:
#     def addTwoNumbers(self,l1,l2):
#         count = 1
#         temp = 0
#         while (l1 or l2):
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0
#             temp = (x + y) * count + temp
#             if l1 != None:
#                 l1 = l1.next
#             if l2 != None:
#                 l2 = l2.next
#             count = count *10
#         print(temp,end="sssssssssss")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0
        count = 1
        l3 = ListNode(0)
        t = l3
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            temp = (x+y) * count + temp
            count = count * 10
            if(l1 != None):
                l1 = l1.next
            if(l2 != None):
                l2 = l2.next
        while temp != 0:
            t.next = ListNode(temp%10)
            t = t.next
            temp = temp//10

        return l3.next

    def travel(self,node):
        while node != None:
            print(node.val)
            node = node.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    func = Solution()
    l3 = func.addTwoNumbers(l1,l2)
    print(l3.val)
    print(l3.next.val)
    print(l3.next.next.val)


#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         temp = 0
#         count = 1
#         while(l1 or l2):
#             x = l1.val if l1 != None
#             y = l2.val if l2 != None
#             temp = (x+y) * count
#             count = count * 10
#             if(l1 != None):
#                 l1 = l1.next
#             if(l2 != None):
#                 l2 = l2.next
#         while temp % 10 != 0:
#             tempnode = ListNode(temp%10)
#             l3 = ListNode(temp%10)
#             temp = temp/10