from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation
from famapy.metamodels.fm_metamodel.models.feature_model import FeatureModel

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_false_optional_features import Glucose3FalseOptionalFeatures

from unittest import TestCase

class FalseOptionalFeaturesTest(TestCase):

    def FalseOptionalOperation(self, pysat_model: PySATModel, expected_output: list):
        false_optional_features_operation = Glucose3FalseOptionalFeatures()

        false_optional_features_operation.execute(pysat_model)
        false_optional_features = false_optional_features_operation.get_false_optional_features()

        try:
            self.assertEqual(false_optional_features, expected_output)
            print("The result is the expected output: " + str(false_optional_features) + "\n")
        except:
            print("The result " + str(false_optional_features) + 
                " dont match with the expected output" + str(expected_output) + "\n")

    def setUp(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCase1(self):
        print("----------False Optional Features Test Case 1----------")
        pysat_model = self.setUp("../models/fama_test_suite/error-guessing/false-optional-features/case1/fof-case1.xml")
        expected_output = ["C"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase2(self):
        print("----------False Optional Features Test Case 2----------")
        pysat_model = self.setUp("../models/fama_test_suite/error-guessing/false-optional-features/case2/fof-case2.xml")
        expected_output = ["C","D"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase3(self):
        print("----------False Optional Features Test Case 3----------")
        pysat_model = self.setUp("../models/fama_test_suite/error-guessing/false-optional-features/case3/fof-case3.xml")
        expected_output = ["C","D"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase4(self):
        print("----------False Optional Features Test Case 4----------")
        pysat_model = self.setUp("../models/fama_test_suite/error-guessing/false-optional-features/case4/fof-case4.xml")
        expected_output = ["C"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase5(self):
        print("----------False Optional Features Test Case 5----------")
        pysat_model = self.setUp("../models/fama_test_suite/error-guessing/false-optional-features/case5/fof-case5.xml")
        expected_output = ["C"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase6(self):
        print("----------False Optional Features Test Case 6----------")
        pysat_model = self.setUp("../models/fama_test_suite/error-guessing/false-optional-features/case6/fof-case6.xml")
        expected_output = ["B","E"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def run(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()
        self.testCase4()
        self.testCase5()
        self.testCase6()
