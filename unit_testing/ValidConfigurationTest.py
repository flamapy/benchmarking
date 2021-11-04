import unittest

from famapy.metamodels.fm_metamodel.transformations.xml_reader import XMLReader

from famapy.core.models import Configuration

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid_configuration import Glucose3ValidConfiguration


class ValidConfigurationTest(unittest.TestCase):

    def ValidConfigurationOperation(self, pysat_model: PySATModel, configuration: Configuration, expected_output: bool):
        valid_configuration_operation = Glucose3ValidConfiguration()

        valid_configuration_operation.set_configuration(configuration)
        valid_configuration_operation.execute(pysat_model)
        is_valid = valid_configuration_operation.is_valid()

        self.assertEqual(is_valid, expected_output)

    def setUp(self):
        xmlreader = XMLReader("models/fama_test_suite/relationships/allrelationships/allrelationships.xml")
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        features = fm.get_features()

        self.A = features[0]
        self.B = features[1]
        self.C = features[4]
        self.D = features[2]
        self.E = features[3]
        self.F = features[5]
        self.G = features[6]

        self.pysat_model = transform.transform()

    def testCase1(self):
        configuration = Configuration({self.A:True, self.B:True, self.C:True})
        expected_output = True
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)

    def testCase2(self):
        configuration = Configuration({self.E:True, self.F:False})
        expected_output = False
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)

    def testCase3(self):
        configuration = Configuration({self.E:True, self.F:True})
        expected_output = True
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)

    def testCase4(self):
        configuration = Configuration({self.E:False, self.F:False})
        expected_output = True
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)

    def testCase5(self):
        configuration = Configuration({self.D:False, self.G:True})
        expected_output = True
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)

    def testCase6(self):
        configuration = Configuration({self.D:True, self.G:True})
        expected_output = False
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)

    def testCase7(self):
        configuration = Configuration({self.D:True, self.G:False})
        expected_output = True
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)

    def testCase8(self):
        configuration = Configuration({self.B:False})
        expected_output = False
        self.ValidConfigurationOperation(self.pysat_model, configuration, expected_output)


if __name__ == '__main__':
    unittest.main()
