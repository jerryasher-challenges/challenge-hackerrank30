#!/bin/python3

# Day 22: binary search trees


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

    def getHeight(self, root):
        if root is None:
            return 0

        # print("n: " + str(root.data))

        if root.left is None and root.right is None:
            return 0

        hleft = self.getHeight(root.left)
        hright = self.getHeight(root.right)

        height = 1 + max(hleft, hright)
        # print("n: " + str(root.data) + " height: " + str(height))
        return height

    def printTree(self, root):
        if root is None:
            return

        # print(root.data)

        self.printTree(root.left)
        self.printTree(root.right)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    print("insert " + str(data))
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
