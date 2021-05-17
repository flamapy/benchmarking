from pysat.solvers import Glucose3

from famapy.core.models import Configuration

from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

from famapy.metamodels.pysat_metamodel.transformations.fm_to_pysat import FmToPysat
from famapy.metamodels.pysat_metamodel.operations.glucose3_false_optional_features import Glucose3FalseOptionalFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_core_features import Glucose3CoreFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_dead_features import Glucose3DeadFeatures
from famapy.metamodels.pysat_metamodel.operations.glucose3_products import Glucose3Products
from famapy.metamodels.pysat_metamodel.operations.glucose3_products_number import Glucose3ProductsNumber
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid import Glucose3Valid
from famapy.metamodels.pysat_metamodel.operations.glucose3_error_diagnosis import Glucose3ErrorDiagnosis
from famapy.metamodels.pysat_metamodel.operations.glucose3_error_detection import Glucose3ErrorDetection
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid_configuration import Glucose3ValidConfiguration
from famapy.metamodels.pysat_metamodel.operations.glucose3_valid_product import Glucose3ValidProduct
from famapy.metamodels.pysat_metamodel.operations.glucose3_filter import Glucose3Filter

import time
import csv

class Glucose3Performance():

    def __init__(self, operation_type):
        self.operation_type = operation_type
        self.features = [10,20,30,40,50,60,70,80,90,100,200,500,800,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,15000,20000]
        self.percent_cons = [1,10,15,30,50]

    def run(self):
        if self.operation_type == "cf":
            self.OperationDataGenerator(Glucose3CoreFeatures())
        elif self.operation_type == "df":
            self.OperationDataGenerator(Glucose3DeadFeatures())
        elif self.operation_type == "fof":
            self.OperationDataGenerator(Glucose3FalseOptionalFeatures())
        elif self.operation_type == "p":
            self.OperationDataGenerator(Glucose3Products())
        elif self.operation_type == "pn":
            self.OperationDataGenerator(Glucose3ProductsNumber())
        elif self.operation_type == "vm":
            self.OperationDataGenerator(Glucose3Valid())
        elif self.operation_type == "edetc":
            self.OperationDataGenerator(Glucose3ErrorDetection())
        elif self.operation_type == "ediag":
            self.OperationDataGenerator(Glucose3ErrorDiagnosis())
        elif self.operation_type == "vc":
            self.OperationDataGenerator(Glucose3ValidConfiguration())
        elif self.operation_type == "vp":
            self.OperationDataGenerator(Glucose3ValidProduct())
        elif self.operation_type == "f":
            self.OperationDataGenerator(Glucose3Filter())
        else:
            raise Exception("The operation type is not defined")

    def OperationDataGenerator(self, operation):
        myFile = open('performance_testing/performance_datasets/' + self.operation_type + '_data_performance.csv', 'w')
        writer = csv.writer(myFile)
        writer.writerows([["Features","Seconds","Percent_cons"]])
        for cons in self.percent_cons:
            for feat in self.features:
                path = "models/synthetic/simple_betty_gen_models/" + str(feat) + "/" + str(cons) + "-9.xml"
                parser = XMLTransformation(path)
                fm = parser.transform()

                if self.operation_type in ("vc","f"):
                    configuration = self.get_config(fm)
                    operation.set_configuration(configuration)

                transform = FmToPysat(fm)
                transform.transform()

                if self.operation_type == "vp":
                    product = self.get_product(fm, transform)
                    operation.set_configuration(product)

                t0 = time.time()
                operation.execute(transform.destination_model)
                t1 = time.time() - t0

                writer.writerows([[feat,t1,cons]])

        print("Generated data!\nNow you can see it with Seaborn Visualizer file")

    def get_config(self, model):
        model_features = model.get_features()
        feat1 = model_features[0]
        feat2 = model_features[1]
        feat3 = model_features[2]
        feat4 = model_features[3]
        feat5 = model_features[4]
        feat6 = model_features[5]
        feat7 = model_features[6]
        feat8 = model_features[7]
        feat9 = model_features[8]

        configuration = Configuration({feat1:True,feat2:True,feat3:True,feat4:True,
            feat5:False,feat6:False,feat7:False,feat8:False,feat9:False})

        return configuration

    def get_product(self, model, transform):
        g = Glucose3()
        for clause in transform.destination_model.r_cnf:
            g.add_clause(clause)
        for clause in transform.destination_model.ctc_cnf:
            g.add_clause(clause)   
      
        product = dict()
        for solution in g.enum_models():
            model_features = model.get_features()
            for variable in solution:
                if variable > 0:
                    name = transform.destination_model.features.get(variable)
                    for feature in model_features:
                        if feature.name == name:
                            product[feature]=True
                else:
                    name = transform.destination_model.features.get(variable)
                    for feature in model_features:
                        if feature.name == name:
                            product[feature]=False

            break
            
        configuration = Configuration(product)

        return configuration

