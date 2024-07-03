import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
ORG_NAME = os.getenv('ORG_NAME')
ECS_CLUSTER = os.getenv('ECS_CLUSTER')
ECS_SERVICE = os.getenv('ECS_SERVICE')
ECS_TASK_DEFINITION = os.getenv('ECS_TASK_DEFINITION')
REGION = os.getenv('REGION', 'eu-central-1')
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', 60))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
