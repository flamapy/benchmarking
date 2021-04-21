import sys

from famapy.core.discover import DiscoverMetamodels


def exec(model):
    # Create the manager
    dm = DiscoverMetamodels()
    # Read the model
    fm = dm.use_transformation_t2m(src=model, dst='fm')
    # Print the model
    #print(fm)
    # Transform to Python-sat metamodel
    pysatm = dm.use_transformation_m2m(src=fm, dst='pysat')
    # Operation execute return the object instance
    operation = dm.use_operation(src=pysatm, operation='DeadFeatures')
    # Print the result
    print("Result:", str(operation.get_result()))


if __name__ == '__main__':
    exec(sys.argv[1])