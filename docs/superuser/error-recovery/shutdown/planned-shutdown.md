---
title: "Planned Shutdown"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "HIM_shutdown_procedure.pdf"
  - "HIM_shutdown_and_open_procedure.pdf"
  - "ZEISS_Power_Outage_Procedure.pdf"
  - "Shutdown_procedure_scanned.pdf"
  - "Shutdown_and_Power_Up_NanoFab.jpg"
revision: "0.1"
---
# Planned Shutdown

> **WARNING**  
> Start preparation the day before Both the local procedure and ZEISS power-outage procedure require warming the GFIS before vacuum is compromised.

1. Stop/override LN₂ refill and start the warm-to-room-temperature process.

1. Set gas off; power down ET detector, flood gun and optional columns as applicable.

1. Ramp down/disable GFIS high-voltage supplies using the documented sequence.

1. Shut down turbo/ion/rough pumping and close the specified valves in sequence.

1. Power down racks, ZEN/System Manager, PCs and chase-rack supplies.

1. Shut down UPS/machine/dewar pump only at the documented final stage.

Use the detailed ZEISS Power Outage Procedure as the step-by-step controlled reference; local shutdown notes provide site-specific hardware cues.

## Logic review — source reconciliation required

> **WARNING — WAITING FOR MANUAL CONFIRMATION**  
> The ZEISS **Operator Manual does not contain the full planned facilities shutdown sequence**. It does confirm two important boundaries: the column isolation valve closes in Standby to isolate gun/column vacuum from the chamber, and the EMO is for an actual emergency rather than routine shutdown because abrupt power removal can lose data and may damage turbo pumps.  
> **Manual references:** Column Isolation Valve, printed p. **21** (PDF page **26**); Emergency Machine Off (EMO), printed p. **13** (PDF page **18**); Ending a Work Session §6.4, printed p. **141** (PDF page **146**).  
> **Waiting for confirmation:** use the separate ZEISS expected-power-outage procedure for the detailed sequence, then confirm which optional subsystems and site-specific valves/switches apply to this installed instrument.

