import pytest

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader
from famapy.metamodels.fm_metamodel.operations import (
    FMCoreFeatures,
    FMCountLeafs,
    FMEstimatedProductsNumber
)

# INDEX: ATTRIBUTE
# 0 filename
# 1 nof core features
# 2 nof dead features
# 3 nof false-optional features
# 4 nof leaf features
# 5 nof of products
MODELS = [('pizzas', 4, 0, 0, 8, 42),
          ('wget', 2, 0, 0, 15, 8192),
          ('tankwar', 7, 0, 0, 26, 1741824),
          ('mobilemedia2', 10, 0, 0, 31, 3096576),
          ('jHipster', 7, 0, 0, 32, 26256),
          ('WeaFQAs', 1, 0, 0, 124, 1677039951397603738337280),
          ('busybox-1.18.0', 20, 15, 3, 683, 0),
          ('embtoolkit', 78, 42, 0, 966, 0),
          ('ea2468', 4, 124, 222, 1069, 0),
          ('uClinux-distribution', 6, 0, 0, 1368, 0),
          ('automotive2_1', 1394, 1, 2, 12615, 0),
          ('linux-2.6.33.3', 53, 211, 39, 5523, 0)]

INPUT_MODELS_FOLDER = 'models/featureide/'
EXTESION = '.xml'


def get_model(model_name) -> str:
    return FeatureIDEReader(INPUT_MODELS_FOLDER + model_name + EXTESION).transform()


@pytest.mark.parametrize("model_name, expected_nof_core_features", [m[:2] for m in MODELS])
def test_nof_core_features(model_name, expected_nof_core_features):
    fm = get_model(model_name)
    core_features = FMCoreFeatures().execute(fm).get_result()
    assert len(core_features) == expected_nof_core_features

@pytest.mark.parametrize("model_name, expected_nof_leaf_features", [[m[0], m[4]] for m in MODELS])
def test_nof_leaf_features(model_name, expected_nof_leaf_features):
    fm = get_model(model_name)
    leaf_features = FMCountLeafs().execute(fm).get_result()
    assert leaf_features == expected_nof_leaf_features

@pytest.mark.parametrize("model_name, expected_nof_products", [[m[0], m[5]] for m in MODELS])
def test_nof_products(model_name, expected_nof_products):
    fm = get_model(model_name)
    nof_products = FMEstimatedProductsNumber().execute(fm).get_result()
    assert nof_products == expected_nof_products
