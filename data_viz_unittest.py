import sys
import unittest
import random
import os
import math
import data_viz as dv


class TestColumn(unittest.TestCase):
    def test_box_unstructured_input_file(self):
        with self.assertRaises(NameError):
            dv.boxplot(oadsuhfa, 'test.png')

    def test_box_string_input_file(self):
        with self.assertRaises(TypeError):
            dv.boxplot('oadsuhfa', 'test.png')

    def test_box_float_input_file(self):
        with self.assertRaises(TypeError):
            dv.boxplot(0.853, 'test.png')

    def test_box_no_file_name(self):
        with self.assertRaises(TypeError):
            dv.boxplot(self.file_int, )

    def test_box_int_file_name(self):
        with self.assertRaises(ValueError):
            dv.boxplot(self.file_int, 17274)

    def test_hist_unstructured_input_file(self):
        with self.assertRaises(NameError):
            dv.histogram(oadsuhfa, 'test.png')

    def test_hist_string_input_file(self):
        with self.assertRaises(TypeError):
            dv.histogram('oadsuhfa', 'test.png')

    def test_hist_float_input_file(self):
        with self.assertRaises(TypeError):
            dv.histogram(0.853, 'test.png')

    def test_hist_no_file_name(self):
        with self.assertRaises(TypeError):
            dv.histogram(self.file_int, )

    def test_hist_int_file_name(self):
        with self.assertRaises(ValueError):
            dv.histogram(self.file_int, 17274)

    def test_combo_unstructured_input_file(self):
        with self.assertRaises(NameError):
            dv.combo(oadsuhfa, 'test.png')

    def test_combo_string_input_file(self):
        with self.assertRaises(TypeError):
            dv.combo('oadsuhfa', 'test.png')

    def test_combo_float_input_file(self):
        with self.assertRaises(TypeError):
            dv.combo(0.853, 'test.png')

    def test_combo_no_file_name(self):
        with self.assertRaises(TypeError):
            dv.combo(self.file_int, )

    def test_combo_int_file_name(self):
        with self.assertRaises(ValueError):
            dv.combo(self.file_int, 17274)

    def setUp(self):
        self.direct_sum_int = 0
        self.file_int = []
        self.file_name = 'test.png'
        for i in range(100):
            rand_int = random.randint(1, 1000)
            self.direct_sum_int += rand_int
            self.file_int.append(rand_int)
        self.direct_mean_int = self.direct_sum_int/100
        self.direct_stdev_int = math.sqrt(sum([(self.direct_mean_int-x)**2
                                          for x in self.file_int]) /
                                          len(self.file_int))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
