# Redis
#CELERY_BROKER_URL='redis://redis:6379/0'
#CELERY_RESULT_BACKEND='redis://redis:6379/0'
# RabbitMQ
CELERY_BROKER_URL='pyamqp://admin:mypass@rabbit//'
CELERY_RESULT_BACKEND='rpc://'

# Flask Mail
MAIL_DEFAULT_SENDER="axiome333@gmail.com"
MAIL_USERNAME="axiome333@gmail.com"
MAIL_PASSWORD="neufeldlab333"
MAIL_SERVER="smtp.gmail.com"
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True