import os
import requests
import time
import analyze


with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

api_base = 'https://strapi.wildeye.tech'
pictures_endpoint = f'{api_base}/api/pictures'

def upload_analyzed_image(picture_document_id, image_id):
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer api_key'
}  
    
def get_latest_original():
    params = {
        'filters[analyzed][$null]': 'true',
        'fields[0]': 'documentId',
        'fields[1]': 'title',
        'populate[original][fields][0]': 'url',
        'sort': 'createdAt:desc',
        'pagination[limit]': 1
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(pictures_endpoint, params=params, headers=headers)
    if response.status_code != 200:
        print("Error fetching image data:", response.url)
    
    return response.json().get("data", [])

while True:
    
    data = get_latest_original()
    if data:
        print(data)
    else:
        time.sleep(30)
        break

    picture_info = data[0]
    picture_document_id = picture_info.get("documentId")

    # Extract the image URL from the response
    try:
        img_url = picture_info["original"]["url"]
    except KeyError:
        print("Image URL not found in response. Skipping...")
        time.sleep(30)
        continue

    # If the URL is relative, prepend the API base URL
    if not img_url.startswith("http"):
        img_url = f"{api_base}{img_url}"

    print("Fetching image from:", img_url)

    # Download the image
    img_response = requests.get(img_url)
    if img_response.status_code != 200:
        print("Failed to download image. Waiting 30 seconds...")
        time.sleep(1)
        continue

    # Save the downloaded image to a temporary file
    temp_img_path = f"/img/temp_{picture_document_id}.jpg"
    with open(temp_img_path, "wb") as f:
        f.write(img_response.content)

    # Run YOLO prediction on the downloaded image
    print(temp_img_path)

    analyze.analyze_latest_image(temp_img_path, "/labeled")
    # Clean up the temporary downloaded image file
    # os.remove(temp_img_path)

    # Optional short sleep before next iteration
    time.sleep(5)

 
