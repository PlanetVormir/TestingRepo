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

process = Popen("sudo -S docker compose up -d".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
process.communicate(input("Enter production password: ").encode())
stdout, err = process.stdout.read().decode(), process.stderr.read().decode()
print(stdout, err, sep="\n\n")

api.update_deployment_status(OWNER, REPOSITORY, deployment_id, state="success")
