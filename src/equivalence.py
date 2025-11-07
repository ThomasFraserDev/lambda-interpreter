from reduction import betaReduce, etaReduce
from ast import Variable, Abstraction, Application

def alphaEquivalent(e1, e2, env=None): # Method that recursively checks whether two expressions are structurally the same
    if env is None:
        env = {}
        
    if isinstance(e1, Variable) and isinstance(e2, Variable): # If the expressions are variables
        if e1.name in env:
            return env[e1.name] == e2.name
        return e1.name == e2.name
    
    if isinstance(e1, Abstraction) and isinstance(e2, Abstraction): # If the expressions are abstractions
        new_env = env.copy()
        new_env[e1.param] = e2.param
        return alphaEquivalent(e1.body, e2.body, new_env)
    
    if isinstance(e1, Application) and isinstance(e2, Application): # If the expressions are applications
        return (alphaEquivalent(e1.func, e2.func, env)
                and alphaEquivalent(e1.arg, e2.arg, env))
    return False

def equivalent(expr1, expr2):
    e1 = etaReduce(betaReduce(expr1))
    e2 = etaReduce(betaReduce(expr2))
    return alphaEquivalent(e1, e2)