import pytest

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader
from famapy.metamodels.bdd_metamodel.transformations.fm_to_bdd import FmToBDD
from famapy.metamodels.bdd_metamodel.operations import (
    BDDProductsNumber,
    BDDProductDistributionBF
)

# INDEX: ATTRIBUTE
# 0 filename
# 1 nof of products
# product distribution
MODELS = [('pizzas', 42, [0, 0, 0, 0, 0, 0, 0, 12, 18, 10, 2, 0, 0]),
          ('wget', 8192, [0, 0, 1, 11, 58, 198, 495, 957, 1452, 1716, 1551, 1045, 506, 166, 33, 3, 0, 0]),
          ('GPL', 436, [0, 0, 0, 0, 0, 0, 0, 1, 10, 27, 52, 73, 83, 78, 61, 36, 13, 2, 0]),
          ('tankwar', 1741824, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 216, 1176, 4008, 12072, 30792, 65856, 120840, 189792, 254880, 291888, 282456, 227088, 147864, 75288, 28608, 7584, 1248, 96, 0, 0, 0, 0, 0, 0, 0]),
          ('mobilemedia2', 3096576, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 684, 3012, 8736, 20376, 43380, 86736, 156864, 247872, 339732, 408252, 436416, 417852, 355992, 264852, 167604, 87468, 36300, 11436, 2556, 360, 24, 0, 0, 0, 0, 0, 0]),
          ('jHipster', 26256, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 16, 42, 106, 200, 238, 250, 488, 1276, 2688, 4314, 5460, 5322, 3696, 1668, 432, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
          ('aafms_framework-namesAdapted', 132224790560, []),
          ('WeaFQAs', 1677039951397603738337280, []),
          ('busybox-1.18.0', 0, []),
          ('embtoolkit', 0, []),
          ('ea2468', 0, []),
          ('uClinux-distribution', 0, []),
          ('automotive2_1', 0, []),
          ('linux-2.6.33.3', 0, [])]

INPUT_MODELS_FOLDER = 'models/featureide/'
EXTESION = '.xml'


def get_model(model_name):
    fm = FeatureIDEReader(INPUT_MODELS_FOLDER + model_name + EXTESION).transform()
    bdd = FmToBDD(fm).transform()
    return bdd

@pytest.mark.parametrize("model_name, expected_nof_products", [[m[0], m[1]] for m in MODELS[:8]])
def test_nof_products(model_name, expected_nof_products):
    model = get_model(model_name)
    nof_products = BDDProductsNumber().execute(model).get_result()
    assert nof_products == expected_nof_products

@pytest.mark.parametrize("model_name, expected_product_dist", [[m[0], m[2]] for m in MODELS[:6]])
def test_product_distribution(model_name, expected_product_dist):
    model = get_model(model_name)
    product_dist = BDDProductDistributionBF().execute(model).get_result()
    assert product_dist == expected_product_dist
