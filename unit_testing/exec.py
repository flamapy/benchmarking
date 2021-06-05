from tests.ValidModelTest import ValidModelTest
from tests.ProductsTest import ProductsTest
from tests.ProductsNumberTest import ProductsNumberTest
from tests.ValidConfigurationTest import ValidConfigurationTest
from tests.ValidProductTest import ValidProductTest
from tests.DeadFeaturesTest import DeadFeaturesTest
from tests.CoreFeaturesTest import CoreFeaturesTest
from tests.FalseOptionalFeaturesTest import FalseOptionalFeaturesTest
from tests.ErrorDetectionTest import ErrorDetectionTest
from tests.ErrorDiagnosisTest import ErrorDiagnosisTest
from tests.FilterTest import FilterTest

print("----------Valid Model Tests----------\n")
valid_model_test = ValidModelTest()
valid_model_test.run()

print("\n ********************** \n")

print("----------Products Tests----------\n")
products_test = ProductsTest()
products_test.run()

print("\n ********************** \n")

print("----------Products Number Tests----------\n")
products_test = ProductsNumberTest()
products_test.run()

print("\n ********************** \n")

print("----------Valid Configuration Tests----------\n")
valid_configuration_test = ValidConfigurationTest()
valid_configuration_test.run()

print("\n ********************** \n")

print("----------Valid Product Tests----------\n")
valid_product_test = ValidProductTest()
valid_product_test.run()

print("\n************************\n")

print("----------Dead Features Tests----------\n")
dead_feature_test = DeadFeaturesTest()
dead_feature_test.run()

print("\n************************\n")

print("----------Core Features Tests----------\n")
core_feature_test = CoreFeaturesTest()
core_feature_test.run()

print("\n************************\n")

print("----------False Optional Features Tests----------\n")
false_optional_feature_test = FalseOptionalFeaturesTest()
false_optional_feature_test.run()

print("\n************************\n")

print("----------Error Detection Tests----------\n")
error_detection_test = ErrorDetectionTest()
error_detection_test.run()

print("\n************************\n")

print("----------Error Diagnosis Tests----------\n")
error_diagnosis_test = ErrorDiagnosisTest()
error_diagnosis_test.run()

print("\n************************\n")

print("----------Filter Tests----------\n")
error_diagnosis_test = FilterTest()
error_diagnosis_test.run()

print("\n************************\n")
