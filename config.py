import os
from dotenv import load_dotenv

# Assuming this script is in the same directory as the .env file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


DATABASE_URL = os.environ["DATABASE_URL"]
TEST_DATABASE_URL = os.environ["TEST_DATABASE_URL"]
RABBITMQ_URL = os.environ["RABBITMQ_URL"]
SENTRY_DSN = os.environ["SENTRY_DSN"]
