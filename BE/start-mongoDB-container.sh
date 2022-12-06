#!/bin/sh

docker run \
    --name mongodb \
    -v ~/mongodb:/data/db \
    -d \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=root \
    -e MONGO_INITDB_ROOT_PASSWORD=root \
    --restart=always \
    mongo