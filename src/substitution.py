from ast import Variable, Abstraction, Application
from utils import containsVar

listOrder = ["x", "y", "z", "x'", "y'", "z'"] 

def substitute(expr, var, replacement):
    if isinstance(expr, Variable): #If the expression is a variable
        if expr.name == var: #If it matches the variable to be replaced
            return replacement
        else:
            return expr
    
    elif isinstance(expr, Abstraction): #If the expression is an abstraction
        if containsVar(replacement, expr.param): #If substitution would cause variable capture
            for v in listOrder: #Find a variable name not already used
                if not containsVar(expr.body, v) and v != expr.param:
                    substituted = substitute(expr.body, expr.param, Variable(v)) #Rename bound variable
                    return Abstraction(v, substitute(substituted, var, replacement)) #Substitute with renamed variable
        else:
            substituted = substitute(expr.body, var, replacement) #Substitute inside body
            return Abstraction(expr.param, substituted)
        
    elif isinstance(expr, Application): #If the expression is an application
        return Application(substitute(expr.func, var, replacement), substitute(expr.arg, var, replacement))
