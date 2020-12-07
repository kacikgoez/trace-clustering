import unittest
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
from tclustering import frequency as f
from tclustering.fsp import FSP
from tclustering.sampleSet import SampleSet
from tclustering.trainingSet import TrainingSet
# from tclustering.cluster import Cluster


# checked
class TestFrequency(unittest.TestCase):
    def test_compare_patter(self):
        self.assertTrue(f.compare_patter(['A'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['C'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['D'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['E'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'D'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['C', 'D'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['C', 'F'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['D', 'F'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['E', 'F'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E', 'F'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'X', 'B', 'C', 'E', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['C'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['D'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['E'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'D'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['C', 'D'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['C', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['E', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F']))
        self.assertTrue(f.compare_patter(['A'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['C'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['D'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['E'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'D'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['C', 'D'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['C', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['D', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['E', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['C'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['D'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertFalse(f.compare_patter(['E'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['A', 'C'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['A', 'D'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertFalse(f.compare_patter(['A', 'E'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['C', 'D'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['C', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['D', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertFalse(f.compare_patter(['E', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertFalse(f.compare_patter(['A', 'E', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z']))
        self.assertTrue(f.compare_patter(['A'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['C'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertFalse(f.compare_patter(['D'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['E'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertFalse(f.compare_patter(['A', 'D'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertFalse(f.compare_patter(['C', 'D'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['C', 'F'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertFalse(f.compare_patter(['D', 'F'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['E', 'F'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E', 'F'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertFalse(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'Y', 'C', 'E', 'F', 'F']))
        self.assertTrue(f.compare_patter(['A'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['C'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['D'], ['A', 'E', 'B', 'F']))
        self.assertTrue(f.compare_patter(['E'], ['A', 'E', 'B', 'F']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['A', 'C'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['A', 'D'], ['A', 'E', 'B', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E'], ['A', 'E', 'B', 'F']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['C', 'D'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['C', 'F'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['D', 'F'], ['A', 'E', 'B', 'F']))
        self.assertTrue(f.compare_patter(['E', 'F'], ['A', 'E', 'B', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E', 'F'], ['A', 'E', 'B', 'F']))
        self.assertFalse(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'E', 'B', 'F']))
        self.assertTrue(f.compare_patter(['A'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['C'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['D'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertTrue(f.compare_patter(['E'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['A', 'C'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['A', 'D'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['C', 'D'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['C', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['D', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertTrue(f.compare_patter(['E', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertFalse(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F']))
        self.assertTrue(f.compare_patter(['A'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['C'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['D'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['E'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'C'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'D'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertFalse(f.compare_patter(['C', 'D'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['C', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['D', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['E', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertTrue(f.compare_patter(['A', 'E', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))
        self.assertFalse(f.compare_patter(['A', 'C', 'D', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']))

    def test_compare_pattern(self):
        pattern_len_1 = [['A'], ['C'], ['D'], ['E'], ['F']]
        pattern_len_2 = [['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'], ['C', 'D'], ['C', 'F'],
                         ['D', 'F'], ['E', 'F']]
        pattern_clo = [['A', 'E', 'F'], ['A', 'C', 'D', 'F']]
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'X', 'B', 'C', 'E', 'D', 'F']), 5)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'X', 'B', 'C', 'E', 'D', 'F']), 8)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'X', 'B', 'C', 'E', 'D', 'F']), 2)
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'E', 'C', 'Y', 'D', 'F']), 5)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'E', 'C', 'Y', 'D', 'F']), 8)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'E', 'C', 'Y', 'D', 'F']), 2)
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'Z', 'C', 'D', 'B', 'E', 'F']), 5)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'Z', 'C', 'D', 'B', 'E', 'F']), 8)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'Z', 'C', 'D', 'B', 'E', 'F']), 2)
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'B', 'C', 'D', 'F', 'Z']), 4)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'B', 'C', 'D', 'F', 'Z']), 6)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'B', 'C', 'D', 'F', 'Z']), 1)
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'Y', 'C', 'E', 'F', 'F']), 4)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'Y', 'C', 'E', 'F', 'F']), 5)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'Y', 'C', 'E', 'F', 'F']), 1)
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'E', 'B', 'F']), 3)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'E', 'B', 'F']), 3)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'E', 'B', 'F']), 1)
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'X', 'E', 'Y', 'Z', 'F']), 3)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'X', 'E', 'Y', 'Z', 'F']), 3)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'X', 'E', 'Y', 'Z', 'F']), 1)
        self.assertEqual(f.compare_pattern(pattern_len_1, ['A', 'B', 'X', 'D', 'C', 'E', 'F']), 5)
        self.assertEqual(f.compare_pattern(pattern_len_2, ['A', 'B', 'X', 'D', 'C', 'E', 'F']), 7)
        self.assertEqual(f.compare_pattern(pattern_clo, ['A', 'B', 'X', 'D', 'C', 'E', 'F']), 1)

    def test_compare_mult_pattern(self):
        mult_pattern = [[['A'], ['C'], ['D'], ['E'], ['F']], [['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'],
                        ['C', 'D'], ['C', 'F'], ['D', 'F'], ['E', 'F']], [['A', 'E', 'F'], ['A', 'C', 'D', 'F']]]
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'X', 'B', 'C', 'E', 'D', 'F']), [5, 8, 2])
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'E', 'C', 'Y', 'D', 'F']), [5, 8, 2])
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'Z', 'C', 'D', 'B', 'E', 'F']), [5, 8, 2])
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'B', 'C', 'D', 'F', 'Z']), [4, 6, 1])
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'Y', 'C', 'E', 'F', 'F']), [4, 5, 1])
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'E', 'B', 'F']), [3, 3, 1])
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'X', 'E', 'Y', 'Z', 'F']), [3, 3, 1])
        self.assertEqual(f.compare_mult_pattern(mult_pattern, ['A', 'B', 'X', 'D', 'C', 'E', 'F']), [5, 7, 1])

    def test_compare_all(self):
        mult_pattern = [[['A'], ['C'], ['D'], ['E'], ['F']], [['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'],
                        ['C', 'D'], ['C', 'F'], ['D', 'F'], ['E', 'F']], [['A', 'E', 'F'], ['A', 'C', 'D', 'F']]]
        traces = [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'],
                  ['A', 'Z', 'C', 'D', 'B', 'E', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z'], ['A', 'Y', 'C', 'E', 'F', 'F'],
                  ['A', 'E', 'B', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']]
        result = [[5, 8, 2], [5, 8, 2], [5, 8, 2], [4, 6, 1], [4, 5, 1], [3, 3, 1], [3, 3, 1], [5, 7, 1]]
        self.assertEqual(f.compare_all(mult_pattern, traces), result)

    def test_in_cluster(self):
        mult_pattern = [[['A'], ['C'], ['D'], ['E'], ['F']], [['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'],
                        ['C', 'D'], ['C', 'F'], ['D', 'F'], ['E', 'F']], [['A', 'E', 'F'], ['A', 'C', 'D', 'F']]]
        traces = [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'],
                  ['A', 'Z', 'C', 'D', 'B', 'E', 'F'], ['A', 'B', 'C', 'D', 'F', 'Z'], ['A', 'Y', 'C', 'E', 'F', 'F'],
                  ['A', 'E', 'B', 'F'], ['A', 'X', 'E', 'Y', 'Z', 'F'], ['A', 'B', 'X', 'D', 'C', 'E', 'F']]
        thresholds = [4, 5, 1]
        result = [True, True, True, True, True, False, False, True]
        self.assertEqual(f.in_cluster(mult_pattern, traces, thresholds), result)


# checked
class TestFsp(unittest.TestCase):

    def test_mapping_dict(self):
        labeling_training_set = [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'],
                                 ['A', 'Z', 'C', 'D', 'B', 'E', 'F']]
        mapping_dict_result = FSP.mapping_dict(labeling_training_set)
        self.assertEqual(mapping_dict_result, {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'X': 7, 'Y': 8, 'Z': 9})

    def test_mapping(self):
        labeling_training_set = [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'],
                                 ['A', 'Z', 'C', 'D', 'B', 'E', 'F']]
        mapping_result = FSP.mapping(labeling_training_set)
        self.assertEqual(mapping_result, [[1, 7, 2, 3, 5, 4, 6], [1, 5, 3, 8, 4, 6], [1, 9, 3, 4, 2, 5, 6]])

    def test_write_text_input_file(self):
        labeling_training_set = [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'],
                                 ['A', 'Z', 'C', 'D', 'B', 'E', 'F']]
        file_path = FSP.write_text_input_file(labeling_training_set,
                                              os.path.join(os.getcwd(), 'training'), 'example.xes', ['CloFast', 0.8])
        with open(file_path, 'r') as file:
            result_text = file.read()
            file.close()

        result = '@CONVERTED_FROM_TEXT\n@ITEM=1=A\n@ITEM=2=B\n@ITEM=3=C\n@ITEM=4=D\n@ITEM=5=E\n@ITEM=6=F\n' \
                 '@ITEM=7=X\n@ITEM=8=Y\n@ITEM=9=Z\n@ITEM=-1=|\n' \
                 '1 -1 7 -1 2 -1 3 -1 5 -1 4 -1 6 -1 -2 \n' \
                 '1 -1 5 -1 3 -1 8 -1 4 -1 6 -1 -2 \n' \
                 '1 -1 9 -1 3 -1 4 -1 2 -1 5 -1 6 -1 -2 \n'
        self.assertEqual(result_text, result)

    def test_result(self):
        labeling_training_set = [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'],
                                 ['A', 'Z', 'C', 'D', 'B', 'E', 'F']]
        pattern_len_one = FSP(os.path.join(os.getcwd(), 'training'), 'SPAM',
                              labeling_training_set, 'example.xes', [0.8, 1, 1])
        pattern_len_two = FSP(os.path.join(os.getcwd(), 'training'), 'SPAM',
                              labeling_training_set, 'example.xes', [0.8, 2, 2])
        pattern_clo = FSP(os.path.join(os.getcwd(), 'training'), 'CloFast',
                          labeling_training_set, 'example.xes', [0.8])
        self.assertEqual(pattern_len_one.get_result(), [['A'], ['C'], ['D'], ['E'], ['F']])
        self.assertEqual(pattern_len_two.get_result(), [['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'],
                                                        ['C', 'D'], ['C', 'F'], ['D', 'F'], ['E', 'F']])
        self.assertEqual(pattern_clo.get_result(), [['A', 'E', 'F'], ['A', 'C', 'D', 'F']])


# checked
class TestSampleSet(unittest.TestCase):

    def test_sample_set(self):
        eventlog = xes_importer.apply(os.path.join(os.getcwd(), 'training', 'running-example.xes'))
        sample = SampleSet(eventlog, [0, 3, 5])
        sample_set = sample.get_sample_set()
        self.assertEqual(eventlog[0], sample_set[0])
        self.assertEqual(eventlog[3], sample_set[1])
        self.assertEqual(eventlog[5], sample_set[2])


# checked
class TestTrainingSet(unittest.TestCase):

    def test_training_set(self):
        eventlog = xes_importer.apply(os.path.join(os.getcwd(), 'training', 'running-example.xes'))
        sample = SampleSet(eventlog, [0, 3, 5])
        sample_set = sample.get_sample_set()
        training_set_help = TrainingSet(sample_set)
        training_set = training_set_help.get_training_set()
        self.assertEqual(len(training_set), 2)
        self.assertTrue(training_set[0] in sample_set)
        self.assertTrue(training_set[1] in sample_set)


'''
class TestClustering(unittest.TestCase):

    def test_clustering(self):
        cluster = Cluster('/Users/lentz/Desktop/trace-clustering/trace_clustering/training/running-example.xes',
                          [1, 2, 3, 4], ['Activity'], 0.8, ['SPAM', 'SPAM', 'CloFast'], [2, 1, 0])
        self.assertEqual(cluster.clustering, [True, True, True, True, True, True])

'''
if __name__ == 'main':
    unittest.main()
