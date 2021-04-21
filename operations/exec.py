import python_sat.valid
import python_sat.products
import python_sat.core
import python_sat.dead

import os

def exec_models_in_dir(start,operation):
    print("Executing "+operation.__name__+" operation")
    for root, dirs, files in os.walk(start):
        for file in files:
            if file.endswith(".xml"):
                print("Executing "+os.path.join(root, file))
                try:
                    operation.exec(os.path.join(root, file))
                except:
                    print("Exception occurred")    


if __name__ == '__main__':
    exec_models_in_dir("./models/fama_test_suite",python_sat.dead)