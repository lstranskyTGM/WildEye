import requests


class ApiClient:
    """
    Provides an interface for interacting with a remote API server using HTTP requests.
    
    Attributes:
        base_url (str): The base URL of the remote server API.
        default_headers (dict): HTTP headers to include in each request.
        
    Methods:
        get(endpoint): Perform a GET request to the specified API endpoint.
        post(endpoint, data): Perform a POST request to the specified API endpoint with provided data.
        upload_file(endpoint, data, files): Perform a multipart/form-data POST request for file uploads.
    """

    def __init__(self, base_url: str, auth_token: str = None) -> None:
        """
        Initialize the API client with a base URL and optional authentication token.

        Args:
            base_url (str): The base URL of the remote server API.
            auth_token (str, optional): Authentication token for secure API access.
        """
        self.base_url = base_url.rstrip('/')
        self.default_headers = {
            "Authorization": f"Bearer {auth_token}" if auth_token else "",
            "accept": "application/json",
        }

    def get(self, endpoint: str, headers: dict = None) -> dict | None:
        """
        Perform a GET request to the specified API endpoint.

        Args:
            endpoint (str): API endpoint to send the GET request to.
            headers (dict, optional): Additional HTTP headers to include in the request

        Returns:
            dict | None: Response data from the server as a dictionary, or None on failure.
        """
        try:
            request_headers = headers or self.default_headers
            response = requests.get(f"{self.base_url}/{endpoint.lstrip('/')}", headers=request_headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during GET request: {e}")
            return None

    def post(self, endpoint: str, data: dict, headers: dict = None) -> dict | None:
        """
        Perform a POST request to the specified API endpoint with provided data.

        Args:
            endpoint (str): API endpoint to send the POST request to.
            data (dict): Data payload to include in the POST request.
            headers (dict, optional): Additional HTTP headers to include in the request.

        Returns:
            dict | None: Response data from the server as a dictionary, or None on failure.
        """
        try:
            request_headers = headers or self.default_headers
            response = requests.post(f"{self.base_url}/{endpoint.lstrip('/')}", json=data, headers=request_headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during POST request: {e}")
            return None

    def upload_file(self, endpoint: str, data: dict, files: dict, headers: dict = None) -> dict | None:
        """
        Perform a multipart/form-data POST request to upload files to the specified API endpoint.

        Args:
            endpoint (str): API endpoint to send the multipart request to.
            data (dict): Form data to include in the POST request.
            files (dict): Dictionary of files to upload in the format {field_name: (filename, file_object, mime_type)}.
            headers (dict, optional): Additional HTTP headers to include in the request.

        Returns:
            dict | None: Response data from the server as a dictionary, or None on failure.
        """
        try:
            request_headers = headers or self.default_headers
            response = requests.post(
                f"{self.base_url}/{endpoint.lstrip('/')}", 
                data=data, 
                files=files, 
                headers=request_headers, 
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during file upload: {e}")
            return None
