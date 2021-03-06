# -*- coding: utf-8 -*-
# Copyright (c) 2020, Dirk van der Laarse and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class DiskUsageAlertSettings(Document):
	def validate(self):
		if self.usage > self.minimum:
			self.alert_state = 1
		else:
			self.alert_state = 0
