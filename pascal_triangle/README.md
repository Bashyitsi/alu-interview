Pascal's Triangle
This Python program generates Pascal's Triangle up to a specified height and returns it as a list of lists of integers. Pascal's Triangle is a mathematical construct where each number in the triangle is the sum of the two numbers directly above it.

Usage
Make sure you have Python installed on your system.

Clone the repository or download the 0-pascal_triangle.py file.

Run the 0-main.py script to see Pascal's Triangle for a given height. You can adjust the height by changing the input argument in the script.

$ python3 0-main.py
Function
python
Copy code
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified height.

    :param n: The height of the Pascal's Triangle.
    :return: A list of lists representing Pascal's Triangle.
    """
n: An integer representing the height of the Pascal's Triangle. Returns an empty list if n is less than or equal to 0.
Example
Here is an example of running the program with a height of 5 in the 0-main.py script:

python
Copy code
from 0-pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row]))

print_triangle(pascal_triangle(5))
This will output:

csharp
Copy code
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
