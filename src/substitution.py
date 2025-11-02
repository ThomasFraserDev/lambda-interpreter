from ast import Variable, Abstraction, Application

listOrder = ["x", "y", "z", "x'", "y'", "z'"]

def contains_var(term, name):
    if isinstance(term, Variable):
        return term.name == name
    elif isinstance(term, Abstraction):
        return contains_var(term.body, name)
    elif isinstance(term, Application):
        return contains_var(term.func, name) or contains_var(term.arg, name)
    else:
        return False

def substitute(term, var, replacement):
    
    if isinstance(term, Variable):
        if term.name == var:
            return replacement
        else:
            return term
    
    elif isinstance(term, Abstraction):
        if contains_var(replacement, term.param):
            for v in listOrder:
                if not contains_var(term.body, v) and v != term.param:
                    substituted = substitute(term.body, term.param, Variable(v))
                    return Abstraction(v, substitute(substituted, var, replacement))
        else:
            substituted = substitute(term.body, var, replacement)
            return Abstraction(term.param, substituted)
        
    elif isinstance(term, Application):
        return Application(substitute(term.func, var, replacement), substitute(term.arg, var, replacement))