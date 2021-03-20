"""
题目描述
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。

链表结点定义如下：

struct ListNode

{

int       m_nKey;

ListNode* m_pNext;

};



正常返回倒数第k个结点指针，异常返回空指针

本题有多组样例输入。

输入说明
1 输入链表结点个数
2 输入链表的值
3 输入k的值

输出描述:
输出一个整数
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = node

    def get_value(self, no):
        n_node = self.head
        value = None
        for _ in range(no):
            n_node = n_node.next
            if n_node is None:
                return 0
            value = n_node.value
        return value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


while True:
    try:
        count = int(input())
        values = input().strip().split(' ')
        k = int(input())
        l = LinkedList()
        for i in values:
            l.append(int(i))
        print(l.get_value(count - k))

    except:
        break
