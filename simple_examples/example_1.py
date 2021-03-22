from famapy.core.discover import DiscoverMetamodels


# create the manager
dm = DiscoverMetamodels()

# Example t2m
fm = dm.use_transformation_t2m(src='example.xml', dst='fm')

# Example m2t
dm.use_transformation_m2t(src=fm, dst='output.json')

# Example of using a m2m transformation
pysatm = dm.use_transformation_m2m(src=fm, dst='pysat')

# operation execute return the object instance
operation = dm.use_operation(src=pysatm, operation='Valid')
print("Result operation valid:", operation.is_valid())
