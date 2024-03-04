"""
Created by
"""
from math import pi
import unittest
from thermo import Stream  # type: ignore
from process_simulator.src.unit_operations.pipe.pipe_segment import PipeSegment


class PipeSegmentTest(unittest.TestCase):
    """
    Simple test cases
    """

    def setUp(self) -> None:
        self.roughness = 0.003      # roughness height (m)
        self.diameter = 0.5         # diameter of the pipe (m)
        self.length = 10000         # length of pipe in (m)
        self.q = 1                  # volumetric flowrate (m^3/s)

        self.inlet_stream = Stream(
            IDs=["Water"], zs=[1.], Q=self.q, T=298, P=1e7)

        self.pipe_segment = PipeSegment(name="section-A",
                                        diameter=self.diameter,
                                        length=self.length,
                                        roughness=self.roughness,
                                        inlet_stream=self.inlet_stream)

    def test_cross_sectional_area(self) -> None:
        """
        Test for cross-sectional area of the pipe.
        """
        self.assertAlmostEqual(
            self.pipe_segment.cross_sectional_area, 0.25*pi*self.diameter**2)

    def test_pressure_drop(self) -> None:
        """
        Test for pressure drop in segment.
        """
        self.pipe_segment.solve()

        self.assertTrue(
            self.pipe_segment.outlet_stream is not None and
            self.pipe_segment.outlet_stream.P is not None)

        if self.pipe_segment.outlet_stream is not None:
            self.assertAlmostEqual(
                self.inlet_stream.P - self.pipe_segment.pressure_drop,
                self.pipe_segment.outlet_stream.P)

        # print("Density: ", self.inlet_stream.rho)
        # print("Velocity: ", self.pipe_segment.velocity)
        # print("Pressure drop: ", self.pipe_segment.pressure_drop)


if __name__ == '__main__':
    unittest.main()
