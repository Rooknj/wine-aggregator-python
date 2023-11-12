# Python Service: [`qbaa-genai-plugin`](https://devportal.intuit.com/app/dp/resource/3029814242517068521/overview)

[![Build Status](https://build.intuit.com/qbo-2/buildStatus/buildIcon?job=qbshared-integrations/qbaa-genai-plugin/qbaa-genai-plugin/master)](https://build.intuit.com/qbo-2/blue/organizations/jenkins/qbshared-integrations%2Fqbaa-genai-plugin%2Fqbaa-genai-plugin/activity?branch=master)
[![codecov](https://codecov.tools.a.intuit.com/ghe/qbshared-integrations/qbaa-genai-plugin/branch/master/graph/badge.svg)](https://codecov.tools.a.intuit.com/ghe/qbshared-integrations/qbaa-genai-plugin)

This Python service was created from Intuit's Service Paved Road.
For support with the paved road:
* Check [StackOverflow tag `psk`](https://stackoverflow.intuit.com/posts/tagged/4803)
* Ask in Slack channel [#cmty-psk](https://intuit-teams.slack.com/archives/C04AR7RF97G)
* For general Service Paved Road support (not Python specific) see [#cmty-services-paved-road](https://intuit-teams.slack.com/archives/C04AFMJ140K)

For support with this service, use Slack channel [#REPLACEME](https://intuit-teams.slack.com/archives/REPLACEME).



## API docs

If running the service locally, available at `/apidoc/swagger` and `/apidoc/redoc`

## Development

This service is built on the [FastAPI framework](https://fastapi.tiangolo.com/).
If you are not familiar with Python's asyncio, we strongly recommend reading the
[Concurrency and async / await](https://fastapi.tiangolo.com/async/) docs first!
Or, "If you just don't know, use normal `def`."

### First: Set up [Lefthook](https://github.com/Arkweid/lefthook)

This project uses Lefthook to manage Git hooks. This will auto-format your code on commit
You can install it via Brew:

```sh
brew install Arkweid/lefthook/lefthook
```

After installation, initialize it via:

```sh
lefthook install
```

It is currently used for linting on pre-commit which you can run via:

```sh
lefthook run pre-commit
```

### Poetry

This library uses [poetry](https://python-poetry.org/docs/basic-usage/#specifying-dependencies) to manage Python dependencies.
To install:

```shell
curl -sSL https://install.python-poetry.org | python3 - --version 1.4.2
```

For additional installation options (e.g. setting the PATH, installing a specific version of poetry),
see the [docs](https://python-poetry.org/docs/#installing-with-the-official-installer).


### Virtual Environment

Create by running

```shell
poetry install
```

Then set the Python interpreter to use the one in the newly created virtual environment (.venv folder). In VSCode for Mac, you can change the Python interpreter using ```Shift+Command+P```

:warning: After running `poetry install` for the first time,
[commit your poetry.lock file to version control](https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control).


Make sure you have `podman` installed.
See [StackOverflow: How do I get started with Podman?](https://stackoverflow.intuit.com/questions/26032) for details.

#### Troubleshooting

If the Python interpreter cannot be found or if there are any other issues with the Poetry virtual environment, go to the root project folder and run these commands:

1. Run
```shell
poetry env remove --all
```
2. Run
```shell
poetry install
```

### IDPS

IDPS integration on local is needed if you need to retrieve any secrets during testing in your development environment. To get it working locally follow the next steps:

1. Install [AWS CLI](https://aws.amazon.com/cli/) with Homebrew
	```bash
	$ brew install awscli
	```
1. Install eiamcli from https://github.intuit.com/EIAM/eiamCli-golang#installation 
1. Contact @rpinerosrho, @ajith or @naren to get ```Developer``` access to this [AWS account](https://devportal.intuit.com/app/dp/resource/2306986501422570059/overview)
1. Create the AWS temp credentials file
	```bash
	$ mkdir ~/.aws && 
	$ touch ~/.aws/credentials
	```
1. Authenticate in eiamcli 
	```bash
	$ eiamcli login
	```
1. Get temporary AWS credentials
	```bash
	$ eiamcli aws_creds -a 326054880772 -r Developer -p genos-plugin
	```
1. Confirm AWS temp credentials were set correctly
	```bash
	$ cat ~/.aws/credentials
	
	[genos-plugin]
	aws_access_key_id=XXXXX
	aws_secret_access_key=XXXXX
	aws_session_token=XXXXX
	```
	*(If the file appears empty try with the `sudo` prefix)*

#### Gotchas
If there is an error stating that the credentials file does not exist. You need to create the credentials file manually:
1. Create the aws directory in your home folder
```bash
mkdir ~/.aws
```
2. Create the credentials file
```bash
touch ~/.aws/credentials
```



### Running project locally using Podman

This project supports Podman and Docker locally via compose files

#### Setting up

1. Install Podman by running
```bash
brew install podman
```
2. Install Podman-Compose by running
```bash
brew install podman-compose
```
3. Run the following command and verify that your podman-compose version is at least 1.0.4
```bash
podman-compose -v
```
4. Run
```bash
podman machine init
```
5. Start the Podman VM by running
```bash
podman machine start
```
#### Running it
1. From the project root directory, run
```bash
./scripts/run_local.sh up
```
2. The qbaa-genai-plugin will be available in localhost port 8090
#### How to exit
1. From the project root directory, run
```bash
./scripts/run_local.sh down
```
##### Alternatively
1. In the same terminal that is running the qbaa-genai-plugin container press Crtl+C
2. Run
```bash
./scripts/run_local.sh down
```

### Running project locally using docker Using Docker

This project supports Podman and Docker locally via compose files

#### Setting up

1. Install Docker Desktop from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Sign into Docker using your Intuit email address

#### Running it

1. Run the Docker Desktop application
2. From the project root directory, run
```bash
./scripts/run_local.sh up
```
3. The qbaa-genai-plugin will be available in localhost port 8090

#### How to exit

1. From the project root directory, run
```bash
./scripts/run_local.sh down
```

##### Alternatively

1. In the same terminal that is running the qbaa-genai-plugin container press Crtl+C
2. Docker is able to handle the shutdown of the containers more gracefully than Podman, so running "./scripts/run_local.sh down" is not required

### Local development using Docker/Podman containerized environments

When running docker-compose up or podman-compose up, the contents of the /app folder will be mounted in the container. In addition, the Python runtime will watch for changes to Python source files in the /app folder and automatically trigger a refresh to make the changes available in the running container.

Note: If the changes involve installing a new package/library then you should exit and start the container environment again (See [How to exit](#how-to-exit) for Podman or Docker).

You can use Postman, Curl or any other client of your choice to make https requests to the qbaa-genai-plugin container on localhost port 8090.

#### Gotchas

For issues during build or as a final stage in troubleshooting you might want to force a rebuild of the container image, to do so, follow these steps

1. Exit the container (See [How to exit](#how-to-exit))
2. From the project root directory, run
```bash
./scripts/run_local.sh restart
```

### Running Locally via Hypercorn

To run locally:
```bash
poetry run hypercorn app/start.py --reload
```

This will start the Hypercorn in your development machine to run the application locally, outside of a containerized environment.

### :warning: Merging your code :warning:

1. Make sure that the qbaa-genai-plugin can run in a containerized environment. To do that, follow the instructions in [Using Podman](#using-podman) or [Using Docker](#using-docker).
2. Test your new functionality while running the container.

**Not following the above steps might result in breaking changes being introduced.**

### Debugging Locally (VSCode)

1. From the project root directory, run
```bash
./scripts/run_debug.sh up
```
2. Go to the Run and Debug section and run the ```Python Debug: Remote Attach profile```

![](docs/images/vscode_debugging/1.png)

3. Now you can set breakpoints and debug at will

[See this video for a demonstration](https://drive.google.com/file/d/1cCRqh6PDZ4LNnsRpzbHKBXweXJ_9mBwr/view?usp=share_link)

To test path used by Service Mesh, use port 8090 without https e.g. [http://localhost:8090/health/full](http://localhost:8090/health/full)

#### How to exit

1. From the project root directory, run
```bash
./scripts/run_debug.sh down
```

#### How to rebuild

1. From the project root directory, run
```bash
./scripts/run_debug.sh rebuild
```

## Testing Plugins

### Registration
Pugins need to be registered with the GenOS app (See [here](https://github.intuit.com/qbshared-integrations/qbaa-genai-plugin/blob/master/app/start.py#L30))

### Sending Requests

Each plugin is exposed for POST requests following this pattern
```
http://localhost:8090/v1/genosplugins/<plugin_name>/generate
```
The input to the plugin will be in the payload of the request

### Testing
Run unit tests with:
```
poetry run pytest app/test/unit --cov=app --cov-report html --cov-report xml
```


### Troubleshooting

1. if you encounter `Bind for 0.0.0.0:8490 failed: port is already allocated.` error, you port is already running. You
should stop the running container in docker (desktop or CLI) and try again.

## Health endpoints

* `/health/full` (gw supported format)

Navigate to [https://localhost:8443/health/full](https://localhost:8443/health/full), you should be able to see the
following response

```
{"status":"Healthy"}
```

## Monitoring and Metrics

Prometheus is integrated into this project with ```prometheus_fastapi_instrumentator```.

## IntelliJ Setup
https://github.intuit.com/qbshared-integrations/qbaa-genai-plugin/wiki/IntelliJ-Setup
