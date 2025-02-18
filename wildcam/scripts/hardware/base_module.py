import functools
from abc import ABC, abstractmethod


def requires_initialization(method):
    """
    Decorator to ensure a module is initialized before calling a method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self._initialized:
            raise RuntimeError(f"{self.__class__.__name__} is not initialized!")
        return method(self, *args, **kwargs)
    return wrapper


class BaseModule(ABC):
    """
    Abstract Base Class for all hardware modules.
    Ensures consistent initialization and cleanup behavior.
    
    Attributes:
        _initialized (bool): Flag indicating if the module is initialized.
    """

    def __init__(self):
        """
        Initializes base attributes but does not initialize hardware.
        """
        self._initialized = False

    @abstractmethod
    def initialize(self):
        """
        Perform all necessary hardware initialization.
        Must be called before using the module.
        """
        pass

    @abstractmethod
    def read_data(self):
        """
        Retrieve data from the hardware module.
        
        Returns:
            Any: Data retrieved from the module (e.g., sensor readings).
        
        Raises:
            RuntimeError: If the module is not initialized.
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
        Perform cleanup operations when shutting down the module (e.g., release resources).
        """
        pass
