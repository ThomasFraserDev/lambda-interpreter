from ast import Variable, Abstraction, Application

def parse(expr):
    expr = expr.replace("//", "λ").strip() # Replace //s with λ
    if expr.startswith("λ"):
        param, body = expr[1], expr[3:] # Split the lambda and its body up, then recursively parse the body
        return Abstraction(param, parse(body))
    elif len(expr) > 1:
        # Start with the first two terms
        app = Application(parse(expr[0]), parse(expr[1]))
        # Then fold over the remaining terms, left-associatively
        for ch in expr[2:]:
            app = Application(app, parse(ch))
        return app
    else: # Otherwise the remaining body must be a variable
        return Variable(expr)