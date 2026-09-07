---
title: "Communication / Firmware"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
  - "HIM_trimer_form.pdf"
revision: "0.2"
nav_previous: "Vacuum Problems"
nav_previous_path: "./superuser/error-recovery/troubleshooting/vacuum-problems.md"
nav_next_path: "./superuser/error-recovery/troubleshooting/trimer-problems.md"
nav_next: "Trimer Problems"
---
# Communication / Firmware

## Symptom

Suspect a communication problem when a NanoFab module is **not communicating with the UI** (no control response or no updated readbacks), when the chamber scope is frozen even though the stage movement motor can be heard, or when the imaging window is completely dark with no other explanation.

The **Hardware Communication Status** and **Firmware Update (Query Nodes)** screens identify the affected controller or node.

1. From the Athena System Manager menu, open **Tools → Service Machine → Hardware Communication Status**. Check for yellow/red modules and confirm the **green bidirectional arrows** next to every controller. A lost USB connection is the most likely cause.
2. Verify the affected controller is powered on and its communications cable is securely attached. If it is, shut down the ZEN UI and **STOP** the server in the Athena System Manager window.
3. Restart the PC to clear cache.
4. Open Athena and start the server. When it has started, open **Tools → Service Machine → Firmware Update** and click **Query Nodes**. Green check marks mean all nodes communicate.
6. If a node shows a red X:
   - **Unreachable – Could not ping node** → check power and cable; power-cycle the node; stop and restart the server; if still unreachable → contact the service representative.
   - **Incompatible firmware** → tick the box next to the red X and click **Download**; re-run Query Nodes; if the message persists → contact the service representative (ZEISS §7.3.2, printed p. 156 / PDF p. 161).
7. Finally, reopen **Hardware Communication Status** and confirm all indicators are green before resuming work.

> **Manual references:** ZEISS Operator Manual §7.3.1, printed pp. **153–154** (PDF **158–159**); §7.3.2, printed pp. **154–156** (PDF **159–161**); local restart sequence per HIM training notes, `HIM_trimer_form.pdf` p. 2.
