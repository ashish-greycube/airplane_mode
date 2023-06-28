// Copyright (c) 2023, Vijay and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
	refresh: function(frm) {
		if (!frm.doc.website) {
			//frappe.msgprint("No website added");
		}
		else{
			frm.add_web_link('https://www.spicejet.com/','Visit Website')
		}
	}
});
