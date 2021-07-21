import unittest

from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.operations.glucose3_products import Glucose3Products


class ProductsTest(unittest.TestCase):

    def ProductsOperation(self, model: PySATModel, expected_output: bool):
        products_operation = Glucose3Products()

        products_operation.execute(model)
        products = products_operation.get_products()

        self.assertEqual(products, expected_output)

    def load_model(self, model_path):
        xmlreader = XMLTransformation(model_path)
        fm = xmlreader.transform()

        transform = FmToPysat(fm)
        return transform.transform()

    def testCaseMandatory(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory/mandatory.xml")
        expected_output = [["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptional(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/optional/optional.xml")
        expected_output = [["A"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/alternative/alternative.xml")
        expected_output = [["A","B"],["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOr(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/or/or.xml")
        expected_output = [["A","B"],["A","B","C"],["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/excludes/excludes.xml")
        expected_output = [["A"],["A","C"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseRequires(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/requires/requires.xml")
        expected_output = [["A"],["A","C"],["A","B","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryOptional(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-optional/mandatory-optional.xml")
        expected_output = [["A","B"],["A","B","C","E"],["A","B","D","C","E"],["A","B","D"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryOr(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-or/mandatory-or.xml")
        expected_output = [["A","B","E","C"],["A","B","E","F","C"],["A","B","E","F","C","D","G"],
                            ["A","B","F","C"],["A","B","E","C","D","G"],["A","B","E","D","G"],
                            ["A","B","E","F","D","G"],["A","B","F","C","D","G"],
                            ["A","B","F","D","G"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-alternative/mandatory-alternative.xml")
        expected_output = [["A","B","E","D"],["A","B","E","C","G"],["A","B","F","C","G"],["A","B","F","D"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryRequires(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-requires/mandatory-requires.xml")
        expected_output = [["A","B","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseMandatoryExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/mandatory-excludes/mandatory-excludes.xml")
        expected_output = []
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalOr(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/optional-or/optional-or.xml")
        expected_output = [["A","C"],["A","C","D"],["A","C","D","G"],["A","C","G"],
                            ["A","B","F","C","G"],["A","B","E","F","C","G"],["A","B","E","F","C"],
                            ["A","B","E","F","C","D"],["A","B","E","C","D"],["A","B","F","C","D"],
                            ["A","B","F","C","D","G"],["A","B","F","D"],["A","B","F","C"],
                            ["A","B","E","C"],["A","B","E","C","G"],["A","B","E","C","D","G"],
                            ["A","B","E","D"],["A","B","E","F","D"],["A","B","E","F","C","D","G"],
                            ["A","D"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOptionalAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/optional-alternative/optional-alternative.xml")
        expected_output = [["A","C"],["A","D"],["A","B","E","C"],["A","B","E","D"],
                            ["A","B","E","D","G"],["A","B","F","D","G"],["A","B","F","D"],
                            ["A","D","G"],["A","B","F","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrAlternative(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/or-alternative/or-alternative.xml")
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
        pysat_model = self.load_model("models/fama_test_suite/relationships/or-requires/or-requires.xml")
        expected_output = [["A","C"],["A","C","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseOrExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/or-excludes/or-excludes.xml")
        expected_output = [["A","C"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeRequires(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/alternative-requires/alternative-requires.xml")
        expected_output = [["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/alternative-excludes/alternative-excludes.xml")
        expected_output = [["A","C"],["A","B"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseRequiresExcludes(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/requires-excludes/requires-excludes.xml")
        expected_output = [["A"],["A","C"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAllRelationships(self):
        pysat_model = self.load_model("models/fama_test_suite/relationships/allrelationships/allrelationships.xml")
        expected_output = [["A","B","D"],["A","B","D","C","F"],["A","B","E","C","F"],
                            ["A","B","E","C","F","G"]]
        self.ProductsOperation(pysat_model, expected_output)

    def testCaseAlternativeOddChildren(self):
        pysat_model = self.load_model("models/fama_test_suite/refinement/alternative-oddChildren/alternative-oddChildren.xml")
        expected_output = []
        self.ProductsOperation(pysat_model, expected_output)


if __name__ == '__main__':
    unittest.main()
