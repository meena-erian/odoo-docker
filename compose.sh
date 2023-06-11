#!/bin/bash

mkdir -p -m 777 data/pgdata
mkdir -p -m 777 data/odoo
docker-compose up --remove-orphans -d