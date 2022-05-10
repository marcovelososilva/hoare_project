from Exprs import *
from Imp   import *
from Specs import *

class WPRec_Exception(Exception):
    pass

''' The first function that you need to implement. It
    refers to the function that implements the
    weakest precondition generation, given a code block
    [c] and a specification [q] (that serves the role of
    post condition.'''

def wprec(c,q):

    # First, we analyse what type of program instruction
    # we have, and then write the corresponding code.
    match c:
        case Skip():
            # Fill the code here
        case Assgn():
            # Fill the code here
        case Seq():
            # Fill the code here
        case IfThen():
            # Fill the code here
        case While():
            # Fill the code here
        case _:
            # This is the case that will not be reached, but is here
            # for completeness.
            raise WPRec_Exception




