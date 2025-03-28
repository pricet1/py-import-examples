# Option 3: Use os and sys packages to modify sys.path

import os
import sys

# Usage:
#   $ python option_3.py

# os.path.dirname(__file__) returns the absolute path to the current working
# directory
fpath = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.append(fpath)
# print(sys.path)

# This import statement will now work (must be after sys.path.append)
import length

txt = "Hello for the third time"
res_len = length.get_length(txt)
print(f"The length of the string is: {res_len}")
