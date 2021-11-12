import pytest

from famapy.metamodels.fm_metamodel.models import FeatureModel
from famapy.metamodels.fm_metamodel.transformations.xml_reader import XMLReader

from famapy.metamodels.pysat_metamodel.models.pysat_model import PySATModel
from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.operations.glucose3_error_detection import Glucose3ErrorDetection
from famapy.metamodels.pysat_metamodel.operations.glucose3_core_features import Glucose3CoreFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_dead_features import Glucose3DeadFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_false_optional_features import Glucose3FalseOptionalFeatures


FAMA_EXTENSION = '.xml'
BASE_INPUT_MODELS_PATH = 'models/fama_test_suite/'


def get_model(filepath: str) -> tuple[FeatureModel, PySATModel]:
    fm = XMLReader(filepath + FAMA_EXTENSION).transform()
    pysat_model = FmToPysat(fm).transform()
    return (fm, pysat_model)


CF_MODELS = {'case1/cf-case1': ['A', 'B'],
             'case2/cf-case2': ['A', 'B'],           
             'case3/cf-case3': ['A', 'B', 'C'],
             'case4/cf-case4': ['A', 'B', 'C', 'E'],
             'case5/cf-case5': ['A', 'B', 'C', 'D'],
             'case6/cf-case6': []}
@pytest.mark.parametrize("model_name, expected_cf", [[m, f] for m, f in CF_MODELS.items()])
def test_core_features(model_name, expected_cf):
    models_path = BASE_INPUT_MODELS_PATH + 'error-guessing/core-features/'
    _, pysat_model = get_model(models_path + model_name)
    core_features = Glucose3CoreFeatures().execute(pysat_model).get_result()
    assert set(core_features) == set(expected_cf)


DF_MODELS = {'case1/df-case1': ['D'],
             'case2/df-case2': ['E'],           
             'case3/df-case3': ['D'],
             'case4/df-case4': ['C'],
             'case5/df-case5': ['A', 'B', 'C'],
             'case6/df-case6': ['B'],
             'case7/df-case7': ['A', 'B', 'C'],
             'case8/df-case8': ['B'],}
@pytest.mark.parametrize("model_name, expected_df", [[m, f] for m, f in DF_MODELS.items()])
def test_dead_features(model_name, expected_df):
    models_path = BASE_INPUT_MODELS_PATH + 'error-guessing/dead-features/'
    _, pysat_model = get_model(models_path + model_name)
    dead_features = Glucose3DeadFeatures().execute(pysat_model).get_result()
    assert set(dead_features) == set(expected_df)


FOF_MODELS = {'case1/fof-case1': ['C'],
              'case2/fof-case2': ['C', 'D'],           
              'case3/fof-case3': ['C', 'D'],
              'case4/fof-case4': ['C'],
              'case5/fof-case5': ['C'],
              'case6/fof-case6': ['B', 'E']}
@pytest.mark.parametrize("model_name, expected_fof", [[m, f] for m, f in FOF_MODELS.items()])
def test_false_optional_features(model_name, expected_fof):
    models_path = BASE_INPUT_MODELS_PATH + 'error-guessing/false-optional-features/'
    fm, pysat_model = get_model(models_path + model_name)
    optional_features = [f.name for f in fm.get_features() if not f.is_mandatory()]
    false_optional_features = Glucose3FalseOptionalFeatures(optional_features).execute(pysat_model).get_result()
    assert set(false_optional_features) == set(expected_fof)


R_MODELS = {'case1/r-case1': ["Dead features: ['D']",
                              "False optional features: ['E']"],
            'case2/r-case2': ["Dead features: ['E']",
                              "False optional features: ['D']"]}
@pytest.mark.parametrize("model_name, expected_redundancies", [[m, f] for m, f in R_MODELS.items()])
def test_error_detection(model_name, expected_redundancies):
    models_path = BASE_INPUT_MODELS_PATH + 'error-guessing/redundancies/'
    _, pysat_model = get_model(models_path + model_name)
    redundancies = Glucose3ErrorDetection().execute(pysat_model).get_result()
    assert set(redundancies) == set(expected_redundancies)