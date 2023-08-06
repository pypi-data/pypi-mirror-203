import os

# Base directory of the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database configuration
DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
DATABASE_ECHO = False
DATABASE_POOL_RECYCLE = 3600
DATABASE_POOL_SIZE = 10

# Migration configuration
MIGRATION_DIR = os.path.join(BASE_DIR, 'migrations')
