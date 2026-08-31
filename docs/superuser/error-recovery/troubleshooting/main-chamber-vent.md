---
title: "Main Chamber Vent"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "HIM_main_chamber_vent.pdf"
revision: "0.1"
---
# Main Chamber Vent

## Symptom

> **WARNING — WAITING FOR MANUAL CONFIRMATION**  
> The local source documents the chamber-vent recovery steps but does **not clearly state the initiating symptom**. The procedure appears intended for an intrusive chamber recovery such as retrieving a sample holder that cannot be recovered through the normal air-lock transfer path. Confirm the approved site-specific trigger before treating this as the authoritative symptom description.

> **WARNING**  
> Intrusive recovery This procedure opens the process chamber and risks contact with the ET detector filament/source region.

1. Keep the transfer door open as documented.

1. Close the Dewar jacket valve; command Main Chamber → Vent.

1. Wait until main chamber and loading dock are vented.

1. Turn off table stabilization and open the chamber from the service side.

1. Retrieve the holder without touching the ET detector filament or source tip.

1. Close/reseal the chamber, pump down, restore stabilization and pump overnight.

1. Check vacuum and ion source the next day.

## Logic review — unresolved source gaps

> **WARNING — WAITING FOR MANUAL CONFIRMATION**  
> **ZEISS manual guidance to confirm locally:** the column isolation valve is specifically intended to isolate the gun/column vacuum from the chamber so the chamber can be vented for service, and it is closed when the GFIS column is in Standby. For return-to-service screening, the manufacturer's Basic System Checks specify GFIS state **Pumped**, gun pressure **<1E-9 Torr**, gun temperature **73–85 K**, column pressure **<1E-8 Torr**, chamber state **Pumped** with chamber pressure **<3E-7 Torr**, and Dewar **Maintain Cool** with bottom temperature **<60 K**.  
> **Manual references:** Column Isolation Valve, printed p. **21** (PDF page **26**); §5.1 Basic System Checks, printed p. **94** (PDF **99**); Vacuum Dashboard state-machine cautions §7.1, printed pp. **144–147** (PDF **149–152**).  
> **Waiting for confirmation:** confirm the exact pre-vent sequence for this site (including column/ET detector/interlock state) and whether the Basic System Check limits plus any additional overnight-pump criteria are sufficient for local return to service.

