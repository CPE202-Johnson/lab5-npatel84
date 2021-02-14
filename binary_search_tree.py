from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    
        
    def inorder_list(self, node, pyList):

        if node is None:
            return None
        else:
            leftNode = self.inorder_list(temp.left, pyList)
            pyList.append(temp.key)
            rightNode = self.inorder_list(temp.right, pyList)
       
        return pyList
class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        if self.root is None: # returns True if a root exists
            return True
        return False          # returns False if a root exists

    def search(self,key): # returns True if key is in a node of the tree, else False
        
        # checking if the root exists
        if self.is_empty():
            return False
        
        # declaring 'temp' as a variable to traverse through the list 
        temp = self.root

        while temp is not None:
            # if the key does not exists, return True as there is no other roots present
            if temp.key == key:
                return True
            
            # check for right root
            elif temp.key < key:
                temp = temp.right
            
            # check for left root
            elif key < temp.key:
                temp = temp.left
        
        return False

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        
        tempNode = TreeNode(key, data)

        temp = self.root

        if self.is_empty():
            self.root = tempNode
    
        while temp is not None:

            if temp.key == key:
                temp.data = tempNode.data
                return True
            
            elif temp.key < key:
                temp.right = tempNode
                return True
            #temp = temp.right
            
            elif key < temp.key:
                temp.left = tempNode
                break
            temp = temp.left
            
    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        
        temp = self.root

        while temp is not None:
            
            if temp.left is None:
                return (temp.key, temp.data)
            temp = temp.left

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None

        temp = self.root

        while temp is not None:
            
            if temp.right is None:
                return (temp.key, temp.data)
            temp = temp.right

    def tree_height_helper(self, Node):
        
        if Node is None:
            return -1
       
        leftNode = self.tree_height_helper(node.left)
        rightNode = self.tree_height_helper(node.right)
        
        if leftNode > rightNode:
            return leftNode + 1
        
        return rightNode + 1

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        
        temp = self.root
        
        if temp is None:
            return None
      
        return self.tree_height_helper(temp)


    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        
        temp = self.root

        if self.is_empty:
            return []

        pyList = []
        return self.inorder_list(temp, pyList)

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        pass
        
   
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        pass
        

