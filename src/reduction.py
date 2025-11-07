from ast import Variable, Abstraction, Application
from substitution import substitute
from utils import freeVars

def getBody(expr): # Helper method that recursively gets the true free body of an abstraction
        if isinstance(expr.body, Abstraction):
          getBody(expr.body)
        else:
            return expr.body

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
    
def etaReduce(expr):
    if not isinstance(expr, Abstraction):
        return expr
    
    if isinstance(expr.body, Variable):
        return expr
    
    if isinstance(expr.body, Abstraction): # If the expression is an abstraction
        freeBody = getBody(expr.body) # Find it's true free body
    else:
        freeBody = expr.body
        
    if freeVars(expr.param, freeBody) and isinstance(expr.body, Abstraction): # If the expression is eta reduceable and is an abstraction
        expr2 = etaReduce(Abstraction(str(expr.body)[2], freeBody.func)) # Recursively create the eta reduced expression
    else:
        expr2 = freeBody.func if hasattr(freeBody, "func") else freeBody # Create the eta reduced expression

    return expr2