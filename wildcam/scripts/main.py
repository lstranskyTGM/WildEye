from core.wildcam import WildCam


def main():
    """
    Main function to initialize and start the WildCam system in the foreground.
    Cleans up resources properly on keyboard exit.
    """
    try:
        wildcam = WildCam()
        print("Press CTRL+C to stop WildCam.")
        wildcam.start_main_loop()
    except KeyboardInterrupt:
        print("\nCTRL+C detected. Stopping WildCam safely...")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if wildcam:
            print("Cleaning up resources before exiting...")
            wildcam.event_handler.set_interrupts(False)
            wildcam.event_handler.camera.cleanup()
            print("Shutdown complete. Exiting.")


if __name__ == "__main__":
    main()
