from ast import Variable, Abstraction, Application
from parser import parse
from substitution import substitute
from reduction import betaReduce, etaReduce

def sendCmds(): # Sends the list of commands, split into sections
    sections = {
        "Expression Creation": [
            "CreateVar <name> [creates a variable]",
            "CreateExpr <expr> [creates an expression]"
        ],
        "Lambda Functionality": [
            "Apply <expr1> <expr2> [applies two expressions]",
            "Substitute <expr> <var> <replacement> [replaces all occurrences of <var> in <expr> with <replacement>]",
            "BetaRed <expr> [beta reduces a given expression]",
            "EtaRed <expr> [eta reduces a given expression]",
            "BetaEtaRed <expr [beta eta reduces a given expression]"
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
            
def startREPL():

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
            e1 = expressions.get(params[1])
            e2 = expressions.get(params[2])
            if e1 and e2: # If the entered expression names exist
                appTerms = Application(e1, e2)
                print(f"Application of {e1} and {e2}: {appTerms}")
                if saveAsExpr():
                    exprCounter += 1
                    name = f"expr{exprCounter}"
                    expressions[name] = appTerms # Setting exprx to be the applied expressions
                    print(f"Expression '{expressions[name]}' created as {name}.")
            else:
                print("No expressions found with the entered names.")
    
        elif params[0] == "substitute" and len(params) == 4: # Substituting a variable into an expression
            e1 = expressions.get(params[1])
            e2 = expressions.get(params[2])
            e3 = expressions.get(params[3])
            if e1 and e2 and e3: # If the expression, and original and replacement variables exist
                subTerm = substitute(e1, e2.name, e3)
                print(f"Substitution of {e2} for {e3} in {e1}: {subTerm}")
                if saveAsExpr():
                    exprCounter += 1
                    name = f"expr{exprCounter}"
                    expressions[name] = subTerm # Setting exprx to be the substituted expression
                    print(f"Expression '{expressions[name]}' created as {name}.")
            else:
                print("No expressions found with the entered names.")
            
        elif params[0] == "betared" and len(params) == 2: # Beta reducing an expression
            e1 = expressions.get(params[1])
            if e1:
                redTerm = betaReduce(e1)
                print(f"The beta normal form of {e1} is: {redTerm}")
                if saveAsExpr():
                    exprCounter += 1
                    name = f"expr{exprCounter}"
                    expressions[name] = redTerm # Setting exprx to be the beta reduced expression
                    print(f"Expression '{expressions[name]}' created as {name}.")
            else:
                print("No expressions found with the entered names.")
            
        elif params[0] == "etared" and len(params) == 2: # Eta reducing an expression
            e1 = expressions.get(params[1])
            if e1:
                redTerm = etaReduce(e1)
                print(f"The eta normal form of {e1} is: {redTerm}")
                if saveAsExpr():
                    exprCounter += 1
                    name = f"expr{exprCounter}"
                    expressions[name] = redTerm # Setting exprx to be the eta reduced expression
                    print(f"Expression '{expressions[name]}' created as {name}.")
            else:
                print("No expressions found with the entered names.")
                
        elif params[0] == "betaetared" and len(params) == 2: # Beta eta reducing an expression
            e1 = expressions.get(params[1])
            if e1:
                redTerm = betaReduce(e1)
                redTerm = etaReduce(e1)
                print(f"The beta eta normal form of {e1} is: {redTerm}")
                if saveAsExpr():
                    exprCounter += 1
                    name = f"expr{exprCounter}"
                    expressions[name] = redTerm # Setting exprx to be the beta eta reduced expression
                    print(f"Expression '{expressions[name]}' created as {name}.")
            else:
                print("No expressions found with the entered names.")
            
        # -------------------- Basic Commands --------------------
            
        elif params[0] == "commands" and len(params) == 1: # Showing list of commands
            sendCmds()
            
        elif params[0] == "delete" and len(params) == 2: # Deleting an expression
            name = params[1]
            if name in expressions:
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