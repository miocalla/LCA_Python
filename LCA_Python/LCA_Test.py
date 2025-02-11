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
        
    def testNullTree(self):
        root = None
        self.assertEqual(findLowestCommonAncestor(root, 2, 3), -1)
        path = []
        self.assertFalse(findPath(root, path, 8))
        self.assertListEqual(path, [])
        
    def testRootAsInput(self):
        self.assertEqual(findLowestCommonAncestor(root, 1, 4), 1)
        
    def testOnlyOneExists(self):
        self.assertEqual(findLowestCommonAncestor(root, 4, 10), -1)
        self.assertEqual(findLowestCommonAncestor(root, 21, 7), -1)
        
    def testLCASameNode(self):
        self.assertEqual(findLowestCommonAncestor(root, 1, 1), 1)
        self.assertEqual(findLowestCommonAncestor(root, 7, 7), 7)

    def testNeitherExist(self):
        self.assertEqual(findLowestCommonAncestor(root, 10, 8), -1)

    def testOnlyOneNode(self):
        root = Node(10)
        self.assertEqual(findLowestCommonAncestor(root, 10, 10), 10)
        
    def testPathFinder(self):
        path = []
        # Root to itself
        self.assertTrue(findPath(root, path, 1))
        self.assertListEqual(path, [1])

        path = []
        # Right Side
        self.assertTrue(findPath(root, path, 7))
        self.assertListEqual(path, [1, 3, 7])

        path = []
        # Left Side
        self.assertTrue(findPath(root, path, 2))
        self.assertListEqual(path, [1, 2])

        path = []
        # No Path
        self.assertFalse(findPath(root, path, 12))
        self.assertListEqual(path, [])

        # Path not from root
        path = []
        self.assertTrue(findPath(root.right, path, 7))
        self.assertListEqual(path, [3, 7])

    print('Success.')


if __name__ == '__main__':
    unittest.main()
        
    