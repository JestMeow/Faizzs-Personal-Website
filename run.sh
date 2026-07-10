#!/bin/bash

set -a
source .env
set +a

flask --app $FLASK_APP --debug run

