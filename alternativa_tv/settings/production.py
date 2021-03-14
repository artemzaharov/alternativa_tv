from .base import *

DEBUG = False
SECRET_KEY = 'ily59&dfggsdfgdsfgfsdsdfd0=06*=86(^f*kynugu*jl_vlokh@%r9sjddzzf0r=b8'
ALLOWED_HOSTS = ['alternativatv.ru','www.alternativatv.ru']
try:
    from .local import *
except ImportError:
    pass
