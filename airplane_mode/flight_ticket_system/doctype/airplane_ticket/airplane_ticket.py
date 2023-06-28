# Copyright (c) 2023, Vijay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import flt, cint, cstr
from random import randint, choice


class AirplaneTicket(Document):
    # def before_insert(self):
    #     self.set_seat_number()

    def validate(self):
        # remove duplicates in add ons
        add_ons = {d.item: d for d in self.add_ons}
        self.add_ons = add_ons.values()

        # set total amount
        self.total_amount = flt(self.flight_price) + sum(
            [flt(d.amount) for d in self.add_ons]
        )

        airplane = frappe.get_value('Airplane Flight', self.flight, 'airplane')
        if airplane:
			# Get the capacity of the airplane
            airplane_capacity = frappe.get_value('Airplane', airplane, 'capacity')
			
			# Count the number of existing tickets for the flight
            existing_tickets = frappe.get_all('Airplane Ticket', filters={'flight': self.flight}, as_list=True)
            if existing_tickets and len(existing_tickets) >= airplane_capacity:
                frappe.throw(_("The number of tickets for this flight has reached the maximum capacity of the airplane."))

    def before_submit(self):
        if not self.status == "Boarded":
            frappe.throw(_("Cannot submit Ticket when status is not Boarded."))

    # def set_seat_number(self):
    #     self.seat = cstr(randint(1, 300)) + choice(["A", "B", "C", "D", "E"])

