# Copyright (c) 2023, Vijay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import cstr


class FlightPassenger(Document):
    def before_save(self):
        self.full_name = " ".join([cstr(self.first_name), cstr(self.last_name)]).strip()
