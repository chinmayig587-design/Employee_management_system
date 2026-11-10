import frappe
frappe.init(site="employee.localhost", sites_path="/home/chinmayi/employee-bench/sites")
frappe.connect()
from employee_manager.test_api import run_tests
run_tests()
