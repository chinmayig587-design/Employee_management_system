import frappe
from employee_manager.api import add_department, get_departments, add_employee, get_employees
from employee_manager.mongodb import get_collection

def run_tests():
    log_file = "/home/chinmayi/employee-bench/test_output.log"
    with open(log_file, "w") as f:
        f.write("[+] Running backend tests...\n")
        
        col_dept = get_collection("departments")
        col_emp = get_collection("employees")
        
        col_dept.delete_many({"department_id": "TEST-DEPT"})
        col_emp.delete_many({"employee_id": "TEST-EMP"})
        
        f.write("[+] Testing add_department...\n")
        frappe.form_dict = {
            "department_id": "TEST-DEPT",
            "name": "Test Department",
            "description": "This is a test department"
        }
        res_dept = add_department()
        f.write(f"add_department result: {res_dept}\n")
        
        f.write("[+] Testing get_departments...\n")
        depts = get_departments()
        f.write(f"get_departments result count: {len(depts)}\n")
        assert any(d["department_id"] == "TEST-DEPT" for d in depts), "Department not found!"
        
        f.write("[+] Testing add_employee...\n")
        frappe.form_dict = {
            "employee_id": "TEST-EMP",
            "first_name": "Testy",
            "last_name": "McTestFace",
            "email": "testy@test.com",
            "phone": "123456",
            "department_id": "TEST-DEPT",
            "designation": "Tester",
            "date_of_joining": "2026-08-10",
            "salary": 1000,
            "status": "Active"
        }
        res_emp = add_employee()
        f.write(f"add_employee result: {res_emp}\n")
        
        f.write("[+] Testing get_employees...\n")
        emps = get_employees()
        f.write(f"get_employees result count: {len(emps)}\n")
        assert any(e["employee_id"] == "TEST-EMP" for e in emps), "Employee not found!"
        
        col_dept.delete_many({"department_id": "TEST-DEPT"})
        col_emp.delete_many({"employee_id": "TEST-EMP"})
        f.write("[+] All API tests passed successfully!\n")
