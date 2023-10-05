Rainwater Trapping Project
This project is designed to solve the problem of calculating the amount of rainwater retained between walls represented by a list of non-negative integers. It follows specific guidelines and requirements.

Project Requirements
The code is written in Python 3.4.3.
Allowed editors: vi, vim, emacs.
All files end with a new line.
The first line of all files is #!/usr/bin/python3.
A README.md file is included at the root of the project folder.
The code follows the PEP 8 style (version 1.7.x).
No external modules are imported.
All modules and functions are documented.
All files are executable.
Usage
To calculate the amount of rainwater retained, use the provided rain function in the 0-rain.py file. You can call the function with a list of non-negative integers representing wall heights.

Example usage in 0_main.py:

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # Output: 6
File Structure
0-rain.py: Contains the implementation of the rain function.
0_main.py: Example usage of the rain function.
README.md: This documentation file.
