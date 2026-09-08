---
title: "Error & Recovery"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "HIM_shutdown_and_open_procedure.pdf"
  - "ZEISS_Power_Outage_Procedure.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
---
# Error & Recovery

Superuser procedures for **controlled shutdown/restart** and for recovering from **abnormal conditions**. Start from the page that matches the situation; each page gives a check order and its end-state/escalation. Do not improvise valve/pump or high-voltage sequencing — follow the cited procedures.

### Shutdown & Recovery
- **Planned Shutdown** — day-before GFIS warm-up, then the valve/pump/chase/UPS shutdown for a planned outage.
- **Power-Up** — facilities, electronics, vacuum pumpdown and release gates after power is restored.
- **GFIS Recovery** — the bake → anneal → trimer sequence after UHV loss.

### Troubleshooting
- **Main Chamber Vent** — intrusive recovery of a dropped/loose sample holder.
- **Gun Overheat** — recovery after LN₂ exhaustion (source bake-and-cool).
- **Vacuum Problems** — pressure/pump/valve faults in the gun/column, chamber, or Dewar.
- **Communication / Firmware** — controllers not communicating; Query Nodes and firmware checks.
- **Trimer Problems** — expected trimer not found or lost.
- **Image Problems** — no valid image: detector, beam, and alignment checks.
