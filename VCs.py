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
        # VC({P} skip {Q}) = {P -> Q} - OK
        case Skip():
            return {SImp(pre, post)}
        # VC({P} x:=e {Q}) = {P -> Q [x->E]} - OK
        case Assgn():
            return {SImp(pre, spec_subst(post, c.name(), c.value()))}
        # VC({P} C1;C2 {Q}) = VC({P} C1 {wprec(C2,Q)}) U VC({wprec(C2,Q)} C2 {Q}) - OK
        case Seq():
            # wprec (esq e dir) = wprec(C2,Q)
            edwprec = wprec(c.right(), post)
            # esq = parte esquerda = VC({P} C1 {wprec(C2,Q)})
            esq = VC(pre, c.left(), edwprec)
            # dir = parte direita = VC({wprec(C2,Q)} C2 {Q})
            dir = VC(edwprec, c.right(), post)
            #esq UNIAO dir
            return esq.union(dir)
        # VC({P} if B then C1 else C2 {Q}) = VC({P & B} C1 {Q}) U VC({P & notB} C2 {Q})
        case IfThen():
            #P e B = {P & B}
            p_and_b = SAnd(pre, bexpr2spec(c.cond()))
            #esq VC({P & B} C1 {Q})
            esq = VC(p_and_b, c.left(), post)
            #P e NotB = {P & notB}
            NOT_b = bexpr2spec(BENeg(c.cond()))
            p_and_NotB = SAnd(pre, NOT_b)
            #dir = VC({P & notB} C2 {Q})
            dir = VC(p_and_NotB, c.right(), post)
            result = esq.union(dir)
            return result
        # VC({P} while B do {I} C {Q}) = {P -> I, I & notB -> Q} U VC({P & notB} C {Q})
        case While():
            #NOT_b = notB
            NOT_b = bexpr2spec(BENeg(c.cond()))
            #esq
            #   p_IMP_i = P -> I
            p_IMP_i = SImp(pre, c.inv())
            #   i_AND_notB = I & notB
            i_AND_notB = SAnd(c.inv(), NOT_b )
            #   iANDnotB_IMP_Q = iANDnotB -> Q
            iANDnotB_IMP_Q = SImp(i_AND_notB, post)
            #   esq = {P -> I, I & notB -> Q}
            esq = {p_IMP_i, iANDnotB_IMP_Q}
            #dir
            #   p_AND_notB = P & notB
            p_AND_notB = SAnd(pre, NOT_b)
            #dir = VC({P & notB} C {Q})
            dir = VC(p_AND_notB, c.body(), post)
            result = esq.union(dir)
            return result
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
