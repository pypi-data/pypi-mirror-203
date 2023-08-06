import pkg_resources
from .main import launcher

__version__: str = pkg_resources.get_distribution(__name__).version
