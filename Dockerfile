# Container image that runs your code
FROM python:3.8-alpine

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY get_asana_task_info.py /get_asana_task_info.py
COPY entrypoint.sh /entrypoint.sh

# # Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
