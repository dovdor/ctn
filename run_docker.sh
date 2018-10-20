#!/usr/bin/env bash
set -o errexit
make > /dev/null
docker run --rm --name ctn dovdor/change-time-to-now:latest "$@"
