# read version from installed package
from importlib.metadata import version
__version__ = version("statgis")

from . import gee
from . import statutils
