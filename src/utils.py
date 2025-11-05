from ast import Variable, Abstraction, Application

def containsVar(expr, name): # Method that checks whether a variable is contained within an expression
    if isinstance(expr, Variable): #If the expression is a variable, check if its name matches
        return expr.name == name
    elif isinstance(expr, Abstraction): #If it's an abstraction, check the body
        return containsVar(expr.body, name)
    elif isinstance(expr, Application): #If it's an application, check it's function and argument
        return containsVar(expr.func, name) or containsVar(expr.arg, name)
    else:
        return False
    
def freeVars(v, expr): # Method that checks if a variable v occurs only in the last slot of expression expr
    exprS = str(expr)
    for i in range(len(exprS)):
        if exprS[i] == v and i != (len(exprS) - 1):
            return False
        elif exprS[i] == v and i == (len(exprS) - 1):
            return True
