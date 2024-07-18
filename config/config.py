from decouple import config

database_uri = config('DATABASE_URI')
fernet_key = config('FERNET_KEY')
secret_key = config('SECRET_KEY')