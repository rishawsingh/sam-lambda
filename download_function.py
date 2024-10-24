import json
import boto3
import base64

s3 = boto3.client('s3')
BUCKET_NAME = 'shaw3-sam4-test'

def handler(event, context):
    try:
        file_name = event['queryStringParameters']['filename']
        file_obj = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
        file_content = file_obj['Body'].read()
        content_type = file_obj['ContentType']

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': content_type,
                'Content-Disposition': f'attachment; filename="{file_name}"'
            },
            'body': file_content,
            'isBase64Encoded': False
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error', 'error': str(e)})
        }
