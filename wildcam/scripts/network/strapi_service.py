import os
import mimetypes
from datetime import datetime, timezone
from network.api_client import ApiClient


class StrapiService:
    """
    Provides high-level methods for interacting with the Strapi API.
    
    Attributes:
        api_client (ApiClient): API client for server communication.
        
    Methods:
        upload_file(file_path): Upload a file to the Strapi upload endpoint.
        create_image_object(image_id, camera_id, lat=None, lng=None): Create a new image object in Strapi.
        update_wildcam_object(): Update an existing Wildcam object in Strapi.
        update_settings(): Update the configuration settings in Strapi.
        get_settings(): Retrieve the configuration settings from Strapi.
        _get_current_timestamp(): Generate the current timestamp in ISO 8601 format.
    """
    
    def __init__(self, base_url: str, auth_token: str = None) -> None:
        """
        Initialize the StrapiService with a base URL and optional authentication token.
        
        Args:
            base_url (str): The base URL of the remote server API.
            auth_token (str, optional): Authentication token for secure API access.
        """
        self.api_client = ApiClient(base_url, auth_token)
    
    def upload_file(self, file_path: str) -> dict | None:
        """
        Upload a file to the Strapi upload endpoint.
        
        Args:
            file_path (str): Path to the file to upload.
            
        Returns:
            dict | None: Response data from the server as a dictionary, or None on failure.
        """
        try:
            # Automatically detect the correct MIME type
            mime_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
            
            # Prepare the file data and form data
            with open(file_path, "rb") as file:
                files = {
                    "files": (os.path.basename(file_path), file, mime_type)
                }
                
                data = {
                    "path": "",
                    "refId": "",
                    "ref": "",
                    "field": ""
                }
                
                # Use the API client to upload the file
                response = self.api_client.upload_file("upload", data, files)
                  
                return response
        except Exception as e:
            print(f"Error during file upload: {e}")
            return None
    
    def create_image_object(self, image_id: str, camera_id: str, lat: float = None, lng: float = None) -> dict | None:
        """
        Create a new image object in Strapi and link it to an Image and Camera.
        
        Args:
            image_id (str): The unique identifier for the image.
            camera_id (str): The unique identifier for the camera.
            lat (float, optional): The latitude coordinate for the image.
            lng (float, optional): The longitude coordinate for the image.
            
        Returns:
            dict | None: Response data from the server as a dictionary, or None on failure.
        """
        try:
            # Prepare the payload for creating the image object
            payload = {
                "data": {
                    "original": image_id,
                    "wild_camera": camera_id,
                    "title": "New Image",
                    "capturedAt": self._get_current_timestamp(),
                    "lat": lat or 0.0,
                    "lng": lng or 0.0,
                    "locale": "string"
                }
            }
            
            # Use the API client to create the image object
            return self.api_client.post("pictures", payload)
        except Exception as e:
            print(f"Error creating image object: {e}")
            return None
    
    # TODO: Implement the following methods
    def update_wildcam_object(self):
        """Update an existing Wildcam object in Strapi."""
        pass
    
    def update_settings(self):
        """Update the configuration settings in Strapi."""
        pass
    
    def get_settings(self):
        """Retrieve the configuration settings from Strapi."""
        pass

    @staticmethod
    def _get_current_timestamp() -> str:
        """
        Generate the current timestamp in ISO 8601 format with UTC timezone.
        
        Returns:
            str: Current timestamp in ISO 8601 format.
        """
        return datetime.now(timezone.utc).isoformat()
