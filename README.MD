# Odoo 14 Docker

Dockerized odoo server


## Instructions

1. Add a ```.env``` file to this directory with the variables: ```ODOO_DATABASE_USER``` and ```ODOO_DATABASE_PASSWORD```

To build this project, run the following command on the parent directory of this repository while having docker and compose installed.

```
docker-compose --env-file ./.env up 
```
