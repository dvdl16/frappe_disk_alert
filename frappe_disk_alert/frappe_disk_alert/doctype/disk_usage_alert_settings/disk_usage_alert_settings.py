# -*- coding: utf-8 -*-
# Copyright (c) 2020, Dirk van der Laarse and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class DiskUsageAlertSettings(Document):
	def validate(self):
		if settings.usage > settings.minimum:
	        settings.alert_state = True
