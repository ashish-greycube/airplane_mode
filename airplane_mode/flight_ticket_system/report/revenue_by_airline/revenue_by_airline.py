# Copyright (c) 2023, Vijay and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "label": "Airline",
            "fieldtype": "Link",
            "options": "Airline",
            "fieldname": "airline",
            "width": 300,
        },
        {
            "label": "Revenue",
            "fieldtype": "Currency",
            "fieldname": "revenue",
            "width": 300,
            "currency": "INR",
        },
    ]
    data = get_data(filters)
    return columns, data, None, get_chart(data), get_summary(data)


def get_data(filters):
    return frappe.db.sql(
        """
    select  
        ta.airline , sum(total_amount) revenue
    from `tabAirplane Ticket` tat 
    inner join `tabAirplane Flight` taf on taf.name = tat.flight 
    inner join tabAirplane ta on ta.name = taf.airplane 
    where tat.docstatus = 1
    group by ta.airline 
    order by revenue desc
    """,
        as_dict=True,
    )


def get_chart(data):
    revenue = {d.airline: d.revenue for d in data}

    labels = frappe.db.get_all("Airline", pluck="name")
    values = [revenue.get(label, 0) for label in labels]

    chart = {
        "data": {
            "labels": [_(label) for label in labels],
            "datasets": [{"name": "Airlinewise Revenue Chart", "values": values}],
        },
        "type": "donut",
        "height": 300,
    }

    return chart


def get_summary(data):
    return [
        {
            "value": sum(d.revenue for d in data),
            "label": _("Total Revenue"),
            "datatype": "Currency",
            "currency": "INR",
        },
    ]
