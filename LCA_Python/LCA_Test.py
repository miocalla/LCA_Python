import unittest 
from LCA import *

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

'''
        1
      /   \
     2     3
    /\     /\
   4  5   6  7
'''


class testLowestCommonAncestor(unittest.TestCase):
    
    def setUp(self):
        pass

    def testNormalCases(self):
       
        # Same-level
        self.assertEqual(findLowestCommonAncestor(root, 2, 3), 1)
        self.assertEqual(findLowestCommonAncestor(root, 4, 6), 1)
        # Different-Level
        self.assertEqual(findLowestCommonAncestor(root, 2, 7), 1)
        self.assertEqual(findLowestCommonAncestor(root, 4, 3), 1)
        
    def testLCANotRoot(self):
        self.assertEqual(findLowestCommonAncestor(root, 6, 7), 3)
        self.assertEqual(findLowestCommonAncestor(root, 4, 5), 2)
        
    def testRootAsInput(self):
        self.assertEqual(findLowestCommonAncestor(root, 1, 4), 1)