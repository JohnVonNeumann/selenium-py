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

logging.basicConfig(format = '%(asctime)s:%(levelname)s: %(message)s', level=logging.DEBUG, filename="test.log")
logging.warning("This is a WARNING message.")
logging.info("This INFO message will not output.")
logging.error("This is an ERROR message.")
