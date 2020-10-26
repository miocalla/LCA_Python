'''
Created on 13 Oct 2020

# GeeksforGeeks implementation
@author: michaelocallaghan
'''
class Node: 
    
    def __init__(self, key): 
        self.key =  key 
        self.left = None
        self.right = None
  
def findPath( root, path, k): 
  
    if root is None: 
        return False
  
    # Store this node is path vector. The node will be removed if not in path from root to k 
    path.append(root.key) 
  
    # See if the k is same as root's key 
    if root.key == k : 
        return True
  
    # Check if in left or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If it gets this far, it means its not present so lets remove the root from the path and return False
    path.pop() 
    return False
  
# Returns LCA if node number1 , number2 are present in the given binary tree otherwise return -1 
def findLowestCommonAncestor(root, number1, number2): 
  
    # To store paths from root to number1 and number2
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to number1 and root to number2. Return -1 if either number1 or number2 is not present 
    if (not findPath(root, path1, number1) or not findPath(root, path2, number2)): 
        return -1 
  
    # Compare the paths to get the first different value 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  


