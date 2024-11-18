"""
Practising writing tests for various functions
https://docs.science.ai.cam.ac.uk/packaging-publishing/4_Testing/
"""
import unittest
from cancer_prediction.CancerModel import CancerModel    # what is the dot doing?

class TestCancerModel(unittest.TestCase):

    def test_target_to_diagnosis():
        model = CancerModel()
        # target = model.target_to_diagnosis("Benign")
        # assert target == 1

        # target = model.target_to_diagnosis("Malignant")
        # assert target == 0
        self.assertEqual(model.target_to_diagnosis("Benign"), 1)
        self.assertEqual(model.target_to_diagnosis("Malignant"), 0)


if __name__ == '__main__':
    unittest.main()