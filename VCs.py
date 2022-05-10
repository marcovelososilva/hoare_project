# from pyparsing import empty
from Exprs import *
from Imp   import *
from Specs import *
from WPrec import *

class VC_Exception(Exception):
    pass

''' Ineficient version of the VC generation algorithm. This is the
    second block of code that you have to implement. '''

def VC(pre,c,post):
    # Like the case of the function [wprec], the way the code goes
    # is by first analysing what kind of command instruction we
    # are looking at, and then provide the corresponding code as
    # defined in the mathematical definition of the VC function
    match c:
        case Skip():
            # Enter your code here, and delete "pass"
            pass
        case Assgn():
            # Enter your code here, and delete "pass"
            pass
        case Seq():
            # Enter your code here, and delete "pass"
            pass
        case IfThen():
            # Enter your code here, and delete "pass"
            pass
        case While():
            # Enter your code here, and delete "pass"
            pass
        case _:
            raise VC_Exception


''' Improved version of the VC generation algorithm.
    This is the final block of code that you have to
    implement. The approach for doing it is the same
    as the one used in the previous two function [wprec]
    and [VC].'''

def VCG(pre,c,post):
    
    def VC_i(p,pst):
        match p:
            case Skip():
                return set()
            case Assgn():
                return set()
            case Seq():
                l = VC_i(p.left(),wprec(p.right(),pst))
                r = VC_i(p.right(),pst)
                return l.union(r)
            case IfThen():
                l = VC_i(p.left(),pst)
                r = VC_i(p.right(),pst)
                return l.union(r)
            case While():
                i = { SImp(SAnd(p.inv(),bexpr2spec(p.cond())),wprec(p.body(),p.inv())) }
                j = { SImp(SAnd(p.inv(),SNeg(bexpr2spec(p.cond()))),pst) }
                r = VC_i(p.body(),p.inv())
                return i.union(j.union(r))

    # For your convenience, we left implemented the call entry point of
    # the [VCG] function, which willl then call the function [VC_i] that
    # must be completed above.
    r = { SImp(pre,wprec(c,post)) }
    return r.union(VC_i(c,post))
