#! /bin/sh

docker build -t $DOCKER_HUB_REPOSITORY:$GITHUB_SHA ./
docker login -p "$DOCKER_HUB_PASS" -u "$DOCKER_HUB_USERNAME"
docker push $DOCKER_HUB_REPOSITORY:$GITHUB_SHA