import functools
from abc import ABC, abstractmethod
from typing import Callable


def requires_initialization(method: Callable) -> Callable:
    """Decorator to ensure a module is initialized before calling a method."""
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
        
    Methods:
        initialize(): Performs all necessary hardware initialization.
        cleanup(): Releases resources and performs cleanup operations.
    """

    def __init__(self) -> None:
        """Initializes base attributes but does not initialize hardware."""
        self._initialized = False

    @abstractmethod
    def initialize(self) -> None:
        """Perform all necessary hardware initialization."""
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Perform cleanup operations when shutting down the module (e.g., release resources)."""
        pass
