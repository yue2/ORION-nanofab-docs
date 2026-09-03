---
title: "Routine Checks"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-03
sources:
  - "HIM_superuser_maintenance.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
nav_previous: "Maintenance"
nav_previous_path: "./superuser/maintenance/index.md"
nav_next_path: "./superuser/maintenance/ln2-system.md"
nav_next: "LN₂ System"
---
# Routine Checks

Maintain a log of base pressures, gun temperature and Dewar pressure to spot drift early; the ZEISS manual notes this data can serve as an early warning of problems and helps service personnel. The site logs **weekly**.

Compare each reading against the normal ranges:

- GFIS column **Pumped**; gun pressure **in E-10 Torr range**
- Gun temperature **92–95 K** This instrument's gun-temperature readback runs **92–95 K** in normal operation because of the thermocouple mounting, higher than the ZEISS §5.1 range of **73–85 K**. Use **92–95 K** as the local normal band; treat a reading above ~95 K sustained outside a Dewar fill as the relevant flag, not the manual's 85 K value.
- Mid-column pressure **<1E-8 Torr**
- Chamber **Pumped**; chamber pressure **<3E-7 Torr**
- Dewar **Maintain Cool**; Dewar bottom temperature **<60 K**

1. Review previous log entries and alerts before starting.
2. Record gun, mid-column and chamber base pressures (pre gas-on, as per ZEISS §6.1.1). Flag any reading outside the ranges above.
3. Record gun temperature and Dewar bottom pressure; confirm the Dewar is in Maintain Cool.
4. Inspect gas pressure: CDA and LN₂ status. Order CDA/N₂ cylinders in advance when the cylinder pressure falls below 200 psi — deliveries are Mon/Wed/Fri (see [Gas Cylinders](./gas-cylinders.md)); plan the external LN₂ tank refill ~16 days after the last one (see [LN₂ System](./ln2-system.md)).
5. Verify the trimer is present and the beam behaves normally, and that the controllers show green communication arrows — do this after any error/alarm or when a session behaves oddly (see [Trimer Problems](../error-recovery/troubleshooting/trimer-problems.md), [Communication / Firmware](../error-recovery/troubleshooting/communication-firmware.md)).
