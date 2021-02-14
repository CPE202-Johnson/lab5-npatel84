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
        bst.insert(0)
        bst.insert(1)
        bst.insert(2)
        self.assertFalse(bst.is_empty())

    def test_search(self):

        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())



if __name__ == '__main__': 
    unittest.main()
