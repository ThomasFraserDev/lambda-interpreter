from ast import Variable, Abstraction, Application

def parse(expr):
    expr = expr.replace("//", "λ").strip() # Replace //s with λ
    if expr.startswith("λ"):
        param, body = expr[1], expr[3:] # Split the lambda and its body up, then recursively parse the body
        return Abstraction(param, parse(body))
    elif len(expr) > 1: # If the remaining body is an application
        if len(expr) >= 3:
        # The inner application is just the first two
            inner = Application(parse(expr[0]), parse(expr[1]))
        # The outer application applies that to the rest
            glorp = Application(inner, parse(expr[2:]))
            print(f"m{glorp}")
            return glorp
        else:
            return Application(parse(expr[0]), parse(expr[1]))
    else: # Otherwise the remaining body must be a variable
        return Variable(expr)