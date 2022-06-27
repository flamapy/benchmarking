from famapy.metamodels.fm_metamodel.transformations.glencoe_reader import GlencoeReader

reader = GlencoeReader('Truck.gfm.json')
fm = reader.transform()
print(fm)