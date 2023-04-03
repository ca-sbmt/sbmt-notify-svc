To run the application locally with all dependencies, run: make run-local-with-deps
To run the application in Docker with all dependencies, run: make run-docker-with-deps


├── Dockerfile
├── .env.local
├── .env.dev
├── .env.prod
├── LICENSE
├── Makefile
├── Readme.md
├── app
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── run.py
├── tests
│   ├── test_example.py




Open your Codespace in the browser.

In the address bar, you should see the hostname or IP address of your Codespace (e.g. my-codespace-abc12345-12345-12345.github.dev). Copy this value as the CODESPACE_HOST.

In the Codespace terminal, type the command whoami and press Enter. This will give you your Codespace username, which you can use as the CODESPACE_USERNAME.

To get the CODESPACE_PASSWORD, you can create a personal access token (PAT) in your GitHub account settings with the "repo" scope. Then, in your Codespace terminal, run the command echo TOKEN_VALUE | docker login https://ghcr.io -u USERNAME --password-stdin, where TOKEN_VALUE is your PAT and USERNAME is your GitHub username. After running this command, your Codespace will be authenticated to pull images from the GitHub Container Registry. You can then use your PAT as the CODESPACE_PASSWORD.

