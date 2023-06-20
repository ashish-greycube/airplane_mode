# Copyright (c) 2023, Vijay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):

	def validate(self):
		add_ons = []
		for item in self.add_ons:
			if item.add_on_type in add_ons:
				frappe.throw(f"Duplicate add-on item found: {item.add_on_type}")
			add_ons.append(item.add_on_type)
	
	def before_save(self):
		add_on_item = self.add_ons

		total_add_on_amount_sum = 0
		for item in add_on_item:
			total_add_on_amount_sum += item.amount

		self.total_amount = (self.ticket_price) + (total_add_on_amount_sum)
		

