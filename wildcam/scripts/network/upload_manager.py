import os
import shutil
from network.strapi_service import StrapiService


class UploadManager:
    """
    Manages the uploading of files to the Strapi server from the local upload queue.
    
    Attributes:
        upload_folder (str): Path to the local upload queue folder.
        archive_folder (str): Path to the archive folder for successful uploads.
        failed_folder (str): Path to the folder for failed uploads.
        strapi_service (StrapiService): Service for interacting with the Strapi API.
        camera_id (str): The ID of the camera associated with the uploads.
        
    Methods:
        upload_files(): Upload all files from the upload queue to the server.
        retry_failed_uploads(): Retry uploading files that previously failed.
    """

    def __init__(self, strapi_service: StrapiService, camera_id: str) -> None:
        """
        Initialize the UploadManager with the required folders and Strapi service.
        
        Args:
            strapi_service (StrapiService): Service for interacting with the Strapi API.
            camera_id (str): The ID of the camera associated with the uploads.
        """
        # Hardcoded paths for now (will be moved to configuration later)
        self.upload_folder = "media/upload_queue/images"
        self.archive_folder = "media/archive/images"
        self.failed_folder = "media/failed_uploads/images"
        
        self.camera_id = camera_id
        self.strapi_service = strapi_service

        # Ensure required directories exist
        os.makedirs(self.upload_folder, exist_ok=True)
        os.makedirs(self.archive_folder, exist_ok=True)
        os.makedirs(self.failed_folder, exist_ok=True)

    def upload_files(self) -> bool:
        """
        Upload all files from the upload queue to the server.
        
        Returns:
            bool: True if all files were uploaded successfully, False otherwise.
        """
        files = [f for f in os.listdir(self.upload_folder) if os.path.isfile(os.path.join(self.upload_folder, f))]
        
        if not files:
            print("No files found in upload queue.")
            return True
        
        success_count = 0
        total_count = len(files)

        for file in files:
            file_path = os.path.join(self.upload_folder, file)
            print(f"Uploading: {file_path}")

            # Upload the file to the server
            upload_response = self.strapi_service.upload_file(file_path)

            if upload_response:
                print(f"Upload successful: {file}")
                
                # If response is a list, get the first item
                if isinstance(upload_response, list) and len(upload_response) > 0:
                    upload_response = upload_response[0]
                
                # Create an image object in Strapis
                image_id = upload_response.get("id")
                if image_id:
                    image_object = self.strapi_service.create_image_object(
                        image_id=image_id,
                        camera_id=self.camera_id
                    )
                    
                    if image_object:
                        print(f"Created image object for {file}")
                        success_count += 1
                        # Move file to archive
                        shutil.move(file_path, os.path.join(self.archive_folder, file))
                    else:
                        print(f"Failed to create image object for {file}")
                        shutil.move(file_path, os.path.join(self.failed_folder, file))
                else:
                    print(f"Failed to get image ID from upload response")
                    shutil.move(file_path, os.path.join(self.failed_folder, file))
            else:
                print(f"Upload failed: {file}")
                shutil.move(file_path, os.path.join(self.failed_folder, file))
        
        print(f"Upload summary: {success_count}/{total_count} files successfully processed")
        return success_count == total_count

    def retry_failed_uploads(self) -> bool:
        """Retry uploading files that initially failed to upload."""
        pass
