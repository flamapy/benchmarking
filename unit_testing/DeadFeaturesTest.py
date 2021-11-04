import unittest

from famapy.metamodels.fm_metamodel.transformations.xml_reader import XMLReader

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_dead_features import Glucose3DeadFeatures


class DeadFeaturesTest(unittest.TestCase):

    def DeadFeaturesOperation(self, model: PySATModel, expected_output: list):
        dead_features_operation = Glucose3DeadFeatures()

        dead_features_operation.execute(model)
        dead_features = dead_features_operation.get_dead_features()

        self.assertEqual(dead_features, expected_output)

    def load_model(self, model_path):
        xmlreader = XMLReader(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCase1(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case1/df-case1.xml")
        expected_output = ["D"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase2(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case2/df-case2.xml")
        expected_output = ["E"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase3(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case3/df-case3.xml")
        expected_output = ["D"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase4(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case4/df-case4.xml")
        expected_output = ["C"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase5(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case5/df-case5.xml")
        expected_output = ["A","B","C"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase6(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case6/df-case6.xml")
        expected_output = ["B"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase7(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case7/df-case7.xml")
        expected_output = ["A","B","C"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase8(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case8/df-case8.xml")
        expected_output = ["B"]
        self.DeadFeaturesOperation(pysat_model, expected_output)


if __name__ == '__main__':
    unittest.main()
