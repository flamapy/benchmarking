import pytest

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader
from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat

from famapy.metamodels.pysat_metamodel.operations.glucose3_products_number import Glucose3ProductsNumber
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid import Glucose3Valid
from famapy.metamodels.pysat_metamodel.operations.glucose3_core_features import Glucose3CoreFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_dead_features import Glucose3DeadFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_false_optional_features import Glucose3FalseOptionalFeatures


# INDEX: ATTRIBUTE
# 0 filename
# 1 nof core features
# 2 nof dead features
# 3 nof false-optional features
# 4 nof leaf features
# 5 nof of products
MODELS = [('pizzas', 4, 0, 0, 8, 42),
          ('wget', 2, 0, 0, 15, 8192),
          ('GPL', 5, 0, 0, 13, 436),
          ('jHipster', 7, 0, 0, 32, 26256),
          ('tankwar', 7, 0, 0, 26, 1741824),
          ('mobilemedia2', 10, 0, 0, 31, 3096576),
          ('aafms_framework-namesAdapted', 3, 0, 0, 45, 132224790560),
          ('WeaFQAs', 1, 0, 0, 124, 1677039951397603738337280),
          ('busybox-1.18.0', 20, 15, 3, 683, 0),
          ('embtoolkit', 78, 42, 0, 966, 0),
          ('ea2468', 4, 124, 222, 1069, 0),
          ('uClinux-distribution', 6, 0, 0, 1368, 0),
          ('automotive2_1', 1394, 1, 2, 12615, 0),
          ('linux-2.6.33.3', 53, 211, 39, 5523, 0)]


INPUT_MODELS_FOLDER = 'models/featureide/'
EXTESION = '.xml'


def get_model(model_name):
    fm = FeatureIDEReader(INPUT_MODELS_FOLDER + model_name + EXTESION).transform()
    sat = FmToPysat(fm).transform()
    return sat

@pytest.mark.parametrize("model_name, expected_nof_products", [[m[0], m[5]] for m in MODELS[:4]])
def test_nof_products(model_name, expected_nof_products):
    model = get_model(model_name)
    nof_products = Glucose3ProductsNumber().execute(model).get_result()
    assert nof_products == expected_nof_products

@pytest.mark.parametrize("model_name", [m[0] for m in MODELS])
def test_valid_model(model_name):
    model = get_model(model_name)
    valid = Glucose3Valid().execute(model).get_result()
    assert valid

@pytest.mark.parametrize("model_name, expected_nof_core_features", [[m[0], m[1]] for m in MODELS])
def test_nof_core_features(model_name, expected_nof_core_features):
    model = get_model(model_name)
    core_features = Glucose3CoreFeatures().execute(model).get_result()
    assert len(core_features) == expected_nof_core_features

@pytest.mark.parametrize("model_name, expected_nof_dead_features", [[m[0], m[2]] for m in MODELS])
def test_nof_dead_features(model_name, expected_nof_dead_features):
    model = get_model(model_name)
    dead_features = Glucose3DeadFeatures().execute(model).get_result()
    assert len(dead_features) == expected_nof_dead_features

@pytest.mark.parametrize("model_name, expected_nof_false_optional_features", [[m[0], m[3]] for m in MODELS])
def test_nof_false_optional_features(model_name, expected_nof_false_optional_features):
    model = get_model(model_name)
    false_optional_features = Glucose3FalseOptionalFeatures().execute(model).get_result()
    assert len(false_optional_features) == expected_nof_false_optional_features