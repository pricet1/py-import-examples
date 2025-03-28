import sys

# Usage:
#   $ python show_sys_path_subdir.py

# The output from sys.path will always contain the current directory at index 0
# (i.e. the one where the script being run resides). This is the reason
# importing is fairly straightforward when both the caller and callee modules
# reside within the same directory.

print(sys.path)
