import frappe
from employee_manager.mongodb import get_collection
from bson import ObjectId
import json

def serialize(doc):
    if not doc:
        return doc
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

@frappe.whitelist(allow_guest=True)
def get_employees():
    col = get_collection("employees")
    employees = list(col.find().sort("employee_id", 1))
    return [serialize(e) for e in employees]

@frappe.whitelist(allow_guest=True)
def add_employee():
    data = frappe.form_dict
    col = get_collection("employees")
    
    if col.find_one({"employee_id": data.get("employee_id")}):
        frappe.throw("Employee ID already exists")
        
    doc = {
        "employee_id": data.get("employee_id"),
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "department_id": data.get("department_id"),
        "designation": data.get("designation"),
        "date_of_joining": data.get("date_of_joining"),
        "salary": float(data.get("salary") or 0.0),
        "status": data.get("status") or "Active"
    }
    
    result = col.insert_one(doc)
    return {"status": "success", "id": str(result.inserted_id)}

@frappe.whitelist(allow_guest=True)
def update_employee():
    data = frappe.form_dict
    col = get_collection("employees")
    
    employee_id = data.get("employee_id")
    if not employee_id:
        frappe.throw("Employee ID is required")
        
    update_data = {
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "department_id": data.get("department_id"),
        "designation": data.get("designation"),
        "date_of_joining": data.get("date_of_joining"),
        "salary": float(data.get("salary") or 0.0),
        "status": data.get("status") or "Active"
    }
    
    col.update_one({"employee_id": employee_id}, {"$set": update_data})
    return {"status": "success"}

@frappe.whitelist(allow_guest=True)
def delete_employee():
    employee_id = frappe.form_dict.get("employee_id")
    if not employee_id:
        frappe.throw("Employee ID is required")
        
    col = get_collection("employees")
    col.delete_one({"employee_id": employee_id})
    
    get_collection("attendance").delete_many({"employee_id": employee_id})
    get_collection("leaves").delete_many({"employee_id": employee_id})
    
    return {"status": "success"}

@frappe.whitelist(allow_guest=True)
def get_departments():
    col = get_collection("departments")
    departments = list(col.find().sort("name", 1))
    return [serialize(d) for d in departments]

@frappe.whitelist(allow_guest=True)
def add_department():
    data = frappe.form_dict
    col = get_collection("departments")
    
    dept_id = data.get("department_id")
    name = data.get("name")
    
    if col.find_one({"department_id": dept_id}):
        frappe.throw("Department ID already exists")
        
    doc = {
        "department_id": dept_id,
        "name": name,
        "description": data.get("description")
    }
    
    result = col.insert_one(doc)
    return {"status": "success", "id": str(result.inserted_id)}

@frappe.whitelist(allow_guest=True)
def delete_department():
    dept_id = frappe.form_dict.get("department_id")
    if not dept_id:
        frappe.throw("Department ID is required")
        
    col = get_collection("departments")
    col.delete_one({"department_id": dept_id})
    return {"status": "success"}

@frappe.whitelist(allow_guest=True)
def get_attendance():
    date = frappe.form_dict.get("date")
    if not date:
        frappe.throw("Date is required")
        
    col = get_collection("attendance")
    attendance_records = list(col.find({"date": date}))
    return [serialize(r) for r in attendance_records]

@frappe.whitelist(allow_guest=True)
def mark_attendance():
    data = frappe.form_dict
    date = data.get("date")
    records_str = data.get("records")
    
    if not date or not records_str:
        frappe.throw("Date and records are required")
        
    records = json.loads(records_str)
    col = get_collection("attendance")
    
    for emp_id, status in records.items():
        col.update_one(
            {"employee_id": emp_id, "date": date},
            {"$set": {"status": status}},
            upsert=True
        )
        
    return {"status": "success"}

@frappe.whitelist(allow_guest=True)
def get_leaves():
    col = get_collection("leaves")
    leaves = list(col.find().sort("start_date", -1))
    return [serialize(l) for l in leaves]

@frappe.whitelist(allow_guest=True)
def apply_leave():
    data = frappe.form_dict
    col = get_collection("leaves")
    
    import uuid
    leave_id = str(uuid.uuid4())[:8]
    
    doc = {
        "leave_id": leave_id,
        "employee_id": data.get("employee_id"),
        "leave_type": data.get("leave_type"),
        "start_date": data.get("start_date"),
        "end_date": data.get("end_date"),
        "reason": data.get("reason"),
        "status": "Pending"
    }
    
    col.insert_one(doc)
    return {"status": "success", "leave_id": leave_id}

@frappe.whitelist(allow_guest=True)
def update_leave_status():
    data = frappe.form_dict
    leave_id = data.get("leave_id")
    status = data.get("status")
    
    if not leave_id or not status:
        frappe.throw("Leave ID and status are required")
        
    col = get_collection("leaves")
    col.update_one({"leave_id": leave_id}, {"$set": {"status": status}})
    return {"status": "success"}
