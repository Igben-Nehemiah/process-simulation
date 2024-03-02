"""
Created by
"""
import unittest

from ..colebrook_white import ColebrookWhite


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

        self.assertTrue(friction_factor > 0)


if __name__ == '__main__':
    unittest.main()
