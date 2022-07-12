from famapy.metamodels.fm_metamodel.transformations import GlencoeWriter
from famapy.metamodels.fm_metamodel.transformations import FeatureIDEReader
from models.models_info import *

for m in MODELS: 
    fm = FeatureIDEReader(INPUT_FIDE_MODELS_FOLDER + m[NAME] + FIDE_EXTENSION).transform()
    writer = GlencoeWriter(INPUT_GLENCOE_MODELS_FOLDER + m[NAME] + GLENCOE_EXTENSION, fm).transform()
    