# Lambda Interpreter
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](./LICENSE)

A command-line REPL for manipulating and reducing lambda calculus expressions with support for β-reduction, η-reduction, substitution, and α-equivalence checking.

## Features

- **Expression Creation**: Build lambda terms and variables
- **Lambda Calculus Operations**:
  - β-reduction: Apply functions to arguments
  - η-reduction: Simplify redundant abstractions (supports multi-parameter reduction)
  - Capture-avoiding substitution
  - Application of terms
- **Equivalence Checking**: Test if two expressions are logically equivalent (α-equivalence after normalization)
- **Interactive REPL**: Manage expressions with save/show/list/delete commands

## Command List

### Expression Creation
- `CreateVar <name>` - Create a variable
- `CreateExpr <expr>` - Parse and create an expression (use `//` for λ)

### Lambda Functionality
- `Apply <expr1> <expr2>` - Apply two expressions together
- `Substitute <expr> <var> <replacement>` - Replace all free occurrences of a variable
- `Equivalent <expr1> <expr2>` - Checks that two expressions are α-equivalent
- `BetaRed <expr>` - β-reduce to normal form
- `EtaRed <expr>` - η-reduce to normal form
- `BetaEtaRed <expr>` - βη-reduce to normal form

### Basic Commands
- `Commands` - Display all available commands
- `Shortcuts` - Display all available command shortcuts
- `Rename <name> <newName>` - Rename an expression
- `Delete <expr>` - Remove an expression
- `DeleteAll` - Remove all expression
- `Show <name>` - Display a specific expression
- `List` - List all saved expressions
- `Quit` - Exit the interpreter

## How To Run

### Prerequisites

- **Python** 3.8 or higher

### Run the Interpreter

From the repository root:
```bash
python3 src/main.py
```

Or if you're in the `src` directory:
```bash
python3 main.py
```

## Project Structure

```
lambda-interpreter/
├── src/
│   ├── ast.py           # AST node definitions (Variable, Abstraction, Application)
│   ├── parser.py        # Parse lambda expressions from strings
│   ├── substitution.py  # Capture-avoiding substitution logic
│   ├── reduction.py     # β and η reduction algorithms
│   ├── equivalence.py   # α-equivalence and logical equivalence checking
│   ├── utils.py         # Helper functions
│   ├── repl.py          # REPL implementation
│   └── main.py          # Entry point
├── README.md
└── LICENSE
```
## Contributing

Contributions are welcome! :]

If you’d like to help improve this lambda interpreter, please follow these steps:
1. Fork the repository and create a new branch from main.
2. For UI changes, screenshots or short clips are encouraged.
3. Make sure the project runs locally:
```bash
npm install
npm run dev
```
4. Open a Pull Request with:
- A clear description of what you changed or added 
- The reasoning behind it

If you’re unsure about an idea or want feedback before starting, feel free to open an issue to discuss it first.

Thanks for helping make this project better! 💜

## License

This software is licensed under the MIT license.
