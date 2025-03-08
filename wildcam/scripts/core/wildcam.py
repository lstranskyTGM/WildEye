import signal
from core.event_handler import EventHandler


class WildCam:
    """
    Orchestrates all components of the WildCam system.

    Attributes:
        event_handler (EventHandler): Handles all system events.
        
    Methods:
        start_main_loop(): Starts the main event loop of the WildCam system.
        cleanup(): Cleans up resources before exiting the WildCam system.
    """

    def __init__(self) -> None:
        """Initializes the WildCam system and sets up the event handler."""
        self.event_handler = EventHandler()
        self.event_handler.set_events(True)

    def start_main_loop(self) -> None:
        """Starts the main event loop of the WildCam system and waits for interrupts."""
        print("WildCam system started.")
        signal.pause()  # Keeps script running to maintain active interrupts

    def cleanup(self) -> None:
        """Cleans up resources before exiting the WildCam system."""
        self.event_handler.set_events(False)
        print("WildCam system stopped.")
