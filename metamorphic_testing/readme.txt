This is the metamorphic testing resutls builts for the operations in FaMaPY, a tool develop in Python 3 to the automated analisys of 
features models. The intention was check the performance of the of the operations implemented in Glucose3 PySat solver.

If you want to run the performance testing in your computer, you need to have installed FaMaPy and his metamodels modules, 
and all the dependencies needed.Then you can run the file MetamorphicTest that have the method Glucose3Metamorphic has 4 parameters, 
the initial feature model, the inital products of these feature model, the number of iterations or metamorphic relations that will be 
generated and the type of the operation to be proven, following the next semantic:

- core features -> cf
- dead features -> df
- products -> p
- products number -> pn
- valid -> v
- false optional features -> fof

