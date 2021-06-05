from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_core_features import Glucose3CoreFeatures

from unittest import TestCase

class CoreFeaturesTest(TestCase):

    def CoreFeaturesOperation(self, model: PySATModel, expected_output: list):
        core_features_operation = Glucose3CoreFeatures()

        core_features_operation.execute(model)
        core_features = core_features_operation.get_core_features()

        try:
            self.assertEqual(core_features, expected_output)
            print("The result is the expected output: " + str(core_features) + "\n")
        except:
            print("The result " + str(core_features) + 
                " dont match with the expected output" + str(expected_output) + "\n")

    def setUp(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCase1(self):
        print("----------Core Features Test Case 1----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/core-features/case1/cf-case1.xml")
        expected_output = ["A","B"]
        self.CoreFeaturesOperation(pysat_model, expected_output)

    def testCase2(self):
        print("----------Core Features Test Case 2----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/core-features/case2/cf-case2.xml")
        expected_output = ["A","B"]
        self.CoreFeaturesOperation(pysat_model, expected_output)

    def testCase3(self):
        print("----------Core Features Test Case 3----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/core-features/case3/cf-case3.xml")
        expected_output = ["A","B","C"]
        self.CoreFeaturesOperation(pysat_model, expected_output)

    def testCase4(self):
        print("----------Core Features Test Case 4----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/core-features/case4/cf-case4.xml")
        expected_output = ["A","B","C","E"]
        self.CoreFeaturesOperation(pysat_model, expected_output)

    def testCase5(self):
        print("----------Core Features Test Case 5----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/core-features/case5/cf-case5.xml")
        expected_output = ["A","B","C","D"]
        self.CoreFeaturesOperation(pysat_model, expected_output)

    def testCase6(self):
        print("----------Core Features Test Case 6----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/core-features/case6/cf-case6.xml")
        expected_output = []
        self.CoreFeaturesOperation(pysat_model, expected_output)

    def run(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()
        self.testCase4()
        self.testCase5()
        self.testCase6()
