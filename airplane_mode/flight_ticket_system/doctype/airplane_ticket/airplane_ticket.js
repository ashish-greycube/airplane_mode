frappe.ui.form.on("Airplane Ticket", {
  refresh: function (frm) {
    frm.add_custom_button(
      "Assign Seat",
      () => {
        frm.events.assign_seat(frm);
      },
      "Actions"
    );
  },

  assign_seat: function (frm) {
    frappe.prompt(
      [
        {
          fieldname: "seat_number",
          label: "Seat Number",
          fieldtype: "Data",
          reqd: 1,
        },
      ],
      function (values) {
        frm.set_value("seat", values.seat_number);
        frm.save();
      },
      "Seat Number",
      "Assign"
    );
  },
});
