# Option 4: Use PYTHONPATH

import length as ln

# Usage:
#   # Add the utils directory to the PYTHONPATH environment variable:
#   $ export PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}$( pwd )/utils
#   # Check the PYTHONPATH:
#   $ echo $PYTHONPATH
#   # (you could add the export statement to your .bashrc or .zshrc to persist it)

#  $ python option_4.py

txt = "Hello yet again"
res_len = ln.get_length(txt)
print(f"The length of the string is: {res_len}")
