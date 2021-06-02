from metamorphic_testing.Glucose3Metamorphic import Glucose3Metamorphic

from famapy.metamodels.fm_metamodel.transformations.xml_transformation import XMLTransformation

parser = XMLTransformation("models/simple/example.xml")
fm = parser.transform()

'''
The method Glucose3Metamorphic has 4 parameters, the initial feature model, the inital products of
these feature model, the number of iterations or metamorphic relations that will be generated and
the type of the operation to be proven, following the next semantic:

- core features -> cf
- dead features -> df
- products -> p
- products number -> pn
- valid -> v
- false optional features -> fof
'''

testing = Glucose3Metamorphic(fm, [["A","C"],["A","B","C"]], 20, "v")
testing.run()
