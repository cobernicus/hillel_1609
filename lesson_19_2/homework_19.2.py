import requests

# URL for uploading the image
upload_url = 'http://127.0.0.1:8080/upload'

# Path to the image you want to upload
image_path = '/home/admin/PycharmProjects/Hillel/pythonProject1/hillel_1609/lesson_19_2/images/sample.jpg'

try:
    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        # Define the files parameter for the POST request
        files = {'image': image_file}

        # Make the POST request to upload the image
        response = requests.post(upload_url, files=files)

    # Check if the upload was successful
    if response.status_code == 201:
        # Parse the JSON response to get the image URL
        data = response.json()
        image_url = data['image_url']
        print(f"Image successfully uploaded. URL: {image_url}")
        filename = image_url.split('/')[-1]  # Extract the filename from the URL
    else:
        print(f"Failed to upload image. Status code: {response.status_code}")
        filename = None

    if filename:
        # URL for getting the uploaded image URL
        get_image_url = f'http://127.0.0.1:8080/image/{filename}'

        # Make the GET request to retrieve the image URL
        response = requests.get(get_image_url, headers={'Content-Type': 'text'})

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response to get the image URL
            data = response.json()
            image_url = data.get('image_url', 'No image_url key found in the response')
            print(f"Image URL: {image_url}")
        else:
            print(f"Failed to retrieve image URL. Status code: {response.status_code}")

        # URL for deleting the uploaded image
        delete_url = f'http://127.0.0.1:8080/delete/{filename}'

        # Make the DELETE request to delete the image
        response = requests.delete(delete_url)

        # Check if the deletion was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            delete_message = data.get('image_url', 'No image_url key found in the response')
            print(f"Image successfully deleted. URL: {delete_message}")
        else:
            print(f"Failed to delete image. Status code: {response.status_code}")

except FileNotFoundError as e:
    print(f"Error: {e}")
