import os
from subprocess import Popen, PIPE
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

err = False
try:
    process = Popen("sudo -S docker compose up -d".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process.communicate(os.environ.get("SUDO_PASSWORD").encode())
except Exception as e:
    print(e)
    err = True

if not err:
    api.update_deployment_status(OWNER, REPOSITORY, deployment_id, state="success")
else:
    api.update_deployment_status(OWNER, REPOSITORY, deployment_id, state="error")
