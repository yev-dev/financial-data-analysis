#!/bin/bash

export VERSION=0.1
export IMAGE_NAME=fda
export DOCKER_USER_HOME=/home/fda-user
export PORT_NUM=9999

echo "Running ${IMAGE_NAME} image for ${VERSION} version tag"

docker run --name ${IMAGE_NAME} -it --rm --detach -p {PORT_NUM}
--volume ${HOME}/notebooks/fda:${DOCKER_USER HOME}/notebooks
--volume ${HOME}/data/fda:${DOCKER_USER_HOME}/notebooks/data
${IMAGE}:${VERSION}
