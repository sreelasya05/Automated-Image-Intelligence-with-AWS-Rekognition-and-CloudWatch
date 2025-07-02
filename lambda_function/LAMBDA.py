import json
import boto3

rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        image_key = record['s3']['object']['key']
        
        # Call Rekognition to detect labels
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': image_key}},
            MaxLabels=10,
            MinConfidence=75
        )
        
        # Process and log the labels
        labels = [label['Name'] for label in response['Labels']]
        print(f"Image: {image_key}, Labels: {labels}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processed all records successfully.')
    }
