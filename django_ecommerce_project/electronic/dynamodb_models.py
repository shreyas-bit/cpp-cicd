import boto3
from django.conf import settings
from datetime import datetime


# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name=settings.AWS_REGION)
table = dynamodb.Table('orders')

class DynamoOrder:
    def __init__(self, product_id, user=None, total_price=None, order_date=None):
        self.product_id = product_id
        self.user = user
        self.total_price = total_price
        self.order_date = order_date
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Update the region accordingly
        self.table = boto3.resource('dynamodb', region_name=settings.AWS_REGION).Table(settings.AWS_DYNAMODB_TABLE) # Make sure 'orders' is your DynamoDB table name

    def save(self):
        try:
            # Put item into DynamoDB
            response = table.put_item(
                Item={
                    'product_id': str(self.product_id),  # Convert product_id to string
                    'user': str(self.user),  # Ensure user is a string
                    'total_price': str(self.total_price),  # Convert to string
                    'order_date': str(self.order_date),  # Convert date to string
                }
            )
            print(f"Order saved to DynamoDB: {response}")
        except Exception as e:
            print(f"Error saving order to DynamoDB: {e}")

    def get_order(self):
        """
        Fetch the order details from DynamoDB using the product_id (partition key).
        """
        try:
            response = self.table.get_item(
                Key={'product_id': str(self.product_id)}  # Fetch using product_id as the partition key
            )
            return response.get('Item', None)  # If not found, return None
        except Exception as e:
            print(f"Error fetching order from DynamoDB: {e}")
            return None
    def get_order_from_dynamodb(self,order_id):
        try:
            response = table.get_item(
            Key={
                'product_id': str(order_id),  # Use product_id as the partition key
            }
          )
            return response.get('Item', None)  # Return the item or None if not found
        except Exception as e:
           print(f"Error fetching order from DynamoDB: {e}")
           return None
       