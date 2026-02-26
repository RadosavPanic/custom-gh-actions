import os
import mimetypes
from google.cloud import storage

def run():
    bucket_name = os.environ["INPUT_GCP_BUCKET_NAME"].strip()
    dist_folder = os.environ["INPUT_DIST_FOLDER"].strip()
    
    client = storage.Client()
    
    bucket = client.bucket(bucket_name)
    
    for root, subdirs, files in os.walk(dist_folder):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, dist_folder)
            
            blob = bucket.blob(relative_path)
            
            content_type = mimetypes.guess_type(file)[0] or "application/octet-stream"
            
            blob.upload_from_filename(local_path, content_type=content_type)
            
            print(f"Uploaded {relative_path}")
            
    website_url = f"https://storage.googleapis.com/{bucket_name}/index.html"
    
    with open(os.environ["GITHUB_OUTPUT"], "a") as output:
        print(f"website-url={website_url}", file=output)
        
if __name__ == "__main__":
    run()
    