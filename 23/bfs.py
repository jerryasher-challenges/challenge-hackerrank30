#!/bin/python3

# Day 23: BST Level-Order Traversal

# Breadth First Search


class Node:

    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):

        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
