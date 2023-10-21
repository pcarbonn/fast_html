import unittest
import time

from fast_html import div


class PerformanceTesting(unittest.TestCase):
    def test_large_structure_generation_performance(self):
        num_divs = 100000
        start_time = time.time()
        for _ in range(num_divs):
            "".join(div("Content"))
        end_time = time.time()
        execution_time = end_time - start_time
        max_execution_time = 0.130
        self.assertLessEqual(execution_time, max_execution_time)


if __name__ == "__main__":
    unittest.main()
