import unittest
from solutions import Solution

# run test with: py -m unittest spec.Validate

class Validate(unittest.TestCase):
    """
    Tests solutions
    """

    def test_convert_number_to_reversed_array(self):
        """
        When you pass a number, the correct array is returned
        """
        s = Solution()
        self.assertEqual(s.convert_number_to_reversed_array(35231), [1,3,2,5,3])
        self.assertEqual(s.convert_number_to_reversed_array(0), [0])
        self.assertEqual(s.convert_number_to_reversed_array(23582357),[7,5,3,2,8,5,3,2])
        self.assertEqual(s.convert_number_to_reversed_array(984764738),[8,3,7,4,6,7,4,8,9])
        self.assertEqual(s.convert_number_to_reversed_array(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
        self.assertEqual(s.convert_number_to_reversed_array(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])

    def test_testing123(self):
        """
        When you pass an array, the correct format is returned
        """
        s = Solution()
        self.assertEqual(s.testing123([]), [])
        self.assertEqual(s.testing123(["a", "b", "c"]), ["1: a", "2: b", "3: c"])
    

    if __name__ == '__main__':
        unittest.main()


