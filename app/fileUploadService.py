import boto3, botocore
from config import AWS_BUCKET_NAME, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_DOMAIN

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_files_to_s3(file, acl="public-read"):
    filename = file.filename
    try:
        s3.upload_fileobj(
            file,
            AWS_BUCKET_NAME,
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        print("Algo aconteceu: ", e)
        return e

    filename_retorno = filename.replace(" ", "+")
    return f"https://carros-projeto.s3.amazonaws.com/{filename_retorno}"