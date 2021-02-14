import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_is_full(self):
    
        queue = Queue(5)
        queue.enqueue(11)
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        queue.enqueue(15)
    
        self.assertTrue(queue.is_full)

    def test_enqueue_1(self):
    
        queue = Queue(5)
        queue.enqueue(11)
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        queue.enqueue(15)
        with self.assertRaises(IndexError):
            queue.enqueue(5)

    def test_enqueue_2(self):
        
        queue = Queue(5)
        queue.enqueue(11)
        queue.enqueue(12)
        queue.enqueue(13)
        queue.enqueue(14)
        queue.enqueue(15)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_dequeue_2(self):
        queue = Queue(5)
        with self.assertRaises(IndexError):
            queue.dequeue()

if __name__ == '__main__': 
    unittest.main()
