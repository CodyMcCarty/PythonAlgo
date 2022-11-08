import unittest
from algo_ds import AlgoDs as Algo

# run test with: py -m unittest spec.ValidateAlgos

class ValidateAlgos(unittest.TestCase):
    """
    Tests algos
    """
    # algo = Algo()
    
    def test_to_basic(self):
        """
        When you age to, its age increases by 2
        """
        # self.algo.to(5)
        algo = Algo()
        self.assertEqual(algo.to(5), 5)

    if __name__ == '__main__':
        unittest.main()


