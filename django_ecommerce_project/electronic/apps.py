from django.apps import AppConfig
from .cloudwatch_utils import create_log_stream  # Import the CloudWatch utility

class ElectronicConfig(AppConfig):
    name = 'electronic'

    def ready(self):
        # Run log stream creation at startup
        create_log_stream()
