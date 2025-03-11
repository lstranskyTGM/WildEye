import signal
import threading
from core.event_handler import EventHandler


class WildCam:
    """
    Orchestrates all components of the WildCam system.

    Attributes:
        event_handler (EventHandler): Handles all system events.
        update_interval (int): Interval in seconds between update cycles.
        update_timer (threading.Timer): Timer for scheduling update cycles.
        
    Methods:
        start_main_loop(): Starts the main event loop of the WildCam system.
        cleanup(): Cleans up resources before exiting the WildCam system.
        start_update_timer(): Starts a timer to trigger update cycles at regular intervals.
    """

    def __init__(self) -> None:
        """Initializes the WildCam system and sets up the event handler."""
        self.event_handler = EventHandler()
        self.event_handler.set_events(True)
        self.update_interval = 60  # Temporary fixed value
        self.update_timer = None

    def start_main_loop(self) -> None:
        """Starts the main event loop of the WildCam system and waits for interrupts."""
        print("WildCam system started.")
        
        # Start the update timer
        self.start_update_timer()
        
        signal.pause()  # Keeps script running to maintain active interrupts
        
    def start_update_timer(self) -> None:
        """Starts a timer to trigger update cycles at regular intervals."""
        # Cancel any existing timer
        if self.update_timer:
            self.update_timer.cancel()
            
        # Create and start a new timer
        self.update_timer = threading.Timer(
            self.update_interval, 
            self._run_update_cycle
        )
        self.update_timer.daemon = True  # Allow the timer to be terminated when the program exits
        self.update_timer.start()
        
    def _run_update_cycle(self) -> None:
        """Run the update cycle and schedule the next one."""
        try:
            self.event_handler.handle_update_cycle()
        except Exception as e:
            print(f"Error during update cycle: {e}")
        finally:
            # Schedule the next update cycle
            self.start_update_timer()

    def cleanup(self) -> None:
        """Cleans up resources before exiting the WildCam system."""
        # Cancel the update timer if it's running
        if self.update_timer:
            self.update_timer.cancel()
            
        # Stop all event interrupts
        self.event_handler.set_events(False)
        print("WildCam system stopped.")
