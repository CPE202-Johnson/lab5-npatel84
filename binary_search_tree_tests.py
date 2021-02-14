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
        bst.insert(4)
        bst.insert(5)
        bst.insert(3)
        bst.insert(1)
        bst.insert(2)
        self.assertFalse(bst.is_empty())
        # self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 5])
        # self.assertEqual(bst.preorder_list(), [4, 2, 1, 3, 5])
        # self.assertEqual(bst.level_order_list(), [4, 2, 5, 1, 3])
        self.assertTrue(bst.search(3))
        self.assertFalse(bst.search(11))
        self.assertEqual(bst.find_min(), (1, None))
        self.assertEqual(bst.find_max(), (5, None))

    def test_search(self):

        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())



if __name__ == '__main__': 
    unittest.main()
