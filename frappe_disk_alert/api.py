import frappe
from frappe import _
import shutil

@frappe.whitelist()
def update_disk_usage():
    """
    Checks the OS Disk Usage and saves the values
    """
    total, used, free = shutil.disk_usage("/")
    settings = frappe.get_single("Disk Usage Alert Settings")
    settings.total = "%d GiB" % (total // (2**30))
    settings.used = "%d GiB" % (used // (2**30))
    settings.free = "%d GiB" % (free // (2**30))
    settings.usage = round(used/total * 100,2)
    settings.save()
