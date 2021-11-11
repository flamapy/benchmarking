import pytest

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader
from famapy.metamodels.bdd_metamodel.transformations.fm_to_bdd import FmToBDD
from famapy.metamodels.bdd_metamodel.operations import (
    BDDProductsNumber,
    BDDProductDistributionBF
)

from models.models_info import *


def get_model(model_name):
    fm = FeatureIDEReader(INPUT_MODELS_FOLDER + model_name + EXTENSION).transform()
    bdd = FmToBDD(fm).transform()
    return bdd

@pytest.mark.parametrize("model_name, expected_nof_products", [[m[NAME], m[NOF_PRODUCTS]] for m in MODELS[:8]])
def test_nof_products(model_name, expected_nof_products):
    model = get_model(model_name)
    nof_products = BDDProductsNumber().execute(model).get_result()
    assert nof_products == expected_nof_products

@pytest.mark.parametrize("model_name, expected_product_dist", [[m[NAME], m[PRODUCT_DISTRIBUTION]] for m in MODELS[:6]])
def test_product_distribution(model_name, expected_product_dist):
    model = get_model(model_name)
    product_dist = BDDProductDistributionBF().execute(model).get_result()
    assert product_dist == expected_product_dist
