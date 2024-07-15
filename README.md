# Password Strength Checker

This is a Python-based GUI application that checks the strength of a password and generates strong passwords. The application uses the `tkinter` library for the graphical user interface and the `re` library for regular expression operations.

## Features
   
-Password Strength Checker: Evaluates the strength of a given password based on length, the presence of lowercase and uppercase letters, digits, and special characters.
-Password Generator: Generates a strong random password.
-Password Visibility Toggle: Allows the user to toggle the visibility of the entered password.
-Entropy Calculation: Shows the entropy of the password when checking its strength.

## Installation

1. Clone the repository to your local machine:
    bash
    git clone https://github.com/yourusername/PasswordStrengthChecker.git
    cd PasswordStrengthChecker
    

2. Ensure you have Python installed on your system. You can download Python from https://www.python.org/

3. (Optional) Create a virtual environment and activate it:
    bash
    python3 -m venv venv
    source venv/bin/activate
    

4. Install the required packages (if any):
    bash
    pip install -r requirements.txt
    

## Usage

1. Run the `password_checker.py` script:
    bash
    python password_checker.py
    

2. The GUI window will open. You can enter a password to check its strength, generate a strong password, and toggle password visibility using the provided buttons.

## Project Structure

- `password_checker.py`: The main script containing the application logic.
- `README.md`: This file.
- `eye_open.png` and `eye_closed.png`: Images used for the password visibility toggle button.


## Acknowledgments

- The `tkinter` library for the GUI.
- The `re` library for regular expression operations.
- The `string` and `random` libraries for password generation.
- The `math` library for entropy calculation.

## Contact

For any questions or suggestions, please contact [mdevanandana.2002@gmail.com].
   
