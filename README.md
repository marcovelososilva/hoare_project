# hoare_project
This repository contains the code base on which the groups of student should work for this assessment. 

## Objectives
For completing this assignment, the groups shall implement the code of:
- the [wprec] function that exists in the [WPrec.py] file;
- the [VC] function that exists in the [VCs.py] file.

## Requirements
For developing this assignment you should have installed:
- Python 3.10
- the colorama package (that you can install via the [pip] command)
- optionally, if you want to see your code being used to call the Z3 theorem prover showing that in fact the Hoare reasoning is correct, you need to install the Z3 theorem prover and the Python API for Z3. See the assignment pdf for instructions.


## Testing your code

For testing your code, your should rely on the Python scripts that start with "test_". There are three of such scripts:
- test_Specs.py : this one has the purpose of serving as an example on how to run tests in the code. This test script simply shows the well-formedness of specifications.
- test_WPrec.py : this test file has the purpose of testing the correct implementation of the [wprec] function that is present in the [WPrec.py] script.
- test_WPrec.py : this test file has the purpose of testing the correct implementation of the [VC] function that is present in the [VCs.py] script.

To run any of these test scripts you just need to invoque the Python interpreter on them, that is, "python test_xxx.py" where the "xxx" should be replaced by corresponding name that corresponds to the test you want to run.