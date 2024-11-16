import boto3
import time
import logging

# Initialize CloudWatch Logs client
logs_client = boto3.client('logs', region_name='us-east-1')
cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-1')  # Your AWS region
# CloudWatch log group and stream
LOG_GROUP = 'product_wishlist'
LOG_STREAM = 'wishlist-log-stream'
NAMESPACE = 'DjangoAppMetrics'

# Create CloudWatch log group if it doesn't exist
def create_log_group():
    try:
        # Check if the log group exists
        response = logs_client.describe_log_groups(logGroupNamePrefix=LOG_GROUP)
        if not response['logGroups']:
            # If it doesn't exist, create it
            logs_client.create_log_group(logGroupName=LOG_GROUP)
            print(f"Log group '{LOG_GROUP}' created successfully!")
        else:
            print(f"Log group '{LOG_GROUP}' already exists.")
    except Exception as e:
        print(f"Error creating log group: {e}")

# Create CloudWatch log stream if it doesn't exist
def create_log_stream():
    try:
        # Ensure the log group exists
        create_log_group()

        # Create the log stream
        logs_client.create_log_stream(
            logGroupName=LOG_GROUP,
            logStreamName=LOG_STREAM
        )
        print(f"Log stream '{LOG_STREAM}' created successfully!")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        print(f"Log stream '{LOG_STREAM}' already exists.")
    except Exception as e:
        print(f"Error creating log stream: {e}")

class CloudWatchLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        timestamp = int(time.time() * 1000)  # Timestamp in milliseconds
        
        # Send logs to CloudWatch
        logs_client.put_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=LOG_STREAM,
            logEvents=[{
                'timestamp': timestamp,
                'message': log_entry
            }]
        )
        
def publish_metric_to_cloudwatch(metric_name, value, dimensions=None):
    try:
        response = cloudwatch_client.put_metric_data(
            Namespace='DjangoAppMetrics',  # Custom namespace for your app
            MetricData=[
                {
                    'MetricName': metric_name,  # The metric name (ProductAdded)
                    'Dimensions': dimensions if dimensions else [],
                    'Value': value,  # Metric value (1 for each product added)
                    'Unit': 'Count',  # Unit for counting (products added)
                    'StorageResolution': 60,  # 1-minute resolution
                },
            ]
        )
        print(f"Successfully sent metric {metric_name} to CloudWatch")
    except Exception as e:
        print(f"Error sending metric to CloudWatch: {e}")

# Function to track wishlist additions (publishing metric)

# Example usage of publishing a custom metric
def log_wishlist_addition(product_name):
    # You can modify this function to use dynamic data
    dimensions = [{'Name': 'Product', 'Value': product_name}]
    publish_metric_to_cloudwatch('ProductAdded', 1, dimensions)