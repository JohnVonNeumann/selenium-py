"""
LOGGING LEVELS
---------------
DEBUG
INFO
WARNING
ERROR
CRITICAL

These levels are ascending (descending here) in importance, also important to understand is that
only WARNING+ will actually be output via terminal/to users.

"""

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
# we set level as debug as it ensures ALL logging methods are recorded
logging.warning("This is a WARNING message.")
logging.info("This INFO message will not output.")
logging.error("This is an ERROR message.")
