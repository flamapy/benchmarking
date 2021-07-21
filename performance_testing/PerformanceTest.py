from Glucose3Performance import Glucose3Performance

'''
The method Glucose3Performance has one parameter, the type of the operation to be proven, following 
the next semantic:

-core features -> cf
-dead features -> df
-products -> p
-products number -> pn
-valid -> v
-valid product -> vp
-valid configuration -> vc
-error detection -> edetc
-error diagnosis -> ediag
-false optional features -> fof
'''

testing = Glucose3Performance("vm")
testing.run()
