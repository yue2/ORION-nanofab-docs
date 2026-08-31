---
title: "Communication / Firmware"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
  - "HIM_trimer_form.pdf"
revision: "0.1"
---
# Communication / Firmware

## Symptom

Suspect a communication or firmware problem when a NanoFab module is **not communicating with the UI**, when its functions cannot be controlled, or when its readbacks stop updating. The Hardware Communication Status and Firmware Update/Query Nodes screens are used to identify the affected controller or node.

1. Open Service Machine → Hardware Communication Status and check for yellow/red modules.

1. Restart Athena/System Manager if required to re-establish module communication.

1. Open Firmware Update and use Query/Query Nodes; verify expected nodes return OK/green checks.

1. If a local recovery procedure calls for restarting ZEN/server/PC, record the action and re-check trimer before returning to users.
