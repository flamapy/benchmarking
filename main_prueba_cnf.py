from famapy.metamodels.pysat_metamodel.transformations.cnf_to_pysat import CNFReader

from famapy.metamodels.pysat_metamodel.operations.glucose3_products_number import Glucose3ProductsNumber
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid import Glucose3Valid
from famapy.metamodels.pysat_metamodel.operations.glucose3_core_features import Glucose3CoreFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_dead_features import Glucose3DeadFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_false_optional_features import Glucose3FalseOptionalFeatures

from models.models_info import *


def get_model(model_name):
    pysat_model = CNFReader(INPUT_TXTCNF_MODELS_FOLDER + model_name + TXTCNF_EXTENSION).transform()
    return pysat_model

if __name__ == '__main__':
    model = get_model('pizzas')
    print(model)
    for i, c in enumerate(model.get_all_clauses()):
        print(f'Clause {i}: {c}')
    nof_products = Glucose3ProductsNumber().execute(model).get_result()
    print(f'#Products: {nof_products}')