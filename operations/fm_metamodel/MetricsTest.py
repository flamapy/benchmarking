import unittest

from parameterized import parameterized

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader


INPUT_MODELS_FOLDER = 'models/featureide/'

# 0 filename
# 1 nof features 
# 2 nof constraints
# 3 root name
# 4 nof ors
# 5 nof alternatives
# 6 nof abstract features
# 7 nof leaf features
# 8 nof core features
MODELS = [['pizzas', 12, 1, 'Pizza', 1, 2, 1, 8, 4],
          ['wget', 17, 0, 'wget', 0, 1, 0, 15, 2],
          ['tankwar', 37, 0, 'TankWar', 2, 6, 0, 26, 7],
          ['mobilemedia2', 43, 3, 'MobileMedia2', 4, 3, 0, 31, 10],
          ['jHipster', 45, 13, 'JHipster', 0, 10, 13, 32, 0],
          ['WeaFQAs', 179, 7, 'FQAs', 13, 23, 0, 124, 1],
          ['busybox-1.18.0', 854, 67, 'root', 0, 8, 0, 683, 20],
          ['embtoolkit', 1179, 167, 'root', 0, 70, 0, 966, 78],
          ['ea2468', 1408, 1281, 'root', 0, 12, 0, 1069, 4],
          ['uClinux-distribution', 1580, 247, 'root', 0, 10, 0, 1368, 6],
          ['automotive2_1', 14010, 624, 'N_379925076__F_91527E35945B', 106, 1010, 0, 12615, 1394],
          ['linux-2.6.33.3', 6467, 7650, 'root', 2, 39, 0, 5523, 53]]


class FMMetricsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reader = FeatureIDEReader
        cls.ext = '.xml'
        cls.input_folder = INPUT_MODELS_FOLDER

    @parameterized.expand([m[:2] for m in MODELS])
    def test_nof_features(self, fm_input, nof_features):
        fm = self.reader(self.input_folder + fm_input + self.ext).transform()
        self.assertEqual(len(fm.get_features()), nof_features)

    @parameterized.expand([[m[0], m[2]] for m in MODELS])
    def test_nof_constraints(self, fm_input, nof_constraints):
        fm = self.reader(self.input_folder + fm_input + self.ext).transform()
        self.assertEqual(len(fm.get_constraints()), nof_constraints)

    @parameterized.expand([[m[0], m[3]] for m in MODELS])
    def test_root_feature(self, fm_input, root_feature):
        fm = self.reader(self.input_folder + fm_input + self.ext).transform()
        self.assertEqual(fm.root.name, root_feature)
        self.assertIsNone(fm.root.get_parent())
    
    @parameterized.expand([[m[0], m[4]] for m in MODELS])
    def test_nof_or_groups(self, fm_input, nof_or_groups):
        fm = self.reader(self.input_folder + fm_input + self.ext).transform()
        result_or_groups = sum(map(lambda f: f.is_or_group(), fm.get_features()))
        self.assertEqual(result_or_groups, nof_or_groups)

    @parameterized.expand([[m[0], m[5]] for m in MODELS])
    def test_nof_alternative_groups(self, fm_input, nof_alternative_groups):
        fm = self.reader(self.input_folder + fm_input + self.ext).transform()
        result_alternative_groups = sum(map(lambda f: f.is_alternative_group(), fm.get_features()))
        self.assertEqual(result_alternative_groups, nof_alternative_groups)

    @parameterized.expand([[m[0], m[6]] for m in MODELS])
    def test_nof_abstract_features(self, fm_input, nof_abstract_features):
        fm = self.reader(self.input_folder + fm_input + self.ext).transform()
        result_abstract_features = sum(map(lambda f: f.is_abstract, fm.get_features()))
        self.assertEqual(result_abstract_features, nof_abstract_features)
    
    @parameterized.expand([[m[0], m[7]] for m in MODELS])
    def test_nof_leaf_features(self, fm_input, nof_leaf_features):
        fm = self.reader(self.input_folder + fm_input + self.ext).transform()
        result_leaf_features = sum(map(lambda f: f.is_leaf(), fm.get_features()))
        self.assertEqual(result_leaf_features, nof_leaf_features)


if __name__ == '__main__':
    unittest.main()
