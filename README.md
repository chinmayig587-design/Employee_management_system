# Employee Management System

An employee-management project using Frappe for the application/API layer and MongoDB for employee, department, attendance, and leave data.

## Project files

- `api.py` contains the Frappe API methods.
- `mongodb.py` provides the MongoDB connection.
- `index.html` contains the application interface.
- The shell scripts set up and run the Frappe bench and MongoDB on Linux.

## Setup notes

The setup scripts currently use the original developer's Linux paths. Update those paths to match your environment before running them.

To create a Frappe site, provide passwords through environment variables rather than storing them in the script:

```bash
export MARIADB_ROOT_PASSWORD='your-mariadb-password'
export FRAPPE_ADMIN_PASSWORD='your-frappe-admin-password'
./create_site.sh
unset MARIADB_ROOT_PASSWORD FRAPPE_ADMIN_PASSWORD
```

Do not commit passwords, database dumps, generated site files, or local environment files.
