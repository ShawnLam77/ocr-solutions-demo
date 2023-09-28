import boto3
from trp import Document

# S3 Bucket Data
s3BucketName = ""
PlaindocumentName = ""

# Amazon Textract client
textractmodule = boto3.client('textract')

# PLAINTEXT detection from documents:
response = textractmodule.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': PlaindocumentName
        }
    })
print ('------------- Print Plaintext detected text ------------------------------')
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print (item["Text"])
