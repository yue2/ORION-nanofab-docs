---
title: "Planned Shutdown"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "HIM_shutdown_procedure.pdf"
  - "HIM_shutdown_and_open_procedure.pdf"
  - "ZEISS_Power_Outage_Procedure.pdf"
  - "Shutdown_procedure_scanned.pdf"
  - "Shutdown_and_Power_Up_NanoFab.jpg"
revision: "0.2"
nav_previous_path: "./superuser/error-recovery/shutdown/index.md"
nav_previous: "Planned Shutdown Index"
nav_next_path: "./superuser/error-recovery/shutdown/power-up.md"
nav_next: "Power-Up"
---
# Planned Shutdown

This guide is for a **planned** power outage. The EMO button is for actual emergencies, not routine shutdown — abrupt power removal can lose data and may damage turbo pumps.

> **WARNING**  
> **Start preparation the day before:** both the local procedure and the power-outage procedure require **warming the GFIS to room temperature** (Dewar heaters) before vacuum is compromised. Allow about **one hour** for the shutdown steps themselves on the day of planned power outage.

### Day before
1. **Ramp down the GFIS high voltages manually in ZEN** (this site runs ZEN Brisbane — required before warming). Use the GFIS column controls in the order: **Lens 2, Lens 1, Accelerator, Extractor**.
2. In Service Machine → GFIS **Column Maintenance**, select **Warm to Room Temperature** and click **Execute Now** — this finishes ramping down the high voltage and turns on the Dewar/column heaters. Note: the GFIS high voltages do **not** disable by themselves; rely on the interlock (or Service Machine → Power Distribution) once the gun warms.

### Day of shutdown
2. Save a stage label suitable for SFIM imaging / source maintenance (**blank metal**) and unload the sample.
3. From ZEN, place the GFIS column in **Standby**: gas (He/Ne) shuts off, the column isolation valve closes, and the column goes to **Pumped** (gun ion pump on). If any action does not happen, do it manually.
4. From ZEN Operation Center, power down the ET detector (and flood gun if used). **On ZEN Brisbane, also disable the Sample Bias manually** (it only powers down automatically with the detector from the Damascus release onward).
5. Exit the **NPVE** interface; power down the NPVE controller (white electronics box) and shut down the NPVE PC.
6. Stop/override the LN₂ auto-refill; **close the CDA and N₂ cylinder valves** and the Dewar jacket valve (site notes).
7. Vacuum shutdown (vacuum screen): tick **Diag**; turn off the **chamber turbo** and **gun turbo** (right-click green squares); **wait until the status reads "Off" (after "braking")**; close the chamber **foreline valve**, chamber **safety valve** (chamber rough pump off), gun **safety valve** (gun rough pump off), and the **Dewar rough valve**.
8. Service Machine → Power Distribution: **uncheck all boxes**. Exit ZEN; press **Stop** on Athena System Manager and wait for **"Server is shut down"**; shut down the NanoFab PC.
9. Chase rack: power off the four switches (**Evactron controller; two Duracomm switches; one Acopian switch**). Reset the chase-rack **EMO**, then switch off both **UPS circuit breakers**.
10. Stop the **Sogevac Dewar pump** (red Stop button) as the final step.

For a **brief outage (<20 min)**, the UPS keeps Lens 1/Extractor/Accelerator powered: isolate the chambers, power off ion/rough pumps, and restore power supplies when mains return (see the power-outage reference). Return-to-service steps are on the **Power-Up** page (next in the chain).

> **Manual references:** ORION NanoFab Power Outage Shutdown and Recovery Procedure (scanned), transcript `docs/information-base/shutdown_procedure_transcript.md`, pp. 1–4; ZEISS Power Outage Procedure (controlled reference).
> **Scope:** this tool has no GaFIB (Capella) or GIS option — the corresponding transcript sections are omitted. NPVE is installed and included.
