"""
Open the "show_version.txt" file for reading. Use the .read() method to read in
the entire file contents to a variable.
Print out the file contents to the screen.
Also print out the type of the variable (you should have a string at this
point).

Close the file.

Open the file a second time using a Python context manager (with statement).
Read in the file contents using the .readlines() method.
Print out the file contents to the screen.
Also print out the type of the variable (you should have a list at this point).
"""

from __future__ import print_function
from __future__ import unicode_literals


# Opening a file.
f = open('show_version.txt')
first_read = f.read()
f.close()
f = ''

print(first_read)
print(type(first_read))


# Opening a file using context manager and the readlines method.
with open('show_version.txt') as f:
    second_read = f.readlines()

# f.close() is not required, the close handle happens automatically
# when you get out of an indented block.
f = ''

print(second_read)
print(type(second_read))
