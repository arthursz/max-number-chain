import unittest

from operator import add


def get_maximum_sum_substring(vector):
    chain = []
    value = -99999

    vector_size = len(vector)

    for begin in range(vector_size):
        for end in range(vector_size):
            if end < begin:
                continue

            chain_sum = reduce(add, vector[begin:end + 1])

            if chain_sum > value:
                value = chain_sum
                chain = [begin, end]

    return chain, value

class TestMaximumSumSubstring(unittest.TestCase):

    def test_positive_chain(self):
       chain, value = get_maximum_sum_substring([0,1,2,3,4,5])

       self.assertEqual(chain, [0,5])
       self.assertEqual(value, 15)

    def test_negative_chain(self):
       chain, value = get_maximum_sum_substring([-1,-2,-3,-4,-5])

       self.assertEqual(chain, [0,0])
       self.assertEqual(value, -1)

    def test_maximum_chain_in_the_begining(self):
       chain, value = get_maximum_sum_substring([7,3,-5,-3,5,-10])

       self.assertEqual(chain, [0,1])
       self.assertEqual(value, 10)

    def test_maximum_chain_in_the_middle(self):
       chain, value = get_maximum_sum_substring([-2,-3,5,3,5,-10])

       self.assertEqual(chain, [2,4])
       self.assertEqual(value, 13)

    def test_maximum_chain_in_the_end(self):
       chain, value = get_maximum_sum_substring([7,-3,-5,-3,5,10])

       self.assertEqual(chain, [4,5])
       self.assertEqual(value, 15)

    def test_mix_chain(self):
       chain, value = get_maximum_sum_substring([7,-3,5,3,-5,-10])

       self.assertEqual(chain, [0,3])
       self.assertEqual(value, 12)

if __name__ == '__main__':
    unittest.main()

