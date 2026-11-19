# 📱 QR Code Generator

A customizable command-line QR code generator built with Python that converts text and URLs into personalized PNG images.

This project is part of **Python Toolbox**, a collection of practical Python projects designed to develop programming skills, explore Python libraries, and apply software development best practices.

## 📌 Project Status

🚧 Currently in development — Version 1.2

## ✨ Features

- Generate QR codes from text or URLs.
- Empty content validation.
- Custom output filenames.
- Automatic PNG extension handling.
- Default filename when no name is provided.
- Customizable foreground and background colors.
- Default color settings.
- Automatic QR code capacity adjustment.
- Configurable module size and border through code.
- PNG image export.
- Interactive command-line interface.

## 🛠️ Technologies

- Python 3
- `qrcode` — Generates and configures QR codes.
- `Pillow` — Supports image generation and processing.
- `time` — Controls execution delays.
- Git and GitHub — Version control.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed.
- Required Python dependencies.

### Installation

Navigate to the project directory:

```bash
cd utilities/qr-code-generator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project

Run the application:

```bash
python main.py
```

Follow the on-screen instructions to generate and customize your QR code.

## 💻 Usage Example

```
=== QR Code Generator ===

Digite um texto ou URL: https://github.com
Conteúdo informado: https://github.com

Digite o nome que deseja no arquivo ou enter para nome padrão: github

Digite a cor do QR Code: purple
Digite a cor do fundo do QR Code: white

Gerando QRCode
QRCode gerado com sucesso!
Nome do arquivo: github.png
```

The generated QR code will be saved in the current working directory when a simple filename is provided.

Use valid color names in English or supported hexadecimal color codes.

The current command-line interface is available in Brazilian Portuguese.

## ⚙️ Default Settings

| Setting | Default Value |
|---|---|
| Filename | document.png |
| Foreground color | black |
| Background color | white |
| Initial QR code version | 1 |
| Box size | 10 |
| Border | 4 |
| File format | PNG |

## 📚 Learning Objectives

This project focuses on developing practical knowledge of:

- Python standard library modules.
- External Python libraries and dependencies.
- Reading technical documentation.
- Variables and data types.
- String manipulation.
- String methods: strip(), lower(), and endswith().
- User input and output.
- Conditional statements.
- Independent conditional statements.
- Logical operators.
- Variable reassignment.
- String formatting with f-strings.
- Introduction to classes and objects.
- Functions, methods, and arguments.
- Image generation and customization.
- Incremental development.
- Manual testing and debugging.
- Version control.

## 🗺️ Development Roadmap

- V1.0 — Basic QR code generation.
- V1.1 — Custom filenames and PNG extension handling.
- V1.2 — Color customization and default settings.
- V1.3 — Input validation and error handling.
- V1.4 — User-defined dimensions and borders.
- V1.5 — Support for additional content types and document links.
- V2.0 — Graphical user interface with Tkinter.
- V2.1 — Modern desktop interface with CustomTkinter.
- V2.2 — Google Drive integration.
- V3.0 — Web application with Streamlit.
- Final documentation and testing.

## ⚠️ Current Limitations

- Invalid color names are not yet handled.
- Color contrast is not automatically validated.
- Invalid filenames are not yet handled.
- Existing files may be overwritten.
- Module size and border cannot yet be customized through user input.
- Document upload and sharing are not yet supported.
- No graphical user interface is currently available.

These limitations will be addressed in future versions.

## 🧪 Testing

Version 1.2 has been successfully tested.

## 📖 References

- [Python Documentation](https://docs.python.org/3/)
- [qrcode Documentation](https://pypi.org/project/qrcode/)
- [Pillow Documentation](https://pillow.readthedocs.io/)

---

Part of the **Python Toolbox** project — learning Python through practical, incremental development.