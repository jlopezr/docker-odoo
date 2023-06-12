#!/bin/bash
docker-compose stop odoo
docker-compose run --service-ports odoo --dev=all
