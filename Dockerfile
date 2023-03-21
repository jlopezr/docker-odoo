FROM odoo:15.0

USER root

RUN apt-get update && apt-get install -y git

USER odoo

RUN pip3 install git+https://github.com/tomquirk/linkedin-api.git && pip3 install linkedin-api~=2.0.0a
