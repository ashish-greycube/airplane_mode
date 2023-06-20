import frappe
from frappe.utils import random_string
import random
from frappe import _

def validate_airplane_ticket(doc,method):
    if doc.doctype == "Airplane Ticket" and doc.status != "Boarded":
        frappe.throw("You can only submit the Airplane Ticket document if the status is 'Boarded'.")

@frappe.whitelist()
def set_random_seat(doc, method):
    if doc.doctype == "Airplane Ticket" and doc.is_new():
        random_integer = random.randint(1, 99)
        random_alphabet = random.choice(["A", "B", "C", "D", "E"])
        seat = f"{random_integer}{random_alphabet}"
        doc.seat = seat