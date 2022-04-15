import os

from fastapi import FastAPI

app = FastAPI()

# Check env variables
required_env_variables = [
    "SMTP_HOST",
    "SMTP_PORT"
]

for env_variable in required_env_variables:
    if not os.environ[env_variable]:
        raise EnvironmentError(f"Environment variable: {env_variable} not provided")