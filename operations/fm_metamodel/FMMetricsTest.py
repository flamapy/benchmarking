import pytest

from famapy.metamodels.fm_metamodel.transformations.featureide_reader import FeatureIDEReader


# INDEX: ATTRIBUTE
# 0 filename
# 1 nof features 
# 2 nof constraints
# 3 root name
# 4 nof ors
# 5 nof alternatives
# 6 nof abstract features
# 7 nof leaf features
MODELS = [('pizzas', 12, 1, 'Pizza', 1, 2, 1, 8),
          ('wget', 17, 0, 'wget', 0, 1, 0, 15),
          ('tankwar', 37, 0, 'TankWar', 2, 6, 0, 26),
          ('mobilemedia2', 43, 3, 'MobileMedia2', 4, 3, 0, 31),
          ('jHipster', 45, 13, 'JHipster', 0, 10, 13, 32),
          ('WeaFQAs', 179, 7, 'FQAs', 13, 23, 0, 124),
          ('busybox-1.18.0', 854, 67, 'root', 0, 8, 0, 683),
          ('embtoolkit', 1179, 167, 'root', 0, 70, 0, 966),
          ('ea2468', 1408, 1281, 'root', 0, 12, 0, 1069),
          ('uClinux-distribution', 1580, 247, 'root', 0, 10, 0, 1368),
          ('automotive2_1', 14010, 624, 'N_379925076__F_91527E35945B', 106, 1010, 0, 12615),
          ('linux-2.6.33.3', 6467, 7650, 'root', 2, 39, 0, 5523)]

INPUT_MODELS_FOLDER = 'models/featureide/'
EXTESION = '.xml'


def get_model(model_name) -> str:
    return FeatureIDEReader(INPUT_MODELS_FOLDER + model_name + EXTESION).transform()


@pytest.mark.parametrize("model_name, expected_nof_features", [m[:2] for m in MODELS])
def test_nof_features(model_name, expected_nof_features):
    fm = get_model(model_name)
    assert len(fm.get_features()) == expected_nof_features

@pytest.mark.parametrize("model_name, expected_nof_constraints", [[m[0], m[2]] for m in MODELS])
def test_nof_constraints(model_name, expected_nof_constraints):
    fm = get_model(model_name)
    assert len(fm.get_constraints()) == expected_nof_constraints

@pytest.mark.parametrize("model_name, expected_root_feature", [[m[0], m[3]] for m in MODELS])
def test_root_feature(model_name, expected_root_feature):
    fm = get_model(model_name)
    assert fm.root.name == expected_root_feature
    assert fm.root.get_parent() is None

@pytest.mark.parametrize("model_name, expected_nof_or_groups", [[m[0], m[4]] for m in MODELS])    
def test_nof_or_groups(model_name, expected_nof_or_groups):
    fm = get_model(model_name)
    result_or_groups = sum(map(lambda f: f.is_or_group(), fm.get_features()))
    assert result_or_groups == expected_nof_or_groups

@pytest.mark.parametrize("model_name, expected_nof_xor_groups", [[m[0], m[5]] for m in MODELS])
def test_nof_alternative_groups(model_name, expected_nof_xor_groups):
    fm = get_model(model_name)
    result_alternative_groups = sum(map(lambda f: f.is_alternative_group(), fm.get_features()))
    assert result_alternative_groups == expected_nof_xor_groups

@pytest.mark.parametrize("model_name, expected_nof_abstract_feats", [[m[0], m[6]] for m in MODELS])
def test_nof_abstract_features(model_name, expected_nof_abstract_feats):
    fm = get_model(model_name)
    result_abstract_features = sum(map(lambda f: f.is_abstract, fm.get_features()))
    assert result_abstract_features == expected_nof_abstract_feats

@pytest.mark.parametrize("fm_input, expected_nof_leaf_features", [[m[0], m[7]] for m in MODELS])
def test_nof_leaf_features(fm_input, expected_nof_leaf_features):
    fm = get_model(fm_input)
    result_leaf_features = sum(map(lambda f: f.is_leaf(), fm.get_features()))
    assert result_leaf_features == expected_nof_leaf_features
