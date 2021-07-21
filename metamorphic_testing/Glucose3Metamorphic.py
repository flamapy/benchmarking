import copy
import random
from typing import Any

from famapy.core.models.ast import AST

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.operations.glucose3_products import Glucose3Products
from famapy.metamodels.pysat_metamodel.operations.glucose3_products_number import Glucose3ProductsNumber
from famapy.metamodels.pysat_metamodel.operations.glucose3_core_features import Glucose3CoreFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_dead_features import Glucose3DeadFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_false_optional_features import Glucose3FalseOptionalFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid import Glucose3Valid

from famapy.metamodels.fm_metamodel.models.feature_model import Feature, FeatureModel, Relation, Constraint


class Glucose3Metamorphic():

    def __init__(self, fm, products, iterations, operation_type):
        self.fm = fm
        self.products = products
        self.iterations = iterations
        self.operation_type = operation_type
        self.iteration_counter = 0
        self.feature_counter = 0
        self.ctc_counter = [0,0]

    def run(self):
        dict = self.genetare_data_test_cases()

        for test_case in dict.items():
            operation_results, case_results = self.get_results(test_case[0], test_case[1])

            check = True
            if self.operation_type == "p" or self.operation_type == "cf" or  self.operation_type == "df":
                for result in case_results:
                    check = check and result in operation_results
            else:
                check = operation_results == case_results

            if check:
                print("Everything has gone as expected for test case")
            else:
                print("There are some error!")
                print("The operation resutls: ")
                print(operation_results)
                print("Doesn't match with the expected data case: ")
                print(case_results)

    def get_results(self, fm_model, case_results) -> tuple[Any,Any]:
        transform = FmToPysat(fm_model)
        transform.transform()
        pysat_model = transform.destination_model

        if self.operation_type == "p":
            operation = Glucose3Products()
        elif self.operation_type == "pn":
            operation = Glucose3ProductsNumber()
            case_results = len(case_results)
        elif self.operation_type == "cf":
            operation = Glucose3CoreFeatures()
            if case_results:
                cores = list(pysat_model.features.values())
            else:
                cores = []
            for product in case_results:
                cores = [feature for feature in product if feature in cores]
            case_results = cores
        elif self.operation_type == "df":
            operation = Glucose3DeadFeatures()
            deads = list(pysat_model.features.values())
            for product in case_results:
                deads = [feature for feature in deads if feature not in product]
            case_results = deads
        elif self.operation_type == "v":
            operation = Glucose3Valid()
            if case_results:
                case_results = True
            else:
                case_results = False
        elif self.operation_type == "fof":
            operation = Glucose3FalseOptionalFeatures()
            falses = []
            if case_results:
                cores = list(pysat_model.features.values())
            else:
                cores = []
            for product in case_results:
                cores = [feature for feature in product if feature in cores]
            for relation in fm_model.relations:
                names = [feat.name for feat in relation.children]
                for core in cores:
                    relation_check = relation.is_optional() or relation.is_or() or relation.is_alternative()
                    if core in names and relation_check:
                        falses.append(core)

            case_results = falses
        else:
            raise Exception("The operation type is not defined")

        operation.execute(pysat_model)
        operation_results = operation.get_result()

        return operation_results,case_results

    def genetare_data_test_cases(self) -> dict[FeatureModel, list[list[str]]]:
        result = {}

        while True:
            features = self.fm.get_features()
            num = len(features)
            new_feature1 = Feature("F" + str(self.feature_counter), [])
            self.feature_counter += 1
            new_feature2 = Feature("F" + str(self.feature_counter), [])

            f_number1 = random.randrange(num)
            f_number2 = random.randrange(num)
            while f_number1 == f_number2:
                f_number2 = random.randrange(num)

            number = random.randrange(1,7)
            if number == 1:
                self.add_mandatory(new_feature1)
            elif number == 2:
                self.add_optional(new_feature1)
            elif number == 3:
                self.add_alternative(new_feature1, new_feature2)
            elif number == 4:
                self.add_or(new_feature1, new_feature2)
            elif number == 5:
                self.add_requires(features[f_number1], features[f_number2])
            else:
                self.add_excludes(features[f_number1], features[f_number2])

            result[copy.deepcopy(self.fm)] = copy.deepcopy(self.products)

            if self.iteration_counter == self.iterations:
                print("The number of desired features has been marked!")
                break
            self.iteration_counter += 1

        return result

    def add_mandatory(self, new_feature) -> None:
        number = random.randrange(len(self.fm.get_features()))
        random_feature = self.fm.get_features()[number]
        self.fm.features.append(new_feature)
        r = Relation(parent=random_feature, children=[new_feature], card_min=1, card_max=1)
        random_feature.relations.append(r)

        for product in self.products:
            if random_feature.name in product:
                product.append(new_feature.name)

    def add_optional(self, new_feature) -> None:
        number = random.randrange(len(self.fm.get_features()))
        random_feature = self.fm.get_features()[number]
        self.fm.features.append(new_feature)
        r = Relation(parent=random_feature, children=[new_feature], card_min=0, card_max=1)
        random_feature.relations.append(r)

        new_products = []
        for product in self.products:
            new_products.append(product)
            if random_feature.name in product:
                new_product = [feat for feat in product]
                new_product.append(new_feature.name)
                new_products.append(new_product)

        self.products = new_products

    def add_alternative(self, new_feature1, new_feature2) -> None:
        self.feature_counter += 1
        number = random.randrange(len(self.fm.get_features()))
        random_feature = self.fm.get_features()[number]
        self.fm.features.append(new_feature1)
        self.fm.features.append(new_feature2)
        r = Relation(parent=random_feature, children=[new_feature1, new_feature2], card_min=1, card_max=1)
        random_feature.relations.append(r)

        new_products = []
        for product in self.products:
            if random_feature.name not in product:
                new_products.append(product)
            else:
                base = [feat for feat in product]
                new_product1 = copy.copy(base)
                new_product2 = copy.copy(base)
                new_product1.append(new_feature1.name)
                new_product2.append(new_feature2.name)
                new_products.append(new_product1)
                new_products.append(new_product2)

        self.products = new_products

    def add_or(self, new_feature1, new_feature2) -> None:
        self.feature_counter += 1
        number = random.randrange(len(self.fm.get_features()))
        random_feature = self.fm.get_features()[number]
        self.fm.features.append(new_feature1)
        self.fm.features.append(new_feature2)
        r = Relation(parent=random_feature, children=[new_feature1, new_feature2], card_min=1, card_max=2)
        random_feature.relations.append(r)

        new_products = []
        for product in self.products:
            if random_feature.name not in product:
                new_products.append(product)
            else:
                base = [feat for feat in product]
                new_product1 = copy.copy(base)
                new_product2 = copy.copy(base)
                new_product3 = copy.copy(base)
                new_product1.append(new_feature1.name)
                new_product2.append(new_feature2.name)
                new_product3.append(new_feature1.name)
                new_product3.append(new_feature2.name)
                new_products.append(new_product1)
                new_products.append(new_product2)
                new_products.append(new_product3)

        self.products = new_products

    def add_requires(self, feature1, feature2) -> None:
        ctc = Constraint("MRe-" + str(self.ctc_counter[0]), AST(feature1.name + " requires " + feature2.name))
        self.fm.ctcs.append(ctc)
        self.ctc_counter[0] += 1

        cores = [feature.name for feature in self.fm.get_features()]
        for product in self.products:
            cores = [feature for feature in product if feature in cores]

        updated_products = [product for product in self.products]
        for product in self.products:
            if feature2.name in cores:
                break
            if feature1.name in product and feature2.name not in product:
                updated_products.remove(product)

        self.products = updated_products

    def add_excludes(self, feature1, feature2) -> None:
        ctc = Constraint("MEx-" + str(self.ctc_counter[1]), AST(feature1.name + " excludes " + feature2.name))
        self.ctc_counter[1] += 1
        self.fm.ctcs.append(ctc)

        updated_products = [product for product in self.products]
        for product in self.products:
            if feature1.name in product and feature2.name in product:
                updated_products.remove(product)

        self.products = updated_products

