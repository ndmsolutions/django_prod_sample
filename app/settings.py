import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

PRODUCTION = env('PRODUCTION')

if PRODUCTION == 'True':
    from .prod_settings import *
else:
    from .dev_settings import *
