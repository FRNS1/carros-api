import string
import random

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))
DEBUG=True
SECRET_KEY = key

AWS_BUCKET_NAME='carros-projeto'
AWS_ACCESS_KEY='AKIARRHBXYEH2XJAHWUF'
AWS_SECRET_ACCESS_KEY='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'
AWS_DOMAIN='http://carros-projeto.s3.amazonaws.com'