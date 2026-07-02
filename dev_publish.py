import argparse
import re
import os
import requests
import json
import glob
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Replace with your DEV.to API key for publishing
DEV_TO_API_KEY = os.environ.get("DEV_TO_API_KEY", "YOUR_API_KEY_HERE")
DEV_TO_API_URL = "https://dev.to/api/articles"

# Authentication for internal image upload API
DEV_TO_COOKIE = os.environ.get("DEV_TO_COOKIE", "")
DEV_TO_CSRF_TOKEN = os.environ.get("DEV_TO_CSRF_TOKEN", "")

def upload_image_to_devto(local_image_path):
    """
    Uploads a local image using Dev.to's internal image upload endpoint.
    Requires DEV_TO_COOKIE and DEV_TO_CSRF_TOKEN from a browser session.
    """
    if not DEV_TO_COOKIE or not DEV_TO_CSRF_TOKEN:
        print(f"⚠️  Missing DEV_TO_COOKIE or DEV_TO_CSRF_TOKEN. Skipping upload for {local_image_path}")
        return f"file://{os.path.basename(local_image_path)}"
        
    upload_url = "https://dev.to/image_uploads"
    headers = {
        "x-csrf-token": DEV_TO_CSRF_TOKEN,
        "cookie": DEV_TO_COOKIE,
        "referer": "https://dev.to/new",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
    }
    
    print(f"Uploading image: {local_image_path}...")
    try:
        with open(local_image_path, 'rb') as f:
            # Forem usually expects the file under the 'image' or 'file' key
            # We'll use 'image' as it's common for their editor
            files = {'image': (os.path.basename(local_image_path), f, 'image/png')}
            response = requests.post(upload_url, headers=headers, files=files)
            
        if response.status_code == 200:
            # The response usually contains the URL to the uploaded image in Cloudinary or S3
            # Depending on Forem's exact response format, it might be plain text or JSON
            try:
                data = response.json()
                # Try common response keys
                image_url = data.get('url') or data.get('image_url')
                
                # Dev.to often returns an array of links
                if not image_url and data.get('links') and len(data.get('links')) > 0:
                    image_url = data.get('links')[0]
                    
                if image_url:
                    print(f"✅ Uploaded successfully: {image_url}")
                    return image_url
            except json.JSONDecodeError:
                # If it's plain text URL
                if response.text.startswith("http"):
                    print(f"✅ Uploaded successfully: {response.text}")
                    return response.text.strip()
            
            print(f"❓ Upload succeeded but couldn't parse URL. Response: {response.text}")
            return f"file://{os.path.basename(local_image_path)}"
            
        else:
            print(f"❌ Failed to upload image. Status: {response.status_code}")
            print(f"Response: {response.text}")
            return f"file://{os.path.basename(local_image_path)}"
    except Exception as e:
        print(f"❌ Exception uploading image: {e}")
        return f"file://{os.path.basename(local_image_path)}"

def process_markdown_and_images(content, base_dir):
    """
    Finds markdown image tags with local paths, uploads them to Dev.to, and replaces the path.
    Matches: ![alt text](local_path)
    """
    img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    
    def replace_image(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # If it's already a web URL, leave it alone
        if image_path.startswith("http://") or image_path.startswith("https://"):
            return match.group(0)
            
        # Resolve local path relative to the markdown file
        full_image_path = os.path.join(base_dir, image_path)
        
        if os.path.exists(full_image_path):
            public_url = upload_image_to_devto(full_image_path)
            return f"![{alt_text}]({public_url})"
        else:
            print(f"⚠️  Image not found locally: {full_image_path}")
            return match.group(0)
            
    return img_pattern.sub(replace_image, content)

def parse_and_publish(md_filepath):
    if not os.path.exists(md_filepath):
        print(f"Error: File '{md_filepath}' not found.")
        return

    with open(md_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print("Error: Markdown file is empty.")
        return

    # 1. Extract Title (First line)
    title = lines[0].strip().lstrip('#').strip()

    # 2. Extract Tags (Last line)
    last_line_index = len(lines) - 1
    while last_line_index > 0 and not lines[last_line_index].strip():
        last_line_index -= 1
        
    raw_tags = lines[last_line_index].strip()
    clean_tags = raw_tags.replace('*', '').strip()
    tags_list = [tag.strip() for tag in clean_tags.split('#') if tag.strip()]

    # 3. Extract Content
    content_lines = lines[1:last_line_index]
    raw_content = ''.join(content_lines).strip()
    
    # 4. Process Content Images
    base_dir = os.path.dirname(os.path.abspath(md_filepath))
    processed_content = process_markdown_and_images(raw_content, base_dir)

    # 5. Look for a banner image
    main_image_url = None
    banner_files = glob.glob(os.path.join(base_dir, "banner.*"))
    if banner_files:
        banner_path = banner_files[0]
        print(f"Found banner image: {banner_path}")
        main_image_url = upload_image_to_devto(banner_path)

    print(f"\n--- Parsed Info ---")
    print(f"Title: {title}")
    print(f"Tags: {tags_list}")
    if main_image_url and not main_image_url.startswith("file://"):
        print(f"Banner URL: {main_image_url}")
    print(f"Content Length: {len(processed_content)} characters")
    print("-------------------\n")

    # 6. Prepare Payload for Dev.to API
    payload = {
        "article": {
            "title": title,
            "body_markdown": processed_content,
            "published": False,
            "tags": tags_list
        }
    }
    
    if main_image_url and not main_image_url.startswith("file://"):
        payload["article"]["main_image"] = main_image_url

    headers = {
        "Content-Type": "application/json",
        "api-key": DEV_TO_API_KEY
    }

    # Uncomment to actually make the API request
    print("Publishing to Dev.to...")
    response = requests.post(DEV_TO_API_URL, json=payload, headers=headers)
    
    if response.status_code == 201:
        print("✅ Successfully published!")
        print("URL:", response.json().get("url"))
    else:
        print(f"❌ Failed to publish. Status: {response.status_code}")
        print("Response:", response.text)
    # print("API Request commented out for safety while setting up image uploads.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Publish Markdown to Dev.to")
    parser.add_argument("--md", required=True, help="Path to the markdown file")
    
    args = parser.parse_args()
    parse_and_publish(args.md)
