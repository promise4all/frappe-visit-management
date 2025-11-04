from __future__ import annotations

import frappe


def on_visit_validate(doc, method=None):
    # placeholder for CRM-related validations, tags or sync
    pass


def on_visit_update(doc, method=None):
    # placeholder for CRM activities logging
    pass


def on_visit_after_insert(doc, method=None):
    # placeholder for initial linkage or notifications
    pass


def on_visit_trash(doc, method=None):
    # placeholder for cleanup
    pass
