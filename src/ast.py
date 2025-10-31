class Variable:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    
class Abstraction:
    def __init__(self, param, body):
        self.param = param
        self.body = body
    def __repr__(self):
        return f"(λ{self.param}.{self.body})"

class Application:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg
    def __repr__(self):
        return f"({self.func} {self.arg})"