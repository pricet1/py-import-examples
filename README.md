# Python imports

## Importing packages and modules

See Varshita Sher's article how to import packages and modules (and the
difference between the two): \
[Understanding Python imports, \_\_init\_\_.py and pythonpath &mdash; once and for all](https://medium.com/data-science/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355) (Oct 7, 2021)

## Creating a package from the utils directory

Turn the utils directory into a package by adding \_\_init\_\_.py in this directory.

Optionally add the following contents to it:

```
# [python]
from utils.lower import to_lower
from utils.upper import to_upper
from utils.length import get_length
```

## Using PYTHONPATH

`PYTHONPATH` is an environment variable that specifies additional directories
where Python should look for modules and packages when importing them. It allows
users to extend Python's search path beyond the default locations, making it
useful for custom libraries or project-specific dependencies.

The only reason to set `PYTHONPATH` is to maintain directories of custom
Python libraries that you do not want to install in the global default location
(i.e. the site-packages directory).

See \
[Importing your Local Package with PYTHONPATH](https://medium.com/@jameskabbes/importing-your-local-package-with-pythonpath-c459dc209c7)
(Sep 21, 2023) by James Kabbes \
and \
[What is PYTHONPATH environment variable in Python?](https://www.tutorialspoint.com/What-is-PYTHONPATH-environment-variable-in-Python) (Aug 26, 2023) by Rajendra Dharmkar

For example, to set the `PYTHONPATH` environment variable to include the `utils` directory

```
# [bash]
echo $PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$( pwd )/utils
echo $PYTHONPATH
```

To persist the above addition to PYTHONPATH, you could put the export statement
into a script and run it to initialise the project (or configure your system to
run it automatically on startup, e.g. in `.bashrc` or `.zshrc`).
