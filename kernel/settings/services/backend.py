from decouple import config

# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda hosts: [host.strip() for host in hosts.split(',')])
# ALLOWED_HOSTS = config('ALLOWED_HOSTS').splite(',')

SECRET_KEY = config('SECRET_KEY')