from ast import Variable, Abstraction, Application
from substitution import substitute

def parse(expr):
    expr = expr.replace("//", "λ")
    if expr.startswith("λ"):
        param = expr[1]
        body = Variable(expr[3:])
        return Abstraction(param, body)
    return Variable(expr)

print("Command List:")
print("     CreateVar <name>")
print("     CreateExpr <expr>")
print("     Apply <t1> <t2>")
print("     Substitute <t1> <var> <replacement>")
print("     Show <name>")
print("     List")
print("     Quit")

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
    
    elif params[0] == "substitute" and len(params) == 4:
        term_name, var, repl_name = params[1], params[2], params[3]
        term = terms[term_name]
        replacement = terms[repl_name]
        exprCounter += 1
        name = f"expr{exprCounter}"
        terms[name] = substitute(term, var, replacement)
        print(f"Substitution '{name}' = {terms[name]} created.")
        
            
    elif params[0] == "show" and len(params) == 2:
        name = params[1]
        if terms[name]:
            print(f"{terms[name]}")
        else:
            print(f"No expression found with that name.")
            
    elif params[0] == "list" and len(params) == 1:
        if terms:
            for name, expr in terms.items():
                print(f"{name}: {expr}")
        else:
            print("No expressions have been defined.")

    else:
        print("Unknown command or number of arguments.")