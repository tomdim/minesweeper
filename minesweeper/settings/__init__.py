import os
import sys

if os.environ.get('PRODUCTION', '') == 'ON':
    from .production import *
elif sys.argv and 'test' in sys.argv:
    from .testing import *
else:
    from .development import *
