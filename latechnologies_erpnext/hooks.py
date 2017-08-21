# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "latechnologies_erpnext"
app_title = "Latechnologies Erpnext"
app_publisher = "MN Technique"
app_description = "ERPNext extensions for LA Tech"
app_icon = "fa fa-desktop"
app_color = "grey"
app_email = "support@mntechnique.com"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/latechnologies_erpnext/css/latechnologies_erpnext.css"
# app_include_js = "/assets/latechnologies_erpnext/js/latechnologies_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/latechnologies_erpnext/css/latechnologies_erpnext.css"
# web_include_js = "/assets/latechnologies_erpnext/js/latechnologies_erpnext.js"

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

# Website user home page (by function)
# get_website_user_home_page = "latechnologies_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "latechnologies_erpnext.install.before_install"
# after_install = "latechnologies_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "latechnologies_erpnext.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"latechnologies_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"latechnologies_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"latechnologies_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"latechnologies_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"latechnologies_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "latechnologies_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "latechnologies_erpnext.event.get_events"
# }


fixtures = [
	{"dt": "Custom Field", "filters": [["name", "in", [
		"Opportunity-la_lead_details_sb",
		"Opportunity-la_estimated_closure_date",
		"Opportunity-la_estimated_closure_month",
		"Opportunity-la_estimated_total_value",
		"Opportunity-la_ps_benchmark",
		"Opportunity-la_total_no_of_endpoints",
		"Opportunity-la_cb",
		"Opportunity-la_total_no_of_branches",
		"Opportunity-la_conf_call_schedule",
		"Opportunity-la_domain_expert_ps",
		"Opportunity-la_technology_name",
		"Opportunity-la_oem_name"
	]]]}
]
