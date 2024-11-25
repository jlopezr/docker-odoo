# Grafana

## Grafana setup

1. Create Postgres Data Source
    - Host URL: postgres: 5432
    - Database name: test (the one you used in Odoo)
    - Username: odoo (This are the default ones in .env)
    - Password: 123456
    - TLS/SSL Mode: disable

2. Import a dashboard
    - Home > Dashboards > New > Import
    - Drag and drop the file dashboard.json

## Create a public link of a dashboard

1. Go to a dashboard
2. Exit the edit mode!!
3. Click on the share button at the top right part of the dashboard.
4. Select Public Dashboard
5. Acknowledge all the items
6. Generate the public URL

