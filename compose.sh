#/bin/bash
docker-compose down
docker-compose --env-file ./.env up --remove-orphans --detach --build
