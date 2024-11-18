"""
Practising writing tests for various functions
https://docs.science.ai.cam.ac.uk/packaging-publishing/4_Testing/
"""

import unittest

from cancer_prediction.cancer_model import CancerModel

# class TestCancerModel(unittest.TestCase):

#     def test_target_to_diagnosis(self):
#         model = CancerModel()
#         # target = model.target_to_diagnosis("Benign")
#         # assert target == 1

#         # target = model.target_to_diagnosis("Malignant")
#         # assert target == 0
#         self.assertEqual(model.target_to_diagnosis("Benign"), 1)
#         self.assertEqual(model.target_to_diagnosis("Malignant"), 0)


class TestCancerModel(unittest.TestCase):

    def test_diagnosis_to_target(self):
        model = CancerModel()
        diagnosis = "Malignant"
        target = model.diagnosis_to_target(diagnosis)
        self.assertEqual(target, 0)

        diagnosis = "Benign"
        target = model.diagnosis_to_target(diagnosis)
        self.assertEqual(target, 1)

    def test_target_to_diagnosis(self):
        model = CancerModel()
        target = 0
        diagnosis = model.target_to_diagnosis(target)
        self.assertEqual(diagnosis, "Malignant")

        target = 1
        diagnosis = model.target_to_diagnosis(target)
        self.assertEqual(diagnosis, "Benign")


if __name__ == "__main__":
    unittest.main()
