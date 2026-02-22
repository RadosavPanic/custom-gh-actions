import os
import boto3
import mimetypes
from botocore.config import Config


def run():
    s3_bucket_name = os.environ['INPUT_S3_BUCKET_NAME'].strip()
    s3_region = os.environ['INPUT_S3_REGION'].strip()
    dist_folder = os.environ['INPUT_DIST_FOLDER'].strip()

    configuration = Config(region_name=s3_region)

    s3_client = boto3.client('s3', config=configuration)

    for root, subdirs, files in os.walk(dist_folder):
        for file in files:
            content_type = mimetypes.guess_type(file)[0] or "application/octet-stream"
            s3_client.upload_file(
                os.path.join(root, file),
                s3_bucket_name,
                os.path.join(root, file).replace(dist_folder + '/', ''),
                ExtraArgs={"ContentType": content_type}
            )

    website_url = f'http://{s3_bucket_name}.s3-website.{s3_region}.amazonaws.com'
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'website-url={website_url}', file=gh_output)


if __name__ == '__main__':
    run()
