{"filter":false,"title":"cloudwatch_utils.py","tooltip":"/django_ecommerce_project/electronic/cloudwatch_utils.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":0,"column":0},"end":{"row":61,"column":0},"action":"insert","lines":["import boto3","import time","import logging","from django.conf import settings","","# Initialize CloudWatch and CloudWatch Logs clients","cloudwatch = boto3.client('cloudwatch', region_name=settings.AWS_REGION_NAME)","logs_client = boto3.client('logs', region_name=settings.AWS_REGION_NAME)","","# CloudWatch log group and stream","LOG_GROUP = 'django-logs'","LOG_STREAM = 'wishlist-log-stream'","","# Create a CloudWatch log stream if it doesn't exist","def create_log_stream():","    try:","        logs_client.create_log_stream(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM","        )","    except logs_client.exceptions.ResourceAlreadyExistsException:","        pass  # If the log stream already exists, we don't need to create it again.","","# Custom logging handler for CloudWatch","class CloudWatchLogHandler(logging.Handler):","    def emit(self, record):","        log_entry = self.format(record)","        timestamp = int(time.time() * 1000)  # Convert to milliseconds for CloudWatch","        logs_client.put_log_events(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM,","            logEvents=[","                {","                    'timestamp': timestamp,","                    'message': log_entry","                }","            ]","        )","","# Function to send a custom metric to CloudWatch for product added to wishlist","def log_product_added_to_wishlist(product_name, user_name):","    cloudwatch.put_metric_data(","        Namespace='ECommerceApp',","        MetricData=[","            {","                'MetricName': 'ProductAddedToWishlist',","                'Dimensions': [","                    {","                        'Name': 'ProductName',","                        'Value': product_name","                    },","                    {","                        'Name': 'UserName',","                        'Value': user_name","                    }","                ],","                'Value': 1,","                'Unit': 'Count'","            }","        ]","    )",""],"id":23}],[{"start":{"row":14,"column":0},"end":{"row":21,"column":83},"action":"remove","lines":["def create_log_stream():","    try:","        logs_client.create_log_stream(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM","        )","    except logs_client.exceptions.ResourceAlreadyExistsException:","        pass  # If the log stream already exists, we don't need to create it again."],"id":24},{"start":{"row":14,"column":0},"end":{"row":21,"column":56},"action":"insert","lines":["def create_log_stream():","    try:","        logs_client.create_log_stream(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM","        )","    except logs_client.exceptions.ResourceAlreadyExistsException:","        pass  # If log stream already exists, do nothing"]}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["a"],"id":25}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"remove","lines":["a"],"id":26}],[{"start":{"row":0,"column":0},"end":{"row":61,"column":0},"action":"remove","lines":["import boto3","import time","import logging","from django.conf import settings","","# Initialize CloudWatch and CloudWatch Logs clients","cloudwatch = boto3.client('cloudwatch', region_name=settings.AWS_REGION_NAME)","logs_client = boto3.client('logs', region_name=settings.AWS_REGION_NAME)","","# CloudWatch log group and stream","LOG_GROUP = 'django-logs'","LOG_STREAM = 'wishlist-log-stream'","","# Create a CloudWatch log stream if it doesn't exist","def create_log_stream():","    try:","        logs_client.create_log_stream(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM","        )","    except logs_client.exceptions.ResourceAlreadyExistsException:","        pass  # If log stream already exists, do nothing","","# Custom logging handler for CloudWatch","class CloudWatchLogHandler(logging.Handler):","    def emit(self, record):","        log_entry = self.format(record)","        timestamp = int(time.time() * 1000)  # Convert to milliseconds for CloudWatch","        logs_client.put_log_events(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM,","            logEvents=[","                {","                    'timestamp': timestamp,","                    'message': log_entry","                }","            ]","        )","","# Function to send a custom metric to CloudWatch for product added to wishlist","def log_product_added_to_wishlist(product_name, user_name):","    cloudwatch.put_metric_data(","        Namespace='ECommerceApp',","        MetricData=[","            {","                'MetricName': 'ProductAddedToWishlist',","                'Dimensions': [","                    {","                        'Name': 'ProductName',","                        'Value': product_name","                    },","                    {","                        'Name': 'UserName',","                        'Value': user_name","                    }","                ],","                'Value': 1,","                'Unit': 'Count'","            }","        ]","    )",""],"id":27},{"start":{"row":0,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["import boto3","import time","","# Initialize CloudWatch Logs client","logs_client = boto3.client('logs', region_name='us-east-1')","","# CloudWatch log group and stream","LOG_GROUP = 'django-logs'","LOG_STREAM = 'wishlist-log-stream'","","# Create CloudWatch log group if it doesn't exist","def create_log_group():","    try:","        # Check if the log group exists","        response = logs_client.describe_log_groups(logGroupNamePrefix=LOG_GROUP)","        if not response['logGroups']:","            # If it doesn't exist, create it","            logs_client.create_log_group(logGroupName=LOG_GROUP)","            print(f\"Log group '{LOG_GROUP}' created successfully!\")","        else:","            print(f\"Log group '{LOG_GROUP}' already exists.\")","    except Exception as e:","        print(f\"Error creating log group: {e}\")","","# Create CloudWatch log stream if it doesn't exist","def create_log_stream():","    try:","        # Ensure the log group exists","        create_log_group()","","        # Create the log stream","        logs_client.create_log_stream(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM","        )","        print(f\"Log stream '{LOG_STREAM}' created successfully!\")","    except logs_client.exceptions.ResourceAlreadyExistsException:","        print(f\"Log stream '{LOG_STREAM}' already exists.\")","    except Exception as e:","        print(f\"Error creating log stream: {e}\")",""]}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":28}],[{"start":{"row":41,"column":0},"end":{"row":54,"column":9},"action":"insert","lines":["class CloudWatchLogHandler(logging.Handler):","    def emit(self, record):","        log_entry = self.format(record)","        timestamp = int(time.time() * 1000)  # Timestamp in milliseconds","        ","        # Send logs to CloudWatch","        logs_client.put_log_events(","            logGroupName=LOG_GROUP,","            logStreamName=LOG_STREAM,","            logEvents=[{","                'timestamp': timestamp,","                'message': log_entry","            }]","        )"],"id":29}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import logging",""],"id":30}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":24},"action":"remove","lines":["django-logs"],"id":31},{"start":{"row":8,"column":13},"end":{"row":8,"column":29},"action":"insert","lines":["product_wishlist"]}],[{"start":{"row":55,"column":9},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"insert","lines":["        "]},{"start":{"row":56,"column":8},"end":{"row":57,"column":0},"action":"insert","lines":["",""]},{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":57,"column":4},"end":{"row":57,"column":8},"action":"remove","lines":["    "],"id":33},{"start":{"row":57,"column":0},"end":{"row":57,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":57,"column":0},"end":{"row":79,"column":63},"action":"insert","lines":["def publish_metric_to_cloudwatch(metric_name, value, dimensions=None):","    try:","        response = cloudwatch_client.put_metric_data(","            Namespace=NAMESPACE,  # Custom namespace for your app","            MetricData=[","                {","                    'MetricName': metric_name,","                    'Dimensions': dimensions if dimensions else [],","                    'Value': value,","                    'Unit': 'Count',","                    'StorageResolution': 60,  # 1-minute resolution","                },","            ]","        )","        print(f\"Successfully sent metric {metric_name} to CloudWatch\")","    except Exception as e:","        print(f\"Error sending metric to CloudWatch: {e}\")","","# Example usage of publishing a custom metric","def log_wishlist_addition(product_name):","    # You can modify this function to use dynamic data","    dimensions = [{'Name': 'Product', 'Value': product_name}]","    publish_metric_to_cloudwatch('ProductAdded', 1, dimensions)"],"id":34}],[{"start":{"row":63,"column":34},"end":{"row":63,"column":45},"action":"remove","lines":["metric_name"],"id":35},{"start":{"row":63,"column":34},"end":{"row":63,"column":50},"action":"insert","lines":["DjangoAppMetrics"]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":30},"action":"insert","lines":["NAMESPACE = 'DjangoAppMetrics'"],"id":36}],[{"start":{"row":10,"column":30},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":37}],[{"start":{"row":58,"column":0},"end":{"row":74,"column":57},"action":"remove","lines":["def publish_metric_to_cloudwatch(metric_name, value, dimensions=None):","    try:","        response = cloudwatch_client.put_metric_data(","            Namespace=NAMESPACE,  # Custom namespace for your app","            MetricData=[","                {","                    'MetricName': DjangoAppMetrics,","                    'Dimensions': dimensions if dimensions else [],","                    'Value': value,","                    'Unit': 'Count',","                    'StorageResolution': 60,  # 1-minute resolution","                },","            ]","        )","        print(f\"Successfully sent metric {metric_name} to CloudWatch\")","    except Exception as e:","        print(f\"Error sending metric to CloudWatch: {e}\")"],"id":38},{"start":{"row":58,"column":0},"end":{"row":77,"column":58},"action":"insert","lines":["def publish_metric_to_cloudwatch(metric_name, value, dimensions=None):","    try:","        response = cloudwatch_client.put_metric_data(","            Namespace=NAMESPACE,  # Custom namespace for your app","            MetricData=[","                {","                    'MetricName': metric_name,  # The metric name (ProductAdded)","                    'Dimensions': dimensions if dimensions else [],","                    'Value': value,  # Metric value (1 for each product added)","                    'Unit': 'Count',  # Unit for counting (products added)","                    'StorageResolution': 60,  # 1-minute resolution","                },","            ]","        )","        print(f\"Successfully sent metric {metric_name} to CloudWatch\")","    except Exception as e:","        print(f\"Error sending metric to CloudWatch: {e}\")","","","# Function to track wishlist additions (publishing metric)"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":90},"action":"insert","lines":["cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-1')  # Your AWS region"],"id":39}],[{"start":{"row":58,"column":0},"end":{"row":75,"column":0},"action":"remove","lines":["def publish_metric_to_cloudwatch(metric_name, value, dimensions=None):","    try:","        response = cloudwatch_client.put_metric_data(","            Namespace=NAMESPACE,  # Custom namespace for your app","            MetricData=[","                {","                    'MetricName': metric_name,  # The metric name (ProductAdded)","                    'Dimensions': dimensions if dimensions else [],","                    'Value': value,  # Metric value (1 for each product added)","                    'Unit': 'Count',  # Unit for counting (products added)","                    'StorageResolution': 60,  # 1-minute resolution","                },","            ]","        )","        print(f\"Successfully sent metric {metric_name} to CloudWatch\")","    except Exception as e:","        print(f\"Error sending metric to CloudWatch: {e}\")",""],"id":40},{"start":{"row":58,"column":0},"end":{"row":74,"column":57},"action":"insert","lines":["def publish_metric_to_cloudwatch(metric_name, value, dimensions=None):","    try:","        response = cloudwatch_client.put_metric_data(","            Namespace=NAMESPACE,  # Custom namespace for your app","            MetricData=[","                {","                    'MetricName': metric_name,  # The metric name (ProductAdded)","                    'Dimensions': dimensions if dimensions else [],","                    'Value': value,  # Metric value (1 for each product added)","                    'Unit': 'Count',  # Unit for counting (products added)","                    'StorageResolution': 60,  # 1-minute resolution","                },","            ]","        )","        print(f\"Successfully sent metric {metric_name} to CloudWatch\")","    except Exception as e:","        print(f\"Error sending metric to CloudWatch: {e}\")"]}],[{"start":{"row":61,"column":22},"end":{"row":61,"column":31},"action":"remove","lines":["NAMESPACE"],"id":41},{"start":{"row":61,"column":22},"end":{"row":61,"column":40},"action":"insert","lines":["'DjangoAppMetrics'"]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":[" "],"id":50},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":[" "]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":[" "]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":[" "],"id":50},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":[" "]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":[" "]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":[" "],"id":51},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":[" "]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":[" "]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"remove","lines":[" "],"id":52},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":[" "],"id":53},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":[" "]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":[" "]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":[" "]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":[" "]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":[" "]}],[{"start":{"row":14,"column":4},"end":{"row":24,"column":47},"action":"remove","lines":["try:","        # Check if the log group exists","        response = logs_client.describe_log_groups(logGroupNamePrefix=LOG_GROUP)","        if not response['logGroups']:","            # If it doesn't exist, create it","            logs_client.create_log_group(logGroupName=LOG_GROUP)","            print(f\"Log group '{LOG_GROUP}' created successfully!\")","        else:","            print(f\"Log group '{LOG_GROUP}' already exists.\")","    except Exception as e:","        print(f\"Error creating log group: {e}\")"],"id":54},{"start":{"row":14,"column":4},"end":{"row":18,"column":22},"action":"insert","lines":["try:","    response = cloudwatch_logs.describe_log_groups()","    print('Log groups:', response)","except Exception as e:","    print('Error:', e)"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":72},"action":"remove","lines":["cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-1') "],"id":55},{"start":{"row":6,"column":0},"end":{"row":6,"column":63},"action":"insert","lines":["cloudwatch_logs = boto3.client('logs', region_name='us-east-1')"]}]]},"ace":{"folds":[],"scrolltop":1033.6000000000001,"scrollleft":0,"selection":{"start":{"row":82,"column":63},"end":{"row":82,"column":63},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":50,"state":"start","mode":"ace/mode/python"}},"timestamp":1731683219418,"hash":"174707be52e9ac58b25afedabfd9eb954ea38f17"}