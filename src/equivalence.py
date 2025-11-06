from ast import Variable, Abstraction, Application
from reduction import betaReduce, etaReduce

def alphaEquivalent(e1, e2, env=None): # Method that checks whether two expressions are alpha equivalent (structurally the same)
    if env is None:
        env = {}
    if isinstance(e1, Variable) and isinstance(e2, Variable): # Compare two variables
        return env.get(e1.name, e1.name) == e2.name
    if isinstance(e1, Abstraction) and isinstance(e2, Abstraction): # Compare two abstractions recursively 
        new_env = env.copy()
        new_env[e1.param] = e2.param
        return alphaEquivalent(e1.body, e2.body, new_env)
    if isinstance(e1, Application) and isinstance(e2, Application): # Compare two applications recursively
        return (alphaEquivalent(e1.func, e2.func, env) and
                alphaEquivalent(e1.arg, e2.arg, env))
    return False # If both expressions aren't the same type, they cannot be equivalent so return false

def equivalent(expr1, expr2): # Method that checks if two expressions are logically equivalent
    e1 = etaReduce(betaReduce(expr1)) # Reduce expressions as far as possible
    e2 = etaReduce(betaReduce(expr2))
    return alphaEquivalent(e1, e2) # Check the expressions structurally match