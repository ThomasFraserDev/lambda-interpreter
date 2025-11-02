from ast import Variable, Abstraction, Application
from substitution import substitute

def sendCmds(): # Sends the list of commands, split into sections
    sections = {
        "Expression Creation": [
            "CreateVar <name> [creates a variable]",
            "CreateExpr <expr> [creates an expression]"
        ],
        "Lambda Functionality": [
            "Apply <expr1> <expr2> [applies two expressions]",
            "Substitute <expr> <var> <replacement> [replaces all occurrences of <var> in <expr> with <replacement>]"
        ],
        "Basic Commands": [
            "Commands [prints all commands]",
            "Delete <expr> [deletes an expression]",
            "Show <name> [shows an expression]",
            "List [lists all expressions]",
            "Quit [quits the programme]"
        ]
    }

    print(" " * 14 + "Command List")
    print('-' * 40) # Spacing
    for section, commands in sections.items():
        print(f"\n{section}:") # Print each sections and its commands
        for cmd in commands:
            print(f"{cmd}")
    print('-' * 40) # More spacing
    
def parse(expr): 
    expr = expr.replace("//", "λ")
    if expr.startswith("λ"):
        param = expr[1]
        body = Variable(expr[3:])
        return Abstraction(param, body)
    return Variable(expr)

def saveAsExpr(): #Asks the user whether they want to save a created expression, returning true or false
    print(f"Would you like to save this as an expression? [Y/N]")
    while True:
        answer = input().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid option. Please retry, typing either 'Y' or 'N'.")
            break # Restart loop

expressions = {} # Initialising expression dictionary
exprCounter = 0 # Initialising the number of saved expressions, used for naming conventions

sendCmds()

while True:
    
    cmd = input().strip()
    params = cmd.lower().split() # Split the entered command into sections
    
    # -------------------- Expression Creation --------------------
    
    if params[0] == "createvar" and len(params) == 2:
        exprCounter += 1
        name = f"expr{exprCounter}"
        expressions[name] = Variable(params[1])
        print(f"Variable '{expressions[name]}' created as '{name}'.")
        
    elif params[0] == "createexpr" and len(params) == 2:
        exprCounter += 1
        name = f"expr{exprCounter}"
        expressions[name] = parse(params[1])
        print(f"Expression '{expressions[name]}' created as '{name}'.")
        
    # -------------------- Lambda Operations --------------------
    
    elif params[0] == "apply" and len(params) == 3:
        t1 = expressions.get(params[1])
        t2 = expressions.get(params[2])
        if t1 and t2:
            appTerms = Application(t1, t2)
            print(f"Application of {t1} and {t2}: {appTerms}")
            if saveAsExpr():
                exprCounter += 1
                name = f"expr{exprCounter}"
                expressions[name] = appTerms
                print(f"Expression '{expressions[name]}' created.")
        else:
            print("No expressions found with the entered names.")
    
    elif params[0] == "substitute" and len(params) == 4:
        t1 = expressions.get(params[1])
        t2 = expressions.get(params[2])
        t3 = expressions.get(params[3])
        if t1 and t2 and t3:
            subTerm = substitute(t1, t2.name, t3)
            print(f"Substitution of {t2} for {t3} in {t1}: {subTerm}")
            if saveAsExpr():
                exprCounter += 1
                name = f"expr{exprCounter}"
                expressions[name] = subTerm
                print(f"Expression '{expressions[name]}' created.")
        else:
            print("No expressions found with the entered names.")
            
    # -------------------- Basic Commands --------------------
            
    elif params[0] == "commands" and len(params) == 1:
        sendCmds()
            
    elif params[0] == "delete" and len(params) == 2:
        name = params[1]
        if expressions[name]:
            expressions.__delitem__(name)
            print(f"Expressions {name} deleted successfully.")
        else:
            print("No expression found with that name.")
        
    elif params[0] == "show" and len(params) == 2:
        name = params[1]
        if expressions[name]:
            print(f"{expressions[name]}")
        else:
            print(f"No expression found with that name.")
            
    elif params[0] == "list" and len(params) == 1:
        if expressions:
            for name, expr in expressions.items():
                print(f"{name}: {expr}")
        else:
            print("No expressions have been defined.")
            
    elif params[0].lower() == "quit":
        break
    
    # -------------------- Unknown Command --------------------

    else:
        print("Unknown command or number of arguments.")
        
    print("Enter next command:")