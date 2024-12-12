import os
import boto3
import mimetypes
from botocore.config import Config


def run():
    bucket = os.environ['INPUT_BUCKET']
    bucket_region = os.environ['INPUT_REGION']
    dist_folder = os.environ['INPUT_DIST_FOLDER']

    configuration = Config(region_name=bucket_region)
    s3_client = boto3.client('s3', config=configuration)

    for root, subdirs, files in os.walk(dist_folder):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, dist_folder)

            s3_client.upload_file(
                file_path,
                bucket,
                s3_key,
                ExtraArgs={"ContentType": mimetypes.guess_type(file)[0]}
            )

    url = f'http://{bucket}.s3-website-{bucket_region}.amazonaws.com'

    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'url={url}', file=gh_output)


if __name__ == '__main__':
    run()
