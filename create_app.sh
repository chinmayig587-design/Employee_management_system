#!/bin/bash
export PATH="$PATH:/home/chinmayi/.local/bin"
cd /home/chinmayi/employee-bench
echo -e "\nEmployee Management System using Frappe and MongoDB\nAntigravity\nadmin@employee.localhost\nmit\nn\n" | bench new-app employee_manager --no-git
