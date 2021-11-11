import pytest

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader

from models.models_info import *


def get_model(model_name) -> str:
    return FeatureIDEReader(INPUT_MODELS_FOLDER + model_name + EXTENSION).transform()


@pytest.mark.parametrize("model_name, expected_nof_features", [[m[NAME], m[NOF_FEATURES]] for m in MODELS])
def test_nof_features(model_name, expected_nof_features):
    fm = get_model(model_name)
    assert len(fm.get_features()) == expected_nof_features

@pytest.mark.parametrize("model_name, expected_nof_constraints", [[m[NAME], m[NOF_CONSTRAINTS]] for m in MODELS])
def test_nof_constraints(model_name, expected_nof_constraints):
    fm = get_model(model_name)
    assert len(fm.get_constraints()) == expected_nof_constraints

@pytest.mark.parametrize("model_name, expected_root_feature", [[m[NAME], m[ROOT_NAME]] for m in MODELS])
def test_root_feature(model_name, expected_root_feature):
    fm = get_model(model_name)
    assert fm.root.name == expected_root_feature
    assert fm.root.get_parent() is None

@pytest.mark.parametrize("model_name, expected_nof_or_groups", [[m[NAME], m[NOF_ORS]] for m in MODELS])    
def test_nof_or_groups(model_name, expected_nof_or_groups):
    fm = get_model(model_name)
    result_or_groups = sum(map(lambda f: f.is_or_group(), fm.get_features()))
    assert result_or_groups == expected_nof_or_groups

@pytest.mark.parametrize("model_name, expected_nof_xor_groups", [[m[NAME], m[NOF_ALTERNATIVES]] for m in MODELS])
def test_nof_alternative_groups(model_name, expected_nof_xor_groups):
    fm = get_model(model_name)
    result_alternative_groups = sum(map(lambda f: f.is_alternative_group(), fm.get_features()))
    assert result_alternative_groups == expected_nof_xor_groups

@pytest.mark.parametrize("model_name, expected_nof_abstract_feats", [[m[NAME], m[NOF_ABSTRACT_FEATURES]] for m in MODELS])
def test_nof_abstract_features(model_name, expected_nof_abstract_feats):
    fm = get_model(model_name)
    result_abstract_features = sum(map(lambda f: f.is_abstract, fm.get_features()))
    assert result_abstract_features == expected_nof_abstract_feats

@pytest.mark.parametrize("fm_input, expected_nof_leaf_features", [[m[NAME], m[NOF_LEAF_FEATURES]] for m in MODELS])
def test_nof_leaf_features(fm_input, expected_nof_leaf_features):
    fm = get_model(fm_input)
    result_leaf_features = sum(map(lambda f: f.is_leaf(), fm.get_features()))
    assert result_leaf_features == expected_nof_leaf_features
