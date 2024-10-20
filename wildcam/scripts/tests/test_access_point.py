import subprocess


def start_access_point():
    """Start the access point using Network Manager."""
    try:
        # Start the access point using the 'accesspoint' connection profile
        subprocess.run(["sudo", "nmcli", "connection", "up", "accesspoint"], check=True)
        print("Access Point started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start the Access Point: {e}")#
        print(e.stderr)

def stop_access_point():
    """Stop the access point using Network Manager."""
    try:
        # Stop the access point using the 'accesspoint' connection profile
        subprocess.run(["sudo", "nmcli", "connection", "down", "accesspoint"], check=True)
        print("Access Point stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop the Access Point: {e}")
        print(e.stderr)

def check_access_point_status():
    """Check the status of the access point."""
    try:
        result = subprocess.run(
            ["nmcli", "connection", "show", "--active"],
            check=True, capture_output=True, text=True
        )
        if "accesspoint" in result.stdout:
            status = "Active"
        else:
            status = "Inactive"
        print(f"Access Point status: {status}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to check the status of the Access Point: {e}")
        print(e.stderr)


if __name__ == "__main__":
    # To start the access point
    print("Starting Access Point...")
    start_access_point()

    # To check the status of the access point
    print("Checking Access Point status...")
    check_access_point_status()

    # To stop the access point
    # print("Stopping Access Point...")
    # stop_access_point()
