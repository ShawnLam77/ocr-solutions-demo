import boto3
from trp import Document

# S3 Bucket Data
s3BucketName = ""
FormdocumentName = ""

# Amazon Textract client
textractmodule = boto3.client('textract')

# FORM detection from documents:
response = textractmodule.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': FormdocumentName
        }
    },
    FeatureTypes=["FORMS"])
doc = Document(response)
print ('------------- Print Form detected text ------------------------------')
for page in doc.pages:
    for field in page.form.fields:
        print("Key: {}, Value: {}".format(field.key, field.value))
