import os

from dotenv import load_dotenv
from api import GithubApp

load_dotenv(".env")
load_dotenv("deploy/.env")

OWNER = os.environ.get("OWNER")
REPOSITORY = os.environ.get("REPOSITORY")

api = GithubApp(
    os.path.expanduser(os.environ.get("KEY_FILE_PATH")),
    os.environ.get("APP_ID")
)

deployment_id = api.create_deployment(OWNER, REPOSITORY)["id"]

# DEPLOYMENT CODE START

from time import sleep

sleep(5)

# DEPLOYMENT CODE END

api.update_deployment_status(OWNER, REPOSITORY, deployment_id, state="success")
