import unittest
import regex


class TestRegex(unittest.TestCase):  # a test case for the regex.py module
    samples_for_true = {1: ['colou?r', 'color'],
                        2: ['colou?r', 'colour'],
                        3: ['colou*r', 'color'],
                        4: ['colou*r', 'colour'],
                        5: ['colou*r', 'colouur'],
                        6: ['col.*r', 'color'],
                        7: ['col.*r', 'colour'],
                        8: ['col.*r', 'colr'],
                        9: ['col.*r', 'collar'],
                        10: ['colou+r', 'colour'],
                        11: ['^no+pe$', 'noooooooope'],
                        12: ['^n.+pe$', 'noooooooope'],
                        13: ['.*', 'aaa'],
                        14: ['\\.$', 'end.'],
                        15: ['3\\+3', '3+3=6'],
                        16: ['\\?', 'Is this working?'],
                        17: ['\\\\', '\\']}

    samples_for_false = {1: ['colou?r', 'colouur'],
                         2: ['col.*r$', 'colors'],
                         3: ['app$', 'apple'],
                         4: ['^le', 'apple'],
                         5: ['colou+r', 'color'],
                         6: ['^n.+p$', 'noooooooope'],
                         7: ['colou\\?r', 'color'],
                         8: ['colou\\?r', 'colour']}

    def test_regex_str_cmp_true(self):
        # tests for the regex_str_cmp() function
        for key, val in self.samples_for_true.items():
            self.assertEqual(regex.regex_str_cmp(val[0], val[1]), True, f'{key}: {val[0]} - {val[1]}')

    def test_regex_str_cmp_false(self):
        # tests for the regex_str_cmp() function
        for key, val in self.samples_for_false.items():
            self.assertEqual(regex.regex_str_cmp(val[0], val[1]), False, f'{key}: {val[0]} - {val[1]}')


if __name__ == '__main__':
    unittest.main()
