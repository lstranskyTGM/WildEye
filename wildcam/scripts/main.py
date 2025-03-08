from core.wildcam import WildCam


def main():
    """
    Main function to initialize and start the WildCam system in the foreground.
    Cleans up resources properly on keyboard exit.
    """
    wildcam = None
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
            wildcam.event_handler.set_events(False)
            wildcam.event_handler.camera_module.cleanup()
            print("Shutdown complete. Exiting.")


if __name__ == "__main__":
    main()
