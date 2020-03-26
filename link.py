class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singleLinkList:

    def __init__(self,node = None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur !=None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.data,end = ' ')
            cur = cur.next
        print('\n')

    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

if __name__=="__main__":
    l1 = singleLinkList()
    print(l1.is_empty())
    print(l1.length())

    l1.add(2)
    print(l1.is_empty())
    l1.travel()