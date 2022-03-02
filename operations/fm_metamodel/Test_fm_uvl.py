import pytest

from famapy.metamodels.fm_metamodel.transformations import UVLReader
from famapy.metamodels.fm_metamodel.operations import (
    FMCoreFeatures,
    FMCountLeafs,
    FMEstimatedProductsNumber
)

from models.models_info import *


def get_model(model_name) -> str:
    return UVLReader(INPUT_UVL_MODELS_FOLDER + model_name + UVL_EXTENSION).transform()


@pytest.mark.parametrize("model_name, expected_nof_core_features", [[m[NAME], m[NOF_CORE_FEATURES]] for m in MODELS])
def test_nof_core_features(model_name, expected_nof_core_features):
    fm = get_model(model_name)
    core_features = FMCoreFeatures().execute(fm).get_result()
    assert len(core_features) == expected_nof_core_features

@pytest.mark.parametrize("model_name, expected_nof_leaf_features", [[m[NAME], m[NOF_LEAF_FEATURES]] for m in MODELS])
def test_nof_leaf_features(model_name, expected_nof_leaf_features):
    fm = get_model(model_name)
    leaf_features = FMCountLeafs().execute(fm).get_result()
    assert leaf_features == expected_nof_leaf_features

@pytest.mark.parametrize("model_name, expected_nof_products", [[m[NAME], m[NOF_PRODUCTS]] for m in MODELS])
def test_nof_estimated_products(model_name, expected_nof_products):
    fm = get_model(model_name)
    nof_products = FMEstimatedProductsNumber().execute(fm).get_result()
    assert expected_nof_products is None or nof_products >= expected_nof_products
