import pytest

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
    nof_products = Glucose3ProductsNumber().execute(model).get_result()
    print(f'#Products: {nof_products}')

@pytest.mark.parametrize("model_name, expected_nof_products", [[m[NAME], m[NOF_PRODUCTS]] for m in MODELS[:4]])
def test_nof_products(model_name, expected_nof_products):
    model = get_model(model_name)
    nof_products = Glucose3ProductsNumber().execute(model).get_result()
    assert nof_products == expected_nof_products

@pytest.mark.parametrize("model_name", [m[0] for m in MODELS])
def test_valid_model(model_name):
    model = get_model(model_name)
    valid = Glucose3Valid().execute(model).get_result()
    assert valid

@pytest.mark.parametrize("model_name, expected_nof_core_features", [[m[NAME], m[NOF_CORE_FEATURES]] for m in MODELS])
def test_nof_core_features(model_name, expected_nof_core_features):
    model = get_model(model_name)
    core_features = Glucose3CoreFeatures().execute(model).get_result()
    assert len(core_features) == expected_nof_core_features

@pytest.mark.parametrize("model_name, expected_nof_dead_features", [[m[NAME], m[NOF_DEAD_FEATURES]] for m in MODELS])
def test_nof_dead_features(model_name, expected_nof_dead_features):
    model = get_model(model_name)
    dead_features = Glucose3DeadFeatures().execute(model).get_result()
    assert len(dead_features) == expected_nof_dead_features
