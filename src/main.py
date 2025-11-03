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
    expr = expr.replace("//", "λ").strip() # Replace //s with λ
    if expr.startswith("λ"):
        param, body = expr[1], expr[3:] # Split the lambda and its body up, then recursively parse the body
        return Abstraction(param, parse(body))
    elif len(expr) > 1: # If the remaining body is an application
        return Application(parse(expr[0]), parse(expr[1:]))
    else: # Otherwise the remaining body must be a variable
        return Variable(expr)

def saveAsExpr(): # Asks the user whether they want to save a created expression, returning true or false
    print(f"Would you like to save this as an expression? [Y/N]")
    while True:
        answer = input().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid option. Please retry, typing either 'Y' or 'N'.")

expressions = {} # Initialising expression dictionary
exprCounter = 0 # Initialising the number of saved expressions, used for naming conventions

sendCmds()

while True:
    
    cmd = input().strip()
    params = cmd.lower().split() # Split the entered command into sections
    
    # -------------------- Expression Creation --------------------
    
    if params[0] == "createvar" and len(params) == 2: # Creating a variable 
        exprCounter += 1
        name = f"expr{exprCounter}"
        expressions[name] = Variable(params[1]) # Setting exprx to be the entered variable
        print(f"Variable '{expressions[name]}' created as '{name}'.")
        
    elif params[0] == "createexpr" and len(params) == 2: # Creating an expression
        exprCounter += 1
        name = f"expr{exprCounter}"
        expressions[name] = parse(params[1]) # Setting exprx to be the entered and parsed expression
        print(f"Expression '{expressions[name]}' created as '{name}'.")
        
    # -------------------- Lambda Operations --------------------
    
    elif params[0] == "apply" and len(params) == 3: # Applying two expressions together
        t1 = expressions.get(params[1])
        t2 = expressions.get(params[2])
        if t1 and t2: # If the entered expression names exist
            appTerms = Application(t1, t2)
            print(f"Application of {t1} and {t2}: {appTerms}")
            if saveAsExpr():
                exprCounter += 1
                name = f"expr{exprCounter}"
                expressions[name] = appTerms # Setting exprx to be the applied expressions
                print(f"Expression '{expressions[name]}' created.")
        else:
            print("No expressions found with the entered names.")
    
    elif params[0] == "substitute" and len(params) == 4: # Substituting a variable into an expression
        t1 = expressions.get(params[1])
        t2 = expressions.get(params[2])
        t3 = expressions.get(params[3])
        if t1 and t2 and t3: # If the expression, and original and replacement variables exist
            subTerm = substitute(t1, t2.name, t3)
            print(f"Substitution of {t2} for {t3} in {t1}: {subTerm}")
            if saveAsExpr():
                exprCounter += 1
                name = f"expr{exprCounter}"
                expressions[name] = subTerm # Setting exprx to be the substituted expression
                print(f"Expression '{expressions[name]}' created.")
        else:
            print("No expressions found with the entered names.")
            
    # -------------------- Basic Commands --------------------
            
    elif params[0] == "commands" and len(params) == 1: # Showing list of commands
        sendCmds()
            
    elif params[0] == "delete" and len(params) == 2: # Deleting an expression
        name = params[1]
        if expressions[name]:
            expressions.__delitem__(name)
            print(f"Expressions {name} deleted successfully.")
        else:
            print("No expression found with that name.")
        
    elif params[0] == "show" and len(params) == 2: # Showing an expression
        name = params[1]
        if expressions[name]:
            print(f"{expressions[name]}")
        else:
            print(f"No expression found with that name.")
            
    elif params[0] == "list" and len(params) == 1: # Listing all expressions
        if expressions:
            for name, expr in expressions.items():
                print(f"{name}: {expr}")
        else:
            print("No expressions have been defined.")
            
    elif params[0].lower() == "quit": # Quitting
        break
    
    # -------------------- Unknown Command --------------------

    else:
        print("Unknown command or number of arguments.")
        
    print("Enter next command:")