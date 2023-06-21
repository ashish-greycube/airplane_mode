# Copyright (c) 2023, Vijay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import flt, cint, cstr
from random import randint, choice


class AirplaneTicket(Document):
    def before_insert(self):
        self.set_seat_number()

    def validate(self):
        # remove duplicates in add ons
        add_ons = {d.item: d for d in self.add_ons}
        self.add_ons = add_ons.values()

        # set total amount
        self.total_amount = flt(self.flight_price) + sum(
            [flt(d.amount) for d in self.add_ons]
        )

    def before_submit(self):
        if not self.status == "Boarded":
            frappe.throw(_("Cannot submit Ticket when status is not Boarded."))

    def set_seat_number(self):
        self.seat = cstr(randint(1, 300)) + choice(["A", "B", "C", "D", "E"])
