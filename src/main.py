from ast import Variable, Abstraction, Application

def parse(expr):
    expr = expr.replace("//", "λ")
    if expr.startswith("λ"):
        param = expr[1]
        body = expr[3:]
        return Abstraction(param, body)

print("Command List:")
print("     CreateVar <name>    -> create a variable")
print("     CreateExpr <expr>   -> create an expression (you may use // to represent λ)")
print("     Apply <t1> <t2>     -> apply two terms together")
print("     Quit                -> exit")

terms = {}
exprCounter = 0

while True:
    
    cmd = input().strip()
    params = cmd.lower().split()
    
    if params[0].lower() == "quit":
        break
    
    elif params[0] == "createvar" and len(params) == 2:
        name = params[1]
        terms[name] = Variable(name)
        print(f"Variable '{name}' created.")
        
    elif params[0] == "createexpr" and len(params) == 2:
        exprCounter += 1
        name = f"expr{exprCounter}"
        terms[name] = parse(params[1])
        print(f"Expression '{terms[name]}' created.")
    
    elif params[0] == "apply" and len(params) == 3:
        t1 = terms.get(params[1])
        t2 = terms.get(params[2])
        if t1 and t2:
            exprCounter += 1
            name = f"expr{exprCounter}"
            appTerms = Application(t1, t2)
            terms[name] = appTerms
            print(f"Expression '{terms[name]}' created.")

    else:
        print("Unknown command or number of arguments.")