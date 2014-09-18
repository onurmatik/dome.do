DEBUG = False

AWS_REGION = 'eu-west-1'

with open('/etc/AWS_SECRET_ACCESS_KEY') as f:
    AWS_SECRET_ACCESS_KEY = f.read().strip()

AWS_ACCESS_KEY_ID = 'AKIAJURTH2SDBBT4A23A'
AWS_STORAGE_BUCKET_NAME = 'dome.do'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False

AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

AWS_SES_REGION_NAME = AWS_REGION
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'

EMAIL_BACKEND = 'django_ses.SESBackend'

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
# DEFAULT_S3_PATH = "/"
#
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = "static"

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
# MEDIA_ROOT = '/'
#
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
