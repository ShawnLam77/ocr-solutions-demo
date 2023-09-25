import boto3
from trp import Document

# S3 Bucket Data
s3BucketName = ""
TabledocumentName = "Image.jpeg"

# Amazon Textract client
textractmodule = boto3.client('textract')

# TABLE data detection from documents:
response = textractmodule.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': TabledocumentName
        }
    },
    FeatureTypes=["TABLES"])
doc = Document(response)
print ('------------- Print Table detected text ------------------------------')
for page in doc.pages:
    for table in page.tables:
        for r, row in enumerate(table.rows):
            itemName  = ""
            for c, cell in enumerate(row.cells):
                print("Table[{}][{}] = {}".format(r, c, cell.text))
