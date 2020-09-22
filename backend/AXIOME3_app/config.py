import os
# Redis
#CELERY_BROKER_URL='redis://redis:6379/0'
#CELERY_RESULT_BACKEND='redis://redis:6379/0'
# RabbitMQ
#CELERY_BROKER_URL='pyamqp://admin:mypass@rabbit//'
#CELERY_RESULT_BACKEND='rpc://'

CELERY_BROKER_URL='pyamqp://axiome3:neufeld@rabbit/axiome3_host'
CELERY_RESULT_BACKEND='rpc://'

# Gmail API
GMAIL_SENDER = os.environ.get('GMAIL_SENDER')

# Default classifier path
# QIIME2 2020.6 SILVA 138
DEFAULT_CLASSIFIER_PATH="/pipeline/AXIOME3/2020_06_classifier_silva138_NR99_V4V5.qza"