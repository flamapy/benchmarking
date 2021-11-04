import unittest

from famapy.metamodels.fm_metamodel.transformations.xml_reader import XMLReader

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_error_detection import Glucose3ErrorDetection


class ErrorDetectionTest(unittest.TestCase):

    def ErrorDetectionOperation(self, model: PySATModel, expected_output: list):
        error_detection_operation = Glucose3ErrorDetection()

        error_detection_operation.execute(model)
        detections = error_detection_operation.get_errors_messages()

        self.assertEqual(detections, expected_output)

    def load_model(self, model_path):
        xmlreader = XMLReader(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCase1(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case1/df-case1.xml")
        expected_output = ["Dead features: ['D']", "False optional features: ['E']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase2(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case2/df-case2.xml")
        expected_output = ["Dead features: ['E']", "False optional features: ['D']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase3(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case3/df-case3.xml")
        expected_output = ["Dead features: ['D']", "False optional features: ['E']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase4(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case4/df-case4.xml")
        expected_output = ["Dead features: ['C']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase5(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case5/df-case5.xml")
        expected_output = ["The model is void, so haven't any product"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase6(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case6/df-case6.xml")
        expected_output = ["Dead features: ['B']", "False optional features: ['C']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase7(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case7/df-case7.xml")
        expected_output =["The model is void, so haven't any product"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase8(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/dead-features/case8/df-case8.xml")
        expected_output = ["Dead features: ['B']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase9(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case1/fof-case1.xml")
        expected_output = ["False optional features: ['C']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase10(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case2/fof-case2.xml")
        expected_output = ["Dead features: ['E']", "False optional features: ['C', 'D']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase11(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case3/fof-case3.xml")
        expected_output = ["False optional features: ['C', 'D']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase12(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case4/fof-case4.xml")
        expected_output = ["Dead features: ['B']", "False optional features: ['C']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase13(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case5/fof-case5.xml")
        expected_output = ["False optional features: ['C']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase14(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/false-optional-features/case6/fof-case6.xml")
        expected_output = ["Dead features: ['F']", "False optional features: ['B', 'E']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase15(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/redundancies/case1/r-case1.xml")
        expected_output = ["Redundancies: ['B requires C']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)

    def testCase16(self):
        pysat_model = self.load_model("models/fama_test_suite/error-guessing/redundancies/case2/r-case2.xml")
        expected_output = ["False optional features: ['B']", "Redundancies: ['D requires B']"]
        self.ErrorDetectionOperation(pysat_model, expected_output)


if __name__ == '__main__':
    unittest.main()
