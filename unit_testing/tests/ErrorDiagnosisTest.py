from unittest import TestCase

from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation
from famapy.metamodels.fm_metamodel.models.feature_model import FeatureModel

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_error_diagnosis import Glucose3ErrorDiagnosis

class ErrorDiagnosisTest(TestCase):

    def ErrorDiagnosisOperation(self, pysat_model: PySATModel, expected_output: list):
        error_diagnosis_operation = Glucose3ErrorDiagnosis()

        error_diagnosis_operation.execute(pysat_model)
        diagnosis = error_diagnosis_operation.get_diagnosis_messages()

        try:
            self.assertEqual(diagnosis, expected_output)
            print("The result is the expected output: " + str(diagnosis) + "\n")
        except:
            print("The result " + str(diagnosis) + 
                " dont match with the expected output " + str(expected_output) + "\n")

    def setUp(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCase1(self):
        print("----------Error Diagnosis Test Case 1----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case1/df-case1.xml")
        expected_output = ["For dead feature D: B excludes D"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def testCase2(self):
        print("----------Error Diagnosis Test Case 2----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case2/df-case2.xml")
        expected_output = ["For false optional feature D: B requires D"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)
        
    def testCase3(self):
        print("----------Error Diagnosis Test Case 3----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case3/df-case3.xml")
        expected_output = ["For dead feature D: D excludes B"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)
        
    def testCase4(self):
        print("----------Error Diagnosis Test Case 4----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case4/df-case4.xml")
        expected_output = ["For dead feature C: B excludes C"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)
        
    def testCase5(self):
        print("----------Error Diagnosis Test Case 5----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case5/df-case5.xml")
        expected_output = ["B excludes C"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)
        
    def testCase6(self):
        print("----------Error Diagnosis Test Case 6----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case6/df-case6.xml")
        expected_output = ["For dead feature B: B requires C", "For false optional feature C: B requires C"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)
        
    def testCase7(self):
        print("----------Error Diagnosis Test Case 7----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case7/df-case7.xml")
        expected_output =["B excludes C"] 
        self.ErrorDiagnosisOperation(pysat_model, expected_output)
        
    def testCase8(self):
        print("----------Error Diagnosis Test Case 8----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/dead-features/case8/df-case8.xml")
        expected_output = ["For dead feature B: B excludes C", "For dead feature B: B requires C"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def testCase9(self):
        print("----------Error Diagnosis Test Case 9----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/false-optional-features/case1/fof-case1.xml")
        expected_output = ["For false optional feature C: B requires C"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def testCase10(self):
        print("----------Error Diagnosis Test Case 10----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/false-optional-features/case2/fof-case2.xml")
        expected_output = ["For false optional feature D: B requires D"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def testCase11(self):
        print("----------Error Diagnosis Test Case 11----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/false-optional-features/case3/fof-case3.xml")
        expected_output = ["For false optional feature D: B requires D"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def testCase12(self):
        print("----------Error Diagnosis Test Case 12----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/false-optional-features/case4/fof-case4.xml")
        expected_output = ["For dead feature B: B requires C", "For false optional feature C: B requires C"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def testCase13(self):
        print("----------Error Diagnosis Test Case 13----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/false-optional-features/case5/fof-case5.xml")
        expected_output = ["For false optional feature C: B requires C"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def testCase14(self):
        print("----------Error Diagnosis Test Case 14----------")
        pysat_model = self.setUp("models/fama_test_suite/error-guessing/false-optional-features/case6/fof-case6.xml")
        expected_output = ["For dead feature F: D excludes F", "For false optional feature B: E requires B"]
        self.ErrorDiagnosisOperation(pysat_model, expected_output)

    def run(self):
        self.testCase1()
        self.testCase2()
        self.testCase3()
        self.testCase4()
        self.testCase5()
        self.testCase6()
        self.testCase7()
        self.testCase8()
        self.testCase9()
        self.testCase10()
        self.testCase11()
        self.testCase12()
        self.testCase13()
        self.testCase14()

