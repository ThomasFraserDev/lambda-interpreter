from ast import Variable, Abstraction, Application

listOrder = ["x", "y", "z", "x'", "y'", "z'"] 

def contains_var(expr, name): # Method that checks whether a variable is contained within an expression
    if isinstance(expr, Variable): #If the expression is a variable, check if its name matches
        return expr.name == name
    elif isinstance(expr, Abstraction): #If it's an abstraction, check the body
        return contains_var(expr.body, name)
    elif isinstance(expr, Application): #If it's an application, check it's function and argument
        return contains_var(expr.func, name) or contains_var(expr.arg, name)
    else:
        return False

def substitute(expr, var, replacement):
    if isinstance(expr, Variable): #If the expression is a variable
        if expr.name == var: #If it matches the variable to be replaced
            return replacement
        else:
            return expr
    
    elif isinstance(expr, Abstraction): #If the expression is an abstraction
        if contains_var(replacement, expr.param): #If substitution would cause variable capture
            for v in listOrder: #Find a variable name not already used
                if not contains_var(expr.body, v) and v != expr.param:
                    substituted = substitute(expr.body, expr.param, Variable(v)) #Rename bound variable
                    return Abstraction(v, substitute(substituted, var, replacement)) #Substitute with renamed variable
        else:
            substituted = substitute(expr.body, var, replacement) #Substitute inside body
            return Abstraction(expr.param, substituted)
        
    elif isinstance(expr, Application): #If the expression is an application
        return Application(substitute(expr.func, var, replacement), substitute(expr.arg, var, replacement))
