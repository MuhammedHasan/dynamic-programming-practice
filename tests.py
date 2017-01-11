import unittest

from rod_cutting import RodCutter


class TestsRodCutter(unittest.TestCase):

    def setUp(self):
        prices = [1,  5, 8,  9, 10, 17, 17, 20, 24, 30]
        self.cutter = RodCutter(prices)

    def based_rod_cutting(self, cutter_function):
        self.assertEqual(cutter_function(1), 1)
        self.assertEqual(cutter_function(2), 5)
        self.assertEqual(cutter_function(3), 8)
        self.assertEqual(cutter_function(4), 10)
        self.assertEqual(cutter_function(5), 13)
        self.assertEqual(cutter_function(6), 17)
        self.assertEqual(cutter_function(7), 18)
        self.assertEqual(cutter_function(8), 22)
        self.assertEqual(cutter_function(9), 25)
        self.assertEqual(cutter_function(10), 30)
        self.assertEqual(cutter_function(11), 31)

    def based_cut_road(self, cutter_function):
        for i in range(10, 20):
            self.assertEqual(self.cutter.cut_road(i), cutter_function(i))

    def test_cut_road(self):
        self.based_rod_cutting(self.cutter.cut_road)

    def test_memorized_cut_rod(self):
        self.based_rod_cutting(self.cutter.memorized_cut_rod)
        self.based_cut_road(self.cutter.memorized_cut_rod)

    def test_bottom_up_cut_rod(self):
        self.based_rod_cutting(self.cutter.bottom_up_cut_rod)
        self.based_cut_road(self.cutter.bottom_up_cut_rod)

    def test_solution_of_rod(self):
        self.assertEqual(list(self.cutter.solution_of_rod(1)), [1])
        self.assertEqual(list(self.cutter.solution_of_rod(8)), [2, 6])
        self.assertEqual(list(self.cutter.solution_of_rod(9)), [3, 6])
        self.assertEqual(list(self.cutter.solution_of_rod(10)), [10])


if __name__ == "__main__":
    unittest.main()
