import copy

# 链表节点类
class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def addNode(self, val):
        # 产生节点
        node = Node(val)
        if self.head.val == -1:
            self.head = node
            # 有环链表这里为指向的节点（入口点）
            self.head.next = None
        else:
            node.next = self.head
            self.head = node

    # 反转链表-迭代
    def reverseLinkedListLoop(self):
        pre = None
        while self.head.next:
            next = self.head.next
            self.head.next = pre
            pre = self.head
            self.head = next
        # 把原来指向None的尾指针指向pre
        self.head.next = pre

    # 反转链表-递归
    def reverseLinkedListRecur(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverseLinkedListRecur(head.next)
        # 反转当前和next指针的指向
        head.next.next = head
        # 原来的next释放掉
        head.next = None
        return newHead

    def printLinkedList(self):
        head = copy.copy(self.head)
        string = ''
        while head:
            string = string + str(head.val) + '-->'
            head = head.next
        print(string + 'None')

# 有环链表
class LinkedListCircle(LinkedList):
    def __init__(self, inNodeVal):
        """
        :param inNodeVal:环链表的入口点的值 
        """
        super().__init__()
        self.inNodeVal = inNodeVal

    def addNode(self, val):
        # 产生节点
        node = Node(val)
        if self.head.val == -1:
            self.head = node
            # 有环链表入口点:先写死为倒数第5个节点
            self.head.next = Node(self.inNodeVal)
        else:
            node.next = self.head
            self.head = node

    def printLinkedList(self):
        head = copy.copy(self.head)
        string = ''
        isFirst = False
        while True:
            if isFirst and head.val == 5:
                break
            elif not isFirst and head.val == 5:
                isFirst = True
            string = string + str(head.val) + '-->'
            head = head.next
        print(string + str(self.inNodeVal))

# class LinkedListUtils:
#     @staticmethod
#     def hasCircle(headNode):
#         if not headNode or not headNode.next:
#             return False
#         fast = headNode.next.next
#         slow = headNode.next
#         while True:
#             if not fast:
#                 return False
#             if fast == slow:
#                 return True
#             fast = fast.next.next
#             slow = slow.next

if __name__ == '__main__':
    ls = LinkedList()
    for i in range(1, 21):
        ls.addNode(i)
    #打印链表
    ls.printLinkedList()
    # 反转链表
    ls.reverseLinkedListLoop()
    # 打印反转后的链表
    ls.printLinkedList()
    # 递归反转链表
    ls.head = ls.reverseLinkedListRecur(ls.head)
    # 打印反转后的链表
    ls.printLinkedList()

    # 有环链表
    lsc = LinkedListCircle(5)
    for i in range(1, 21):
        lsc.addNode(i)
    # 打印有环链表
    lsc.printLinkedList()