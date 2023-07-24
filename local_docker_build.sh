#!/bin/bash

export IMAGE=fda
export VERSIONS=0.1

echo "Building docker file for ${IMAGE} image with ${VERSION} tag"

docker build --build-arg ARTIFACTORY_USERNAME=${ARTIFACTORY_USERNAME} --build-arg ARTIFACTORY_TOKEN=${ARTIFACTORYTOKEN} -t ${IMAGE}:${VERSION} -f docker/Dockerfile .