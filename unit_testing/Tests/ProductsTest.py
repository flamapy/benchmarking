from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_products import Glucose3Products

from unittest import TestCase

class ProductsTest(TestCase):

    def ProductsOperation(self, model: PySATModel, expected_output: bool):
        products_operation = Glucose3Products()

        products_operation.execute(model)
        products = products_operation.get_products()

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
        print("----------Products Test Case Mandatory----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory/mandatory.fama")
        expected_output = [["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptional(self):
        print("----------Products Test Case Optional----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/optional/optional.fama")
        expected_output = [["A"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseAlternative(self):
        print("----------Products Test Case Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/alternative/alternative.fama")
        expected_output = [["A","B"],["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseOr(self):
        print("----------Products Test Case Or----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or/or.fama")
        expected_output = [["A","B"],["A","B","C"],["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseExcludes(self):
        print("----------Products Test Case Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/excludes/excludes.fama")
        expected_output = [["A"],["A","C"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseRequires(self):
        print("----------Products Test Case Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/requires/requires.fama")
        expected_output = [["A"],["A","C"],["A","B","C"]]
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseMandatoryOptional(self):
        print("----------Products Test Case Mandatory/Optional----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-optional/mandatory-optional.fama")
        expected_output = [["A","B"],["A","B","C","E"],["A","B","D","C","E"],["A","B","D"]]
        self.ProductsOperation(pysat_model, expected_output)
        
    def testCaseMandatoryOr(self):
        print("----------Products Test Case Mandatory/Or----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-or/mandatory-or.fama")
        expected_output = [["A","B","E","C"],["A","B","E","F","C"],["A","B","E","F","C","D","G"],
                            ["A","B","F","C"],["A","B","E","C","D","G"],["A","B","E","D","G"],
                            ["A","B","E","F","D","G"],["A","B","F","C","D","G"],
                            ["A","B","F","D","G"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryAlternative(self):
        print("----------Products Test Case Mandatory/Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-alternative/mandatory-alternative.fama")
        expected_output = [["A","B","E","D"],["A","B","E","C","G"],["A","B","F","C","G"],["A","B","F","D"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryRequires(self):
        print("----------Products Test Case Mandatory/Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-requires/mandatory-requires.fama")
        expected_output = [["A","B","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryExcludes(self):
        print("----------Products Test Case Mandatory/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/mandatory-excludes/mandatory-excludes.fama")
        expected_output = []
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalOr(self):
        print("----------Products Test Case Optional/Or----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/optional-or/optional-or.fama")
        expected_output = [["A","C"],["A","C","D"],["A","C","D","G"],["A","C","G"],
                            ["A","B","F","C","G"],["A","B","E","F","C","G"],["A","B","E","F","C"],
                            ["A","B","E","F","C","D"],["A","B","E","C","D"],["A","B","F","C","D"],
                            ["A","B","F","C","D","G"],["A","B","F","D"],["A","B","F","C"],
                            ["A","B","E","C"],["A","B","E","C","G"],["A","B","E","C","D","G"],
                            ["A","B","E","D"],["A","B","E","F","D"],["A","B","E","F","C","D","G"],
                            ["A","D"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalAlternative(self):
        print("----------Products Test Case Optional/Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/optional-alternative/optional-alternative.fama")
        expected_output = [["A","C"],["A","D"],["A","B","E","C"],["A","B","E","D"],
                            ["A","B","E","D","G"],["A","B","F","D","G"],["A","B","F","D"],
                            ["A","D","G"],["A","B","F","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrAlternative(self):
        print("----------Products Test Case Or/Alternative----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or-alternative/or-alternative.fama")
        expected_output = [["A","C","D"],["A","C","D","E","H"],["A","C","D","E","I"],
                            ["A","B","F","D","E","I"],["A","B","F","G","D","E","I"],
                            ["A","B","F","G","D"],["A","B","G","D"],["A","B","G","D","E","I"],
                            ["A","B","F","D"],["A","B","F","E","I"],["A","B","F","E","H"],
                            ["A","B","F","D","E","H"],["A","C","E","H"],["A","C","E","I"],
                            ["A","B","G","E","I"],["A","B","F","G","E","I"],
                            ["A","B","F","G","D","E","H"],["A","B","F","G","E","H"],
                            ["A","B","G","E","H"],["A","B","G","D","E","H"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrRequires(self):
        print("----------Products Test Case Or/Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or-requires/or-requires.fama")
        expected_output = [["A","C"],["A","C","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrExcludes(self):
        print("----------Products Test Case Or/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/or-excludes/or-excludes.fama")
        expected_output = [["A","C"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeRequires(self):
        print("----------Products Test Case Alternative/Requires----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/alternative-requires/alternative-requires.fama")
        expected_output = [["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeExcludes(self):
        print("----------Products Test Case Alternative/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/alternative-excludes/alternative-excludes.fama")
        expected_output = [["A","C"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseRequiresExcludes(self):
        print("----------Products Test Case Requires/Excludes----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/requires-excludes/requires-excludes.fama")
        expected_output = [["A"],["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAllRelationships(self):
        print("----------Products Test Case All Relationships----------")
        pysat_model = self.setUp("models/fama_test_suite/relationships/allrelationships/allrelationships.fama")
        expected_output = [["A","B","D"],["A","B","D","C","F"],["A","B","E","C","F"],
                            ["A","B","E","C","F","G"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeOddChildren(self):
        print("----------Products Test Case Alternative Odd Children----------")
        pysat_model = self.setUp("models/fama_test_suite/refinement/alternative-oddChildren/alternative-oddChildren.fama")
        expected_output = []
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
