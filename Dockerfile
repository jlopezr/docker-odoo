FROM odoo:15.0

USER root

RUN apt-get update && apt-get install -y git
