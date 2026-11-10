#!/bin/bash
export PATH="$PATH:/home/chinmayi/.local/bin"
cd /home/chinmayi/employee-bench
: "${MARIADB_ROOT_PASSWORD:?Set MARIADB_ROOT_PASSWORD before running this script}"
: "${FRAPPE_ADMIN_PASSWORD:?Set FRAPPE_ADMIN_PASSWORD before running this script}"
bench new-site employee.localhost \
  --mariadb-root-password "$MARIADB_ROOT_PASSWORD" \
  --admin-password "$FRAPPE_ADMIN_PASSWORD"
