# EB(EC2) 운영환경

from .settings import *

# 운영환경에서는 반드시 False로 설정
DEBUG = False

ALLOWED_HOSTS = [
'Eb-django-app-env.eba-m8kemdqr.ap-northeast-2.elasticbeanstalk.com'
]

