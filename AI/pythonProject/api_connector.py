import os
import requests
import time
import analyze

# change according to project structure
path_for_images = "img/"
path_for_analyzed_images = "labeled/"

# loop counter
counter = 0

with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

api_base = 'https://strapi.wildeye.tech'
pictures_endpoint = f'{api_base}/api/pictures'

def upload_analysis(picture_document_id, tags, title, image_id):
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }  
    body = {
        "data": {
            "analyzed": image_id,
            "tags": tags,
            "title": title
        }
    }
    print(f"{pictures_endpoint}/{picture_document_id}\n{body}\n{headers}")
    response = requests.put(f"{pictures_endpoint}/{picture_document_id}", json=body, headers=headers)
    print(response.status_code, response.text)

def upload_image(path):
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }  
    upload_url = f"{api_base}/api/upload"
    
    try:
        with open(path, "rb") as image_file:
            filename = os.path.basename(path)
            files = {
                # 'files' is the field name Strapi expects by default
                'files': (filename, image_file, 'image/jpeg')
            }
            response = requests.post(upload_url, files=files, headers=headers)
            response.raise_for_status()
            print("Image uploaded successfully:", response.json())
            return response.json()
    except Exception as e:
        print("Error uploading image:", e)
        return None

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
        print("No new images")
        time.sleep(30)
        continue

    picture_info = data[0]
    picture_document_id = picture_info.get("documentId")
    picture_title = picture_info["title"]

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
    temp_img_path = f"{path_for_images}temp_{picture_document_id}.jpg"
    with open(temp_img_path, "wb") as f:
        f.write(img_response.content)

    # Run YOLO prediction on the downloaded image
    #print(temp_img_path)

    analysis = analyze.analyze_latest_image(path_for_images, path_for_analyzed_images)
    os.remove(temp_img_path)

    #print(analysis)
    response = upload_image(f"{path_for_analyzed_images}{analysis["filename"]}")
    uploaded_image_id = response[0]['id']

    if picture_title == "new image" and analysis["title"]:
        picture_title = analysis["title"]
    upload_analysis(picture_document_id,analysis["tags"],picture_title,uploaded_image_id)
    counter += 1
    print(f"picture #{counter} done!")

 
