from __future__ import annotations

import frappe


@frappe.whitelist()
def get_visit_kpis(mode: str = "my", period: str = "month", user: str | None = None, overdue_within_period: bool = False):
    """Return KPI totals for Planned/In Progress/Completed/Overdue.

    This is a simplified placeholder implementation; replace queries as needed.
    """
    return {
        "planned": 0,
        "in_progress": 0,
        "completed": 0,
        "overdue": 0,
        "is_manager": frappe.has_permission(doctype="Visit", ptype="write"),
        "effective_mode": mode,
    }
