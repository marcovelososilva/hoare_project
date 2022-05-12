from operator import neg
from Exprs import *
from Imp import *
from Specs import *


class WPRec_Exception(Exception):
    pass


''' The first function that you need to implement. It
    refers to the function that implements the
    weakest precondition generation, given a code block
    [c] and a specification [q] (that serves the role of
    post condition.'''


def wprec(c, q):

    # First, we analyse what type of program instruction
    # we have, and then write the corresponding code.
    match c:
        # wprec(skip, Q) = Q
        case Skip():
            return q
        # wprec(x:=E,Q) = Q[x->E]
        case Assgn():
            return spec_subst(q, c.name(), c.value())
        # wprex(C1;C2,Q) = wprec(C1,wprec(C2,Q)) C1=c.right(); C2=c.left()
        case Seq():
            Q = wprec(c.right(), q)
            return wprec(c.left(), Q)
        # wprec(if B then C1 else C2,Q) = (B -> wprec(C1,Q))&&(not B -> wprec(C2, Q)) B=b; C1=ct; C2=cf;
        case IfThen():
            oneQ = wprec(c.left(), q)
            one = SImp(bexpr2spec(c.cond()), oneQ)
            twoQ = wprec(c.right(), q)
            notB = BENeg(c.cond())
            two = SImp(bexpr2spec(notB), twoQ)
            return SAnd(one, two)
        # wprec(while B do {A} C, Q) = I
        case While():
            return c.inv()
        case _:
            # This is the case that will not be reached, but is here
            # for completeness.
            raise WPRec_Exception
