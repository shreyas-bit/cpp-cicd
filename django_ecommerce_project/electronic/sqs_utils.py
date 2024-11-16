# sqs_utils.py
import boto3
from django.conf import settings

# Create an SQS client using boto3
sqs = boto3.client('sqs', region_name=settings.AWS_REGION)

def send_message_to_sqs(message_body):
    """
    Sends a message to the SQS queue
    """
    try:
        response = sqs.send_message(
            QueueUrl=settings.AWS_SQS_QUEUE_URL,
            MessageBody=message_body,
        )
        print(f"Message sent to SQS: {response['MessageId']}")
        return response
    except Exception as e:
        print(f"Error sending message to SQS: {str(e)}")
        return None
