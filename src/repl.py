from ast import Variable, Application
from operations.parser import parse
from operations.substitution import substitute
from operations.reduction import betaReduce, etaReduce
from operations.equivalence import equivalent

def sendCmds(): # Sends the list of commands, split into sections
    sections = {
        "Expression Creation": [
            "CreateVar <expr> [creates a variable]",
            "CreateExpr <expr> [creates an expression]"
        ],
        "Lambda Functionality": [
            "Apply <expr1> <expr2> [applies two expressions]",
            "Substitute <expr> <var> <replacement> [replaces all occurrences of <var> in <expr> with <replacement>]",
            "Equivalent <expr1> <expr2> [checks that two expressions are logically equivalent]",
            "BetaRed <expr> [beta reduces a given expression]",
            "EtaRed <expr> [eta reduces a given expression]",
            "BetaEtaRed <expr [beta eta reduces a given expression]"
        ],
        "Basic Commands": [
            "Commands [prints all commands]",
            "Shortcuts [prints all command shortcuts]",
            "Rename <name> <newName> [renames an expression]",
            "Delete <expr> [deletes an expression]",
            "DeleteAll [deletes all expressions]",
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
    
def sendShortcuts(): # Sends the list of command shortcuts, split into sections
    sections = {
        "Expression Creation": [
            "CreateVar -> CV",
            "CreateExpr -> CE"
        ],
        "Lambda Functionality": [
            "Apply -> APP",
            "Substitute -> SUB",
            "Equivalent -> EQ",
            "BetaRed -> BR",
            "EtaRed -> ER",
            "BetaEtaRed -> BER"
        ],
        "Basic Commands": [
            "Commands -> CMDS",
            "Shortcuts -> SC",
            "Rename -> RN",
            "Delete -> DEL",
            "DeleteAll -> DELA"
            "Show -> S",
            "List -> L",
            "Quit -> Q"
        ]
    }
    
    print(" " * 9 + "Command Shortcut List")
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
    
        if (params[0] == "createvar" or params[0] == "cv") and len(params) == 2: # Creating a variable 
            exprCounter += 1
            name = f"expr{exprCounter}"
            expressions[name] = Variable(params[1]) # Setting exprx to be the entered variable
            print(f"Variable '{expressions[name]}' created as '{name}'.")
        
        elif (params[0] == "createexpr" or params[0] == "ce") and len(params) == 2: # Creating an expression
            exprCounter += 1
            name = f"expr{exprCounter}"
            expressions[name] = parse(params[1]) # Setting exprx to be the entered and parsed expression
            print(f"Expression '{expressions[name]}' created as '{name}'.")
        
        # -------------------- Lambda Operations --------------------
    
        elif (params[0] == "apply" or params[0] == "app") and len(params) == 3: # Applying two expressions together
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
    
        elif (params[0] == "substitute" or params[0] == "sub") and len(params) == 4: # Substituting a variable into an expression
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
                
        elif (params[0] == "equivalent" or params[0] == "eq") and len(params) == 3:
            e1 = expressions.get(params[1])
            e2 = expressions.get(params[2])
            if e1 and e2:
                if equivalent(e1, e2):
                    print(f"{e1} and {e2} are logically equivalent.")
                else:
                    print(f"{e1} and {e2} are not logically equivalent.")
            else:
                print("No expressions found with the entered names.")
            
        elif (params[0] == "betared" or params[0] == "br") and len(params) == 2: # Beta reducing an expression
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
            
        elif (params[0] == "etared" or params[0] == "er") and len(params) == 2: # Eta reducing an expression
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
                
        elif (params[0] == "betaetared" or params[0] == "ber") and len(params) == 2: # Beta eta reducing an expression
            e1 = expressions.get(params[1])
            if e1:
                redTerm = etaReduce(betaReduce(e1))
                print(f"The beta eta normal form of {e1} is: {redTerm}")
                if saveAsExpr():
                    exprCounter += 1
                    name = f"expr{exprCounter}"
                    expressions[name] = redTerm # Setting exprx to be the beta eta reduced expression
                    print(f"Expression '{expressions[name]}' created as {name}.")
            else:
                print("No expressions found with the entered names.")
            
        # -------------------- Basic Commands --------------------
            
        elif (params[0] == "commands" or params[0] == "cmds") and len(params) == 1: # Show list of all commands
            sendCmds()
            
        elif (params[0] == "shortcuts" or params[0] == "sc") and len(params) == 1: # Show list of all command shortcuts
            sendShortcuts()

        elif (params[0] == "rename" or params[0] == "rn") and len(params) == 3: # Renames a created expression
            name = params[1]
            newName = params[2]
            if expressions[name]:
                expressions[newName] = expressions[name]
                expressions.__delitem__(name)
                print(f"Expression {expressions[newName]} renamed to {newName}.")
            else:
                print(f"No expressions found with name {name}.")
            
        elif (params[0] == "delete" or params[0] == "del") and len(params) == 2: # Delete a created expression
            name = params[1]
            if name in expressions:
                expressions.__delitem__(name)
                print(f"Expressions {name} deleted successfully.")
            else:
                print("No expression found with that name.")
                
        elif (params[0] == "deleteall" or params[0] == "dela") and len(params) == 1: # Delete all created expressions
            if expressions:
                expressions.clear()
                print(f"Expressions deleted successfully.")
            else:
                print("No expressions found.")
        
        elif (params[0] == "show" or params[0] == "s") and len(params) == 2: # Show a created expression
            name = params[1]
            if expressions[name]:
                print(f"{expressions[name]}")
            else:
                print(f"No expression found with that name.")
            
        elif (params[0] == "list" or params[0] == "l") and len(params) == 1: # List all created expressions
            if expressions:
                for name, expr in expressions.items():
                    print(f"{name}: {expr}")
            else:
                print("No expressions have been defined.")
            
        elif (params[0].lower() == "quit" or params[0] == "q"): # Quit
            break
    
    # -------------------- Unknown Command --------------------

        else:
            print("Unknown command or number of arguments.")
        
        print("Enter next command:")