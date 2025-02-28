import functools
from abc import ABC, abstractmethod
from typing import Callable


def requires_hardware_setup(method: Callable) -> Callable:
    """Decorator to ensure a module's hardware is set up before calling a method."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self._hardware_configured:
            raise RuntimeError(f"{self.__class__.__name__} is not set up! Call hardware_setup() first.")
        return method(self, *args, **kwargs)
    return wrapper


class BaseModule(ABC):
    """
    Abstract Base Class for all hardware modules.
    Ensures consistent setup and cleanup procedures for all modules.
    
    Attributes:
        _hardware_configured (bool): Flag indicating whether hardware is set up.
        
    Methods:
        hardware_setup(): Performs all necessary hardware configurations.
        cleanup(): Releases resources and performs cleanup operations.
    """

    def __init__(self) -> None:
        """Initializes base attributes but does not configure hardware."""
        self._hardware_configured = False

    @abstractmethod
    def hardware_setup(self) -> None:
        """Perform all necessary hardware configurations."""
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Perform cleanup operations when shutting down the module (e.g., release resources)."""
        pass
