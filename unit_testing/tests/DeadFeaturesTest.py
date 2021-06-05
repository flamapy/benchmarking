from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_dead_features import Glucose3DeadFeatures

from unittest import TestCase

class DeadFeaturesTest(TestCase):

    def DeadFeaturesOperation(self, model: PySATModel, expected_output: list):
        dead_features_operation = Glucose3DeadFeatures()

        dead_features_operation.execute(model)
        dead_features = dead_features_operation.get_dead_features()

        try:
            self.assertEqual(dead_features, expected_output)
            print("The result is the expected output: " + str(dead_features) + "\n")
        except:
            print("The result " + str(dead_features) + 
                " dont match with the expected output " + str(expected_output) + "\n")

    def setUp(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCase1(self):
        print("----------Dead features Test Case 1----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case1/df-case1.xml")
        expected_output = ["D"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def testCase2(self):
        print("----------Dead features Test Case 2----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case2/df-case2.xml")
        expected_output = ["E"]
        self.DeadFeaturesOperation(pysat_model, expected_output)
        
    def testCase3(self):
        print("----------Dead features Test Case 3----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case3/df-case3.xml")
        expected_output = ["D"]
        self.DeadFeaturesOperation(pysat_model, expected_output)
        
    def testCase4(self):
        print("----------Dead features Test Case 4----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case4/df-case4.xml")
        expected_output = ["C"]
        self.DeadFeaturesOperation(pysat_model, expected_output)
        
    def testCase5(self):
        print("----------Dead features Test Case 5----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case5/df-case5.xml")
        expected_output = ["A","B","C"]
        self.DeadFeaturesOperation(pysat_model, expected_output)
        
    def testCase6(self):
        print("----------Dead features Test Case 6----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case6/df-case6.xml")
        expected_output = ["B"]
        self.DeadFeaturesOperation(pysat_model, expected_output)
        
    def testCase7(self):
        print("----------Dead features Test Case 7----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case7/df-case7.xml")
        expected_output = ["A","B","C"]
        self.DeadFeaturesOperation(pysat_model, expected_output)
        
    def testCase8(self):
        print("----------Dead features Test Case 8----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case8/df-case8.xml")
        expected_output = ["B"]
        self.DeadFeaturesOperation(pysat_model, expected_output)

    def run(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()
        self.testCase4()
        self.testCase5()
        self.testCase6()
        self.testCase7()
        self.testCase8()  
