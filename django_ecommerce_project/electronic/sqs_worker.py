# sqs_worker.py
import boto3
import time
from django.conf import settings

# Set up the SQS client
sqs = boto3.client('sqs', region_name=settings.AWS_REGION)

def process_sqs_messages():
    """
    Polls the SQS queue and processes messages.
    This should be run in a separate process or thread.
    """
    while True:
        # Receive messages from the queue
        response = sqs.receive_message(
            QueueUrl=settings.AWS_SQS_QUEUE_URL,
            AttributeNames=['All'],
            MaxNumberOfMessages=10,  # Number of messages to fetch at once
            WaitTimeSeconds=20  # Long polling to reduce costs
        )

        if 'Messages' in response:
            for message in response['Messages']:
                # Process each message
                print(f"Processing message: {message['Body']}")
                
                # You can perform tasks like sending notifications, updating databases, etc.

                # After processing, delete the message from the queue
                sqs.delete_message(
                    QueueUrl=settings.AWS_SQS_QUEUE_URL,
                    ReceiptHandle=message['ReceiptHandle']
                )
                print(f"Message {message['MessageId']} deleted from queue.")
        else:
            print("No messages in the queue. Sleeping for 20 seconds...")
            time.sleep(20)
