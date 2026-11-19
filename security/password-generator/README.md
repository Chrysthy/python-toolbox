# 🔐 Password Generator

A customizable command-line password generator built with Python, using cryptographically secure random character selection.

This project is part of **Python Toolbox**, a collection of practical Python projects designed to develop programming skills, explore Python libraries, and apply software development best practices.

## 📌 Project Status

🚧 Currently in development — Version 1.2

## ✨ Features

- Random password generation.
- Custom password length.
- Customizable character selection:
  - Lowercase letters.
  - Uppercase letters.
  - Numbers.
  - Special characters.
- Cryptographically secure random character selection using Python's `secrets` module.
- Password length display.
- Interactive command-line interface.

## 🛠️ Technologies

- Python 3
- `string` — Provides predefined character sets.
- `secrets` — Provides cryptographically secure random selection.
- Git and GitHub — Version control.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed.

No external dependencies are required. This project uses only Python standard library modules.

### Running the Project

Navigate to the project directory:

```bash
cd security/password-generator
```

Run the application:

```bash
python main.py
```

Follow the on-screen instructions to customize and generate your password.

## 💻 Usage Example

```text
=== Password Generator ===

Quantos caracteres deseja na senha? 16
Incluir letras minúsculas? (s/n) s
Incluir letras maiúsculas? (s/n) s
Incluir números? (s/n) s
Incluir símbolos? (s/n) s

Senha Gerada: kR7@m2L#p9X!a4&B
Quantidade de caracteres: 16
```

The generated password will vary with each execution.

The current command-line interface is available in Brazilian Portuguese.

## 📚 Learning Objectives

This project focuses on developing practical knowledge of:

- Python standard library modules.
- String manipulation and concatenation.
- Variables and data types.
- User input and type conversion.
- Conditional statements.
- Loops and string accumulation.
- Secure random character selection.
- Incremental development.
- Manual testing and version control.

## 🗺️ Development Roadmap

- [x] V1.0 — Basic password generation.
- [x] V1.1 — Custom password length.
- [x] V1.2 — Character type customization.
- [ ] V1.3 — Input validation and error handling.
- [ ] V1.4 — Guaranteed inclusion of selected character types.
- [ ] V1.5 — Code refactoring and functions.
- [ ] Final documentation and testing.

## 🔒 Current Limitations

- Input validation is not yet implemented.
- Password length restrictions are not yet enforced.
- At least one character type must be selected.
- Selecting a character type does not currently guarantee its presence in the generated password.

These limitations will be addressed in future versions.

---

Part of the **Python Toolbox** project — learning Python through practical, incremental development.