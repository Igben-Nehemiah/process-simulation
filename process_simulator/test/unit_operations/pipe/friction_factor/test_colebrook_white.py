"""
Created by
"""
import unittest

from .....src.unit_operations.pipe.friction_factor.colebrook_white import ColebrookWhite


class ColebrookWhiteTest(unittest.TestCase):
    """
    Simple test cases
    """

    def test_calculate(self) -> None:
        """
        Test for the calculate method.
        """
        roughness = 0.001  # roughness height (m)
        diameter = 0.1  # diameter of the pipe (m)
        reynolds_no = 50000  # Reynolds number
        friction_factor_corr = ColebrookWhite(
            reynolds_no, roughness/diameter)
        friction_factor = friction_factor_corr.calculate()

        self.assertNotEqual(friction_factor, 0.0)
        self.assertGreater(friction_factor, 0)
        print(friction_factor)


if __name__ == '__main__':
    unittest.main()
