from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from unittest import TestCase

from famapy.core.models import Configuration

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_filter import Glucose3Filter

class FilterTest(TestCase):

    def ValidConfigurationOperation(self, pysat_model: PySATModel, configuration: Configuration, expected_output: bool):
        valid_configuration_operation = Glucose3Filter()

        valid_configuration_operation.set_configuration(configuration)
        valid_configuration_operation.execute(pysat_model)
        filter_products = valid_configuration_operation.get_filter_products()

        try:
            self.assertEqual(filter_products, expected_output)
            print("The result is the expected output: " + str(filter_products) + "\n")
        except:
            print("The result " + str(filter_products) + 
                " dont match with the expected output " + str(expected_output) + "\n")

    def setUp(self):
        xmlreader = XMLTransformation("../models/fama_test_suite/relationships/allrelationships/allrelationships.xml")
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return fm,transform.transform()

    def testCase1(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 1----------")
        expected_output = [["A", "B", "D", "C", "F"], ["A", "B", "E", "C", "F"], ["A", "B", "E", "C", "F", "G"]]
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def testCase2(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 2----------")
        expected_output = []
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def testCase3(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 3----------")
        expected_output = [["A", "B", "E", "C", "F"], ["A", "B", "E", "C", "F", "G"]]
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def testCase4(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 4----------")
        expected_output = [["A", "B", "D"]]
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def testCase5(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 5----------")
        expected_output = [["A", "B", "E", "C", "F", "G"]]
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def testCase6(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 6----------")
        expected_output = []
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def testCase7(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 7----------")
        expected_output = [["A", "B", "D"], ["A", "B", "D", "C", "F"]]
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def testCase8(self, pysat_model: PySATModel, configuration: Configuration):
        print("----------Filter Test Case 8----------")
        expected_output = []
        self.ValidConfigurationOperation(pysat_model, configuration, expected_output)

    def run(self):
        fm_model,pysat_model=self.setUp()
        features = fm_model.get_features()
        A = features[0]
        B = features[1]
        C = features[4]
        D = features[2]
        E = features[3]
        F = features[5]
        G = features[6]

        self.testCase1(pysat_model,Configuration({A:True,B:True,C:True}))
        self.testCase2(pysat_model,Configuration({E:True,F:False}))
        self.testCase3(pysat_model,Configuration({E:True,F:True}))
        self.testCase4(pysat_model,Configuration({E:False,F:False}))
        self.testCase5(pysat_model,Configuration({D:False,G:True}))
        self.testCase6(pysat_model,Configuration({D:True,G:True}))
        self.testCase7(pysat_model,Configuration({D:True,G:False}))
        self.testCase8(pysat_model,Configuration({B:False}))
