from unittest import TestCase

from inevitable.tests import clocks


class TestFinite(TestCase):
    def test_it_runs_a_finite_number_of_times(self):
        clock = clocks.Finite(iterations=2)

        clock.time()
        clock.time()

        with self.assertRaises(clocks.EndOfTime):
            clock.time()

    def test_the_time_is_kept(self):
        clock = clocks.Finite(iterations=3)
        clock.time()
        self.assertEqual(clock.time(), 1)

    def test_it_starts_at_zero(self):
        clock = clocks.Finite(iterations=1)
        self.assertEqual(clock.time(), 0)

    def test_it_can_skip_steps(self):
        clock = clocks.Finite(iterations=5, step=3)
        clock.time()
        self.assertEqual(clock.time(), 3)
