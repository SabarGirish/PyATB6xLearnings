# Keywords are called as Reserved words
# All keywords can be in Lower case or Upper case
#Keywords are  a case senstive
# We cannot use Keyword as a Variable Name or function Name, or any other identifier


# Print() - This is not a keyword  (case senstive)

"""   Print() - This is not a keyword
                            ^^^^^^^
SyntaxError: invalid syntax"""


# Keywords - print(),False,None,assert,await, break

# we can import keyword and print(keyword.kwlist) -

import keyword
print(keyword.kwlist)

""" ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',"""


