## In this new file in your text editor, type the following:

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

## Notice that this code imports the abilities of goodbye from the sayings pacakage.
# If the user inputed at least two arguments at the command line, it will say "goodbye" along with the string inputed at the command line.

