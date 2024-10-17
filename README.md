# Password Generator with Strength Checker

A simple Python application that generates secure passwords based on user preferences. The program uses the Tkinter library for the graphical user interface (GUI) and provides a strength checker to assess the generated password's robustness. Additionally, users can save the generated password to a text file.

## Features

- **Customizable Password Generation**: 
  - Choose password length.
  - Option to include/exclude uppercase letters, lowercase letters, digits, and special characters.
  
- **Password Strength Checker**: 
  - Evaluates the strength of the generated password (Weak, Moderate, Strong).
  
- **Save Passwords**: 
  - Option to save generated passwords to a `.txt` file for easy access.

## Installation

### Prerequisites

- Python 3.x
- Tkinter (usually included with standard Python installations)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/Cyprians-Mwanza/Password-Generator.git
   cd https://github.com/Cyprians-Mwanza/Password-Generator.git
2.Install required dependencies:
pip install -r requirements.txt
3.Run the application:
python main.py

**Usage**
Open the application.
Set your password preferences (length, character types).
Click "Generate Password" to create a password.
The generated password and its strength will be displayed.
Optionally, save the password by clicking "Save Password."

**How It Works**
The application uses random character selection from user-specified categories (uppercase, lowercase, digits, special characters) to generate a password. The strength checker evaluates the password based on length and the inclusion of different character types.

**Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some amazing feature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.


**Screenshots**
Main Window	Generated Password
<img width="960" alt="Password Generator" src="https://github.com/user-attachments/assets/272aed69-2931-4717-9c55-2edf0f23b6ea">
<img width="960" alt="success Message" src="https://github.com/user-attachments/assets/0dee4740-ab94-4084-a352-11ce9ee425cf">


**License**
Distributed under the MIT License. See LICENSE for more information.

**Acknowledgements**
Built with Tkinter for the GUI.
Uses Python's string and random libraries for password generation.
Password strength checker inspired by general password best practices


