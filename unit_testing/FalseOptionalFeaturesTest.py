import unittest

from famapy.metamodels.fm_metamodel.transformations.xml_reader import XMLReader

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_false_optional_features import Glucose3FalseOptionalFeatures


class FalseOptionalFeaturesTest(unittest.TestCase):

    def FalseOptionalOperation(self, pysat_model: PySATModel, expected_output: list):
        false_optional_features_operation = Glucose3FalseOptionalFeatures()

        false_optional_features_operation.execute(pysat_model)
        false_optional_features = false_optional_features_operation.get_false_optional_features()

        self.assertEqual(false_optional_features, expected_output)

    def load_model(self, model_path):
        xmlreader = XMLReader(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCase1(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case1/fof-case1.xml")
        expected_output = ["C"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase2(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case2/fof-case2.xml")
        expected_output = ["C","D"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase3(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case3/fof-case3.xml")
        expected_output = ["C","D"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase4(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case4/fof-case4.xml")
        expected_output = ["C"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase5(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case5/fof-case5.xml")
        expected_output = ["C"]
        self.FalseOptionalOperation(pysat_model, expected_output)

    def testCase6(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case6/fof-case6.xml")
        expected_output = ["B","E"]
        self.FalseOptionalOperation(pysat_model, expected_output)


if __name__ == '__main__':
    unittest.main()
