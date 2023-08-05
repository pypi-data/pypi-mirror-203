
from unittest import TestCase

from caselessmapping import CaselessMapping

class TestCaselessMapping(TestCase):

    def test_null_init(self):
        self.assertRaises(TypeError, CaselessMapping)

    def test_int_keys(self):
        data = {1: 10, 2: 20, 3:30}
        cd = CaselessMapping(data)
        self.assertEqual(cd, data)

    def test_str_keys(self):
        data = {'a': 'A', 'b': 'B', 'c': 'C'}
        cd = CaselessMapping(data)
        self.assertEqual(cd, data)

    def test_matching_case_retreive(self):
        data = {'a': 'A', 'B': 'B', 'c': 'C'}
        cd = CaselessMapping(data)
        self.assertEqual(cd['a'], data['a'])
        self.assertEqual(cd['B'], data['B'])

    def test_caseless_retreive(self):
        data = {'a': 'A', 'B': 'B', 'c': 'C'}
        cd = CaselessMapping(data)
        self.assertEqual(cd['A'], data['a'])
        self.assertEqual(cd['b'], data['B'])

    def test_len(self):
        data = {'a': 'A', 'B': 'B', 'c': 'C'}
        cd = CaselessMapping(data)
        self.assertEqual(len(cd), 3)

    def test_iter(self):
        data = {'a': 'A', 'B': 'B', 'c': 'C'}
        cd = CaselessMapping(data)
        orig_tups = list(data.items())
        test_tups = list(cd.items())
        self.assertListEqual(orig_tups, test_tups)

    def test_raw_name(self):
        data = {'a': 'A', 'B': 'B', 'c': 'C'}
        cd = CaselessMapping(data)
        self.assertEqual(cd.get_raw_key_name('b'), 'B')
