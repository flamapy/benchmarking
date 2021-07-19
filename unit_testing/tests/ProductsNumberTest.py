from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from unittest import TestCase

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_products_number import Glucose3ProductsNumber

class ProductsNumberTest(TestCase):

    def ProductsOperation(self, model: PySATModel, expected_output: bool):
        products_operation = Glucose3ProductsNumber()

        products_operation.execute(model)
        products = products_operation.get_products_number()

        try:
            self.assertEqual(products, expected_output)
            print("The result is the expected output: " + str(expected_output) + "\n")
        except:
            print("The result " + str(products) + 
                " dont match with the expected output " + str(expected_output) + "\n")

    def setUp(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()
        
        transform = FmToPysat(fm)
        return transform.transform()

    def testCaseMandatory(self):
        print("----------Products Number Test Case Mandatory----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/mandatory/mandatory.xml")
        expected_output = 1
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptional(self):
        print("----------Products Number Test Case Optional----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/optional/optional.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseAlternative(self):
        print("----------Products Number Test Case Alternative----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/alternative/alternative.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseOr(self):
        print("----------Products Number Test Case Or----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/or/or.xml")
        expected_output = 3
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseExcludes(self):
        print("----------Products Number Test Case Excludes----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/excludes/excludes.xml")
        expected_output = 3
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseRequires(self):
        print("----------Products Number Test Case Requires----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/requires/requires.xml")
        expected_output = 3
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseMandatoryOptional(self):
        print("----------Products Number Test Case Mandatory/Optional----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/mandatory-optional/mandatory-optional.xml")
        expected_output = 4
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseMandatoryOr(self):
        print("----------Products Number Test Case Mandatory/Or----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/mandatory-or/mandatory-or.xml")
        expected_output = 9
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryAlternative(self):
        print("----------Products Number Test Case Mandatory/Alternative----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/mandatory-alternative/mandatory-alternative.xml")
        expected_output = 4
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryRequires(self):
        print("----------Products Number Test Case Mandatory/Requires----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/mandatory-requires/mandatory-requires.xml")
        expected_output = 1
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryExcludes(self):
        print("----------Products Number Test Case Mandatory/Excludes----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/mandatory-excludes/mandatory-excludes.xml")
        expected_output = 0
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalOr(self):
        print("----------Products Number Test Case Optional/Or----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/optional-or/optional-or.xml")
        expected_output = 20
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalAlternative(self):
        print("----------Products Number Test Case Optional/Alternative----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/optional-alternative/optional-alternative.xml")
        expected_output = 9
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrAlternative(self):
        print("----------Products Number Test Case Or/Alternative----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/or-alternative/or-alternative.xml")
        expected_output = 20
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrRequires(self):
        print("----------Products Number Test Case Or/Requires----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/or-requires/or-requires.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrExcludes(self):
        print("----------Products Number Test Case Or/Excludes----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/or-excludes/or-excludes.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeRequires(self):
        print("----------Products Number Test Case Alternative/Requires----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/alternative-requires/alternative-requires.xml")
        expected_output = 1
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeExcludes(self):
        print("----------Products Number Test Case Alternative/Excludes----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/alternative-excludes/alternative-excludes.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseRequiresExcludes(self):
        print("----------Products Number Test Case Requires/Excludes----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/requires-excludes/requires-excludes.xml")
        expected_output = 2
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAllRelationships(self):
        print("----------Products Number Test Case All Relationships----------")
        pysat_model = self.setUp("../models/fama_test_suite/relationships/allrelationships/allrelationships.xml")
        expected_output = 4
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeOddChildren(self):
        print("----------Products Number Test Case Alternative Odd Children----------")
        pysat_model = self.setUp("../models/fama_test_suite/refinement/alternative-oddChildren/alternative-oddChildren.xml")
        expected_output = 0
        self.ProductsOperation(pysat_model, expected_output)


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
        self.testCaseAlternativeOddChildren()

