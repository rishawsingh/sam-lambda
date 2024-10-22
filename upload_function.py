import json
import boto3
import uuid

s3 = boto3.client('s3')
BUCKET_NAME = 'shaw3-sam3-test'

def handler(event, context):
    try:
        file_name = event['headers'].get('file-name', f"{str(uuid.uuid4())}.bin")
        file_content = base64.b64decode(event['body']) if event.get('isBase64Encoded', False) else event['body']

        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded', 'file_name': file_name})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'error': str(e)})
        }
