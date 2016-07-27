#!/bin/bash
set +x
docker build -f Dockerfile-base -t mmaybeno/nylas-perft-demo .
docker build -f Dockerfile-flaskapp -t mmaybeno/flask-demo .
docker build -f Dockerfile-stackcollector -t mmaybeno/stackcollector-demo .
