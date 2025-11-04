from ast import Variable, Abstraction, Application
from substitution import substitute

def betaReduce(expr):
    if isinstance(expr, Application): #If the expression is an application (and hence can be beta reduced)
        if isinstance(expr.func, Abstraction): #If the first expression is an abstraction
            return betaReduce(substitute(expr.func.body, expr.func.param, expr.arg)) # Remove it's lambda term and recursively call betaReduce, substituting in the applied expression for the lambda term in the body
        else:
            return Application(betaReduce(expr.func), betaReduce(expr.arg))
    elif isinstance(expr, Abstraction):
        return Abstraction(expr.param, betaReduce(expr.body))
    else:
        return expr