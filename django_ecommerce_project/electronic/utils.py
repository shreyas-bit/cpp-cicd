import boto3
from django.conf import settings
from botocore.exceptions import ClientError

# Initialize SNS client
sns_client = boto3.client('sns', region_name=settings.AWS_REGION_NAME)

def send_cart_notification(user_email, product_name):
    """Send SNS notification when a product is added to the cart."""
    try:
        message = f"{product_name} has been added to your cart!"
        subject = "Product Added to Cart"
        
        # Publish to the SNS Topic
        response = sns_client.publish(
            TopicArn=settings.SNS_TOPIC_ARN,
            Message=message,
            Subject=subject,
        )
        print("Notification sent successfully!")
        return response
    except ClientError as e:
        print(f"Error sending notification: {e}")
        return None

