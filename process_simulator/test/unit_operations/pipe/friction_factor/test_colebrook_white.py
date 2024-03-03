"""
Created by
"""
import unittest

from process_simulator.src.unit_operations.pipe.friction_factor.colebrook_white import ColebrookWhite


class ColebrookWhiteTest(unittest.TestCase):
    """
    Simple test cases
    """

    def setUp(self) -> None:
        self.roughness = 0.001  # roughness height (m)
        self.diameter = 0.1  # diameter of the pipe (m)

    def test_calculate_turbulent(self) -> None:
        """
        Test for the calculate method.
        """

        reynolds_no = 50000  # Reynolds number
        friction_factor_corr = ColebrookWhite(
            reynolds_no, self.roughness/self.diameter)
        friction_factor = friction_factor_corr.calculate()

        self.assertNotEqual(friction_factor, 0.0)
        self.assertGreater(friction_factor, 0)

    def test_calculate_transition(self) -> None:
        """
        Test for the transition case
        """
        reynolds_no = 3500
        friction_factor_corr = ColebrookWhite(
            reynolds_no, self.roughness/self.diameter)
        friction_factor = friction_factor_corr.calculate()

        self.assertGreater(friction_factor, 0)
        self.assertNotEqual(friction_factor, 64./reynolds_no)

    def test_calculate_laminar(self) -> None:
        """
        Test for the laminar case
        """
        reynolds_no = 2000
        friction_factor_corr = ColebrookWhite(
            reynolds_no, self.roughness/self.diameter)
        friction_factor = friction_factor_corr.calculate()

        self.assertEqual(friction_factor, 64./reynolds_no)


if __name__ == '__main__':
    unittest.main()
