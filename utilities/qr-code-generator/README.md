# QR Code Generator

A customizable Python application that generates QR codes from text or URLs and saves them as PNG images.

This project is part of my Python Toolbox, a growing collection of practical projects developed to improve my Python skills through hands-on learning.

## Features

- Generate QR codes from text or URLs
- Validate empty content
- Customize output filenames
- Automatically add the PNG extension
- Choose foreground and background colors
- Use default colors when no color is provided
- Automatically adjust QR code capacity
- Configure module size and border
- Export QR codes as PNG images

## Technologies

- Python
- qrcode
- Pillow
- time (Python standard library)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

1. Enter a text or URL.
2. Choose a filename or press Enter to use the default.
3. Choose a foreground color.
4. Choose a background color.
5. The generated QR code will be saved as a PNG image.

Use color names in English, such as purple, blue, green, black, and white.

## Default Settings

| Setting | Default value |
|---|---|
| Filename | document.png |
| Foreground color | black |
| Background color | white |
| Initial QR code version | 1 |
| Box size | 10 |
| Border | 4 |

## What I Learned

- Working with external libraries
- Reading technical documentation
- Handling user input
- String manipulation
- Conditional statements
- Independent conditions
- Variable reassignment
- F-strings
- Classes and objects
- Functions and methods
- Image generation and customization
- Testing and debugging

## Roadmap

- [x] Basic QR code generation
- [x] Empty input validation
- [x] PNG image export
- [x] Custom filenames
- [x] File extension validation
- [x] Custom foreground and background colors
- [x] Default color settings
- [ ] Invalid color validation
- [ ] Error handling
- [ ] User-defined dimensions and borders
- [ ] Support for document links
- [ ] Graphical interface with Tkinter
- [ ] Modern interface with CustomTkinter
- [ ] Google Drive integration
- [ ] Web application with Streamlit

## Current Version

v1.2 — Implemented and successfully tested in Google Colab.

## Documentation

- [qrcode](https://pypi.org/project/qrcode/)
- [Python](https://docs.python.org/3/)