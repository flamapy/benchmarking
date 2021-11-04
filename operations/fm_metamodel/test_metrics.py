import unittest

from parameterized import parameterized

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader


INPUT_MODELS_FOLDER = '../../models/featureide/'

# filename, nof_features, nof_constraints, root_name, nof_ors, nof_alternatives, nof_core_features
MODELS = [['pizzas', 12, 1, 'Pizza', 1, 2, 4],
          ['wget', 17, 0, 'wget', 0, 1, 2],
          ['tankwar', 37, 0, 'TankWar', 2, 6, 7],
          ['mobilemedia2', 43, 3, 'MobileMedia2', 4, 3, 10],
          ['jHipster', 45, 13, 'JHipster', 0, 10, 0],
          ['WeaFQAs', 179, 7, 'FQAs', 13, 23, 1],
          ['busybox-1.18.0', 854, 67, 'root', 0, 8, 20],
          ['embtoolkit', 1179, 167, 'root', 0, 70, 78],
          ['ea2468', 1408, 1281, 'root', 0, 12, 4],
          ['uClinux-distribution', 1580, 247, 'root', 0, 10, 6],
          ['automotive2_1', 14010, 624, 'N_379925076__F_91527E35945B', 106, 1010, 1394],
          ['linux-2.6.33.3', 6467, 7650, 'root', 2, 39, 53]]
          

class FMMetricsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reader = FeatureIDEReader
        cls.ext = '.xml'
        cls.input_folder = INPUT_MODELS_FOLDER

    @parameterized.expand([m[:2] for m in MODELS])
    def test_nof_features(self, fm_input, nof_features):
        reader = self.reader(self.input_folder + fm_input + self.ext)
        fm = reader.transform()
        self.assertEqual(len(fm.get_features()), nof_features)

    @parameterized.expand([[m[0], m[2]] for m in MODELS])
    def test_nof_constraints(self, fm_input, nof_constraints):
        reader = self.reader(self.input_folder + fm_input + self.ext)
        fm = reader.transform()
        self.assertEqual(len(fm.get_constraints()), nof_constraints)

    @parameterized.expand([[m[0], m[3]] for m in MODELS])
    def test_root_feature(self, fm_input, root_feature):
        reader = self.reader(self.input_folder + fm_input + self.ext)
        fm = reader.transform()
        self.assertEqual(fm.root.name, root_feature)
        self.assertIsNone(fm.root.get_parent())
    
    @parameterized.expand([[m[0], m[4]] for m in MODELS])
    def test_nof_or_groups(self, fm_input, nof_or_groups):
        reader = self.reader(self.input_folder + fm_input + self.ext)
        fm = reader.transform()
        result_or_groups = sum(map(lambda f: f.is_or_group(), fm.get_features()))
        self.assertEqual(result_or_groups, nof_or_groups)

    @parameterized.expand([[m[0], m[5]] for m in MODELS])
    def test_nof_alternative_groups(self, fm_input, nof_alternative_groups):
        reader = self.reader(self.input_folder + fm_input + self.ext)
        fm = reader.transform()
        result_alternative_groups = sum(map(lambda f: f.is_alternative_group(), fm.get_features()))
        self.assertEqual(result_alternative_groups, nof_alternative_groups)

if __name__ == '__main__':
    unittest.main()
