import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple_1(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        self.assertEqual(bst.search(1), False)
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_simple_2(self):
        bst = BinarySearchTree()
        bst.insert(38)
        bst.insert(2)
        bst.insert(29)
        bst.insert(9)
        bst.insert(68)
        bst.insert(1)
        bst.insert(34)
        bst.insert(8)
        bst.insert(24)
        bst.insert(34)
        bst.insert(56)
        bst.insert(48)
        self.assertEqual(bst.tree_height(),4)
        self.assertEqual(bst.find_min(), (1, None))
        self.assertEqual(bst.find_max(), (68, None))
        self.assertEqual(bst.inorder_list(),[1, 2, 8, 9, 24, 29, 34, 38, 48, 56, 68])
        self.assertEqual(bst.preorder_list(),[38, 2, 1, 29, 9, 8 , 24, 34, 68, 56, 48])
        self.assertEqual(bst.level_order_list(),[38, 2, 68, 1, 29, 56, 9, 34, 48, 8, 24])

    def test_search(self):
        # test case for an empty list
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())

if __name__ == '__main__': 
    unittest.main()
