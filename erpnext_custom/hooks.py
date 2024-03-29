# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_custom"
app_title = "ERPNext Customisation"
app_publisher = "NCC"
app_description = "Customisations for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "social@ncc.gov.gh"
app_license = "MIT"

fixtures = [
    {"dt": "Property Setter", "filters": [
        [
            "doc_type", "in", [
                "Employee",
                "Leave Application",
                "Leave Type",
                "Training Event",
                "Vehicle",
                "Notification",
                "Print Format"
            ]
        ]
    ]},
    {"dt": "Custom Field", "filters": [
        [
            "fieldname", "in", [
                "assumption_of_duty",
                "acceptance_date",
                "reports_to_name",
                "age",
                "employee_name",
                "year",
                "type",
                "tyre_type",
                "image",
                "column_break_7",
                "section_break_4",
                "department",
                "employee_number",
                "staff_id",
                "branch",
                "ssnit",
                "workflow_state",
                "additional_cell_number",
                "status",
                "ghanacard_details",
                "personal_id_number",
                "document_number",
                "column_break_83",
                "ghanacard_date_of_issuance",
                "ghanacard_date_of_expiry"
            ]
        ]
    ]},
    {"dt": "Client Script", "filters": [
        [
            "name", "in", [
                "Employee-Form",
                "Vehicle-Form",
                "Leave Application-Form",
                "Leave Application-List"
            ]
        ]
    ]}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/erpnext_custom/css/erpnext_custom.css"
# app_include_js = "/assets/erpnext_custom/js/erpnext_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_custom/css/erpnext_custom.css"
# web_include_js = "/assets/erpnext_custom/js/erpnext_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_custom.install.before_install"
# after_install = "erpnext_custom.install.after_install"

# After migration
after_migrate = "erpnext_custom.app.company_name"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	},
#   "Department": {
# 	    "on_submit": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty",
# 	    "on_cancel": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "after_insert": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "before_rename": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "on_update": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "on_trash": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
#   },
    "Leave Application": {
 	    "on_submit": "erpnext_custom.server_scripts.leave_application.after_approval"
# 	    "on_cancel": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "after_insert": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "before_rename": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "on_update": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
# 	    "on_trash": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
   }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
# 	"all": [
# 		"erpnext_custom.tasks.all"
# 	],
 	"daily": [
 		"erpnext_custom.birthday_reminder.send_birthday_reminders"
 	],
# 	"hourly": [
# 		"erpnext_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_custom.tasks.monthly"
# 	]
}

# Testing
# -------

# before_tests = "erpnext_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnext_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

