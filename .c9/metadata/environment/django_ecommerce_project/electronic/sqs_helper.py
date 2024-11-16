{"filter":false,"title":"sqs_helper.py","tooltip":"/django_ecommerce_project/electronic/sqs_helper.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["# sqs_helper.py","","import boto3","from django.conf import settings","","# Initialize SQS client","sqs = boto3.client('sqs', region_name=settings.AWS_SQS_REGION)","","def send_message_to_sqs(message_body):","    \"\"\"","    Function to send a message to the SQS queue.","    \"\"\"","    try:","        # Send message to SQS queue","        response = sqs.send_message(","            QueueUrl=settings.AWS_SQS_QUEUE_URL,","            MessageBody=message_body","        )","        print(f\"Message sent to SQS: {response['MessageId']}\")","    except Exception as e:","        print(f\"Error sending message to SQS: {str(e)}\")",""],"id":1}]]},"ace":{"folds":[],"scrolltop":25.2,"scrollleft":0,"selection":{"start":{"row":21,"column":0},"end":{"row":21,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1731678479907,"hash":"208ace001a529f81538c6d227fc0798764d88418"}