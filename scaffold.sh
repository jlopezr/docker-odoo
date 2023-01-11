#!/bin/bash
docker-compose exec -ti odoo /usr/bin/odoo scaffold /mnt/extra-addons/$1
