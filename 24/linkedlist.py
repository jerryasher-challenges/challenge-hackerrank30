#!/bin/python 3

# Day 24: more linked lists


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while(start.next is not None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        current = head
        num = current.data
        while current.next is not None:
            if current.next.data == num:
                current.next = current.next.next
            else:
                current = current.next
                num = current.data
        return head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
