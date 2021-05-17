This is the performance testing resutls builts for the operations in FaMaPY, a tool develop in Python 3 to the automated analisys of 
features models. The intention was check the performance of the of the operations implemented in Glucose3 PySat solver.

With a 6 cores / 12 threads processor the results of the performance testing are in the folder PerformanceDatasets, you can visualize them
with the SeabornVisualizer file changing the path to the diferents datasets. You must have installed Seaborn and his dependencies.

If you want to run the performance testing in your computer, you need to have installed FaMaPy and his metamodels modules, 
and all the dependencies needed. Then, you can generate the datasets files running the file PerformanceTest.py with the type of operation
that you want to perfom as a parameter, following the next semantic:

- core features -> cf
- dead features -> df
- products -> p
- products number -> pn
- valid -> v
- valid product -> vp
- valid configuration -> vc
- error detection -> edetc
- error diagnosis -> ediag
- false optional features -> fof

