#!/bin/bash
#docker compose exec odoo /bin/bash -c "cd /mnt/extra-addons && pip install -r requirements.txt"
#exit

# Execute commands inside the Docker container using Docker Compose
docker compose exec -T odoo /bin/bash << EOF

# Change directory to /mnt/extra
cd /mnt/extra-addons

# Install requirements
pip install -r requirements.txt

# Execute the main.py script
exit
EOF
