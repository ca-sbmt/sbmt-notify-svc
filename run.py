import os
from pathlib import Path
from dotenv import load_dotenv
import uvicorn

# Load environment variables based on the specified environment
ENV_TYPE = os.getenv("ENV_TYPE", "local")
env_path = Path(".") / f".env.{ENV_TYPE}"
load_dotenv(dotenv_path=env_path)

if __name__ == "__main__":
    if ENV_TYPE in ["local","dev", "prod"]:
        uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=(ENV_TYPE == "local"))
    else:
        print("Invalid environment type. Please set ENV_TYPE to 'local' or 'dev' or 'prod'.")
