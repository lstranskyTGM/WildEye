import requests
import json
import mimetypes
from dotenv import load_dotenv
import os
from datetime import datetime, timezone

# Load API key from .env file
load_dotenv()
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# Base URLs for Strapi API
BASE_URL = "https://strapi.wildeye.tech/api"
UPLOAD_URL = f"{BASE_URL}/upload"
PICTURES_URL = f"{BASE_URL}/pictures"

# Path to the image file
IMAGE_PATH = "test_image.png"


# Generate the current timestamp in ISO 8601 format
def get_current_timestamp():
    return datetime.now(timezone.utc).isoformat()  # ISO 8601 with UTC timezone


# Upload Image to Strapi
def upload_image(image_path):
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "accept": "application/json"
    }

    # Automatically detect the correct MIME type (e.g., image/png or image/jpeg)
    mime_type = mimetypes.guess_type(image_path)[0] or "application/octet-stream"
    files = {
        "files": (image_path, open(image_path, "rb"), mime_type)
    }

    data = {
        "path": "",
        "refId": "",
        "ref": "",
        "field": ""
    }

    try:
        response = requests.post(UPLOAD_URL, headers=headers, files=files, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

        # Check if the status code is in the 2xx range
        if 200 <= response.status_code < 300:
            print("Image uploaded successfully.")
            image_data = response.json()
            print(json.dumps(image_data, indent=2))
            return image_data[0]["id"]  # Extract uploaded image ID
        else:
            print(f"Unexpected response status: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during image upload: {e}")
        return None


# Create a Picture Object and Attach the Uploaded Image
def create_picture_object(image_id):
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "data": {
            "original": image_id,
            "wild_camera": "camera_id",
            "title": "new image",
            "capturedAt": get_current_timestamp(),  # Use dynamically generated timestamp
            "lat": 0.0,
            "lng": 0.0,
            "locale": "string"
        }
    }

    try:
        response = requests.post(PICTURES_URL, headers=headers, json=payload)
        response.raise_for_status()

        # Check if the status code is in the 2xx range
        if 200 <= response.status_code < 300:
            print("Image object created successfully.")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Unexpected response status: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error during picture object creation: {e}")


# Run the Test
if __name__ == "__main__":
    if not AUTH_TOKEN:
        print("Error: AUTH_TOKEN is not set in the .env file.")
    else:
        image_id = upload_image(IMAGE_PATH)
        if image_id:
            create_picture_object(image_id)
            print("Test completed.")
        else:
            print("Image upload failed.")
