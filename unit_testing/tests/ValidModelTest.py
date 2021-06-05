from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid import Glucose3Valid

from unittest import TestCase

class ValidModelTest(TestCase):

    def ValidModelOperation(self, model: PySATModel, expected_output: bool):
        valid_operation = Glucose3Valid()

        valid_operation.execute(model)
        is_valid = valid_operation.get_result()

        try:
            self.assertEqual(is_valid, expected_output)
            print("The result is the expected output: " + str(expected_output) + "\n")
        except:
            print("The result " + str(is_valid) + 
                " dont match with the expected output" + str(expected_output) + "\n")

    def setUp(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()
        
        transform = FmToPysat(fm)
        return transform.transform()

    def testCaseMandatory(self):
        print("----------Valid Model Test Case Mandatory----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory/mandatory.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseOptional(self):
        print("----------Valid Model Test Case Optional----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/optional/optional.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)
        
    def testCaseAlternative(self):
        print("----------Valid Model Test Case Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/alternative/alternative.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)
        
    def testCaseOr(self):
        print("----------Valid Model Test Case Or----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or/or.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)
        
    def testCaseExcludes(self):
        print("----------Valid Model Test Case Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/excludes/excludes.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)
        
    def testCaseRequires(self):
        print("----------Valid Model Test Case Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/requires/requires.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)
        
    def testCaseMandatoryOptional(self):
        print("----------Valid Model Test Case Mandatory/Optional----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-optional/mandatory-optional.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)
        
    def testCaseMandatoryOr(self):
        print("----------Valid Model Test Case Mandatory/Or----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-or/mandatory-or.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseMandatoryAlternative(self):
        print("----------Valid Model Test Case Mandatory/Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-alternative/mandatory-alternative.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseMandatoryRequires(self):
        print("----------Valid Model Test Case Mandatory/Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-requires/mandatory-requires.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseMandatoryExcludes(self):
        print("----------Valid Model Test Case Mandatory/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-excludes/mandatory-excludes.xml")
        expected_output = False
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseOptionalOr(self):
        print("----------Valid Model Test Case Optional/Or----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/optional-or/optional-or.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseOptionalAlternative(self):
        print("----------Valid Model Test Case Optional/Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/optional-alternative/optional-alternative.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseOrAlternative(self):
        print("----------Valid Model Test Case Or/Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or-alternative/or-alternative.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseOrRequires(self):
        print("----------Valid Model Test Case Or/Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or-requires/or-requires.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseOrExcludes(self):
        print("----------Valid Model Test Case Or/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or-excludes/or-excludes.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseAlternativeRequires(self):
        print("----------Valid Model Test Case Alternative/Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/alternative-requires/alternative-requires.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseAlternativeExcludes(self):
        print("----------Valid Model Test Case Alternative/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/alternative-excludes/alternative-excludes.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseRequiresExcludes(self):
        print("----------Valid Model Test Case Requires/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/requires-excludes/requires-excludes.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseAllRelationships(self):
        print("----------Valid Model Test Case All Relationships----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/allrelationships/allrelationships.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseAlternativeNoOr(self):
        print("----------Valid Model Test Case Alternative No Or----------")
        pysat_model = self.setUp("models/fama_test_suite/refinement/alternative-noOr/alternative-noOr.xml")
        expected_output = False
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseOrNoAlternative(self):
        print("----------Valid Model Test Case Or No Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/refinement/or-noAlternative/or-noAlternative.xml")
        expected_output = True
        self.ValidModelOperation(pysat_model, expected_output)	

    def testCaseAlternativeNoParentLastChild(self):
        print("----------Valid Model Test Case No Parent - Last Child Selected----------")
        pysat_model = self.setUp("models/fama_test_suite/refinement/alternative-noParentLastChild/alternative-noParentLastChild.xml")
        expected_output = False
        self.ValidModelOperation(pysat_model, expected_output)

    def testCaseAlternativeOddChildren(self):
        print("----------Valid Model Test Case No Parent - Last Child Selected----------")
        pysat_model = self.setUp("models/fama_test_suite/refinement/alternative-oddChildren/alternative-oddChildren.xml")
        expected_output = False
        self.ValidModelOperation(pysat_model, expected_output)

    def run(self):
        self.testCaseMandatory()
        self.testCaseOptional()
        self.testCaseAlternative()
        self.testCaseOr()
        self.testCaseExcludes()
        self.testCaseRequires()
        self.testCaseMandatoryOptional()
        self.testCaseMandatoryOr()
        self.testCaseMandatoryAlternative()
        self.testCaseMandatoryRequires()
        self.testCaseMandatoryExcludes()
        self.testCaseOptionalOr()
        self.testCaseOptionalAlternative()
        self.testCaseOrAlternative()
        self.testCaseOrRequires()
        self.testCaseOrExcludes()
        self.testCaseAlternativeRequires()
        self.testCaseAlternativeExcludes()
        self.testCaseRequiresExcludes()
        self.testCaseAllRelationships()
        self.testCaseAlternativeNoOr()
        self.testCaseOrNoAlternative()
        self.testCaseAlternativeNoParentLastChild()
        self.testCaseAlternativeOddChildren()
