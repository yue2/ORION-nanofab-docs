---
title: "GFIS Recovery"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "HIM_shutdown_and_open_procedure.pdf"
  - "ZEISS_Power_Outage_Procedure.pdf"
  - "HIM_trimer_form.pdf"
revision: "0.2"
nav_previous: "Power-Up"
nav_previous_path: "./superuser/error-recovery/shutdown/power-up.md"
---
# GFIS Recovery

Use this page after **GFIS gun/column vacuum (UHV) was lost** (full outage, chamber vent, or a vacuum event) and the column requires a **bake** before the source can be recovered. Vacuum restoration is covered on the **Power-Up** page; this page is the single home for the bake → anneal → trimer sequence.

> **WARNING**  
> **High voltage / restricted maintenance:** follow lockout and site electrical-safety requirements. The GFIS high voltages must remain disabled while cables are unplugged for the bake.

### Prepare
1. Verify the GFIS column state is **Pumped No Ion Pump**; home the **GFIS apertures**.
2. **Unplug the accelerator, extractor, and Lens 1 high-voltage cables** at the column and **wrap the cables in clean Al foil** for the bake (HIM open procedure, p. 4).
3. Confirm the LN₂ supply is connected and adequate — tank pressure ~**1.5 bar** and the tank valve open — so the Dewar refills after the bake.

### Bake
4. In Service Machine → GFIS **Column Maintenance**, select **Warm, Bake and Get Cold** and set the hours to bake. **At this site 72 h is sufficient** (the ZEISS standard recommendation is 100 h — Tool-Owner-approved local value). Click **Execute Now** and leave it to complete.
5. After the bake completes, **reconnect the high-voltage cables** (remove the Al foil).
6. Verify the GFIS state is **Pumped** (GFIS ion pump on) and the **gun pressure reaches ~1e-10 T** — the threshold that allows helium flow for trimer formation. If the pressure does not recover, do not proceed — escalate (degas/cryosurface regeneration per the gun-overheat page, then service if it still fails).

### Source recovery
7. In Service Machine → Power Distribution → Power Supplies, **enable the four GFIS high-voltage elements**.
8. Load a **blank-metal** sample suitable for SFIM and drive the stage to the saved SFIM stage label.
9. From ZEN GFIS Column Maintenance, perform the **Light Anneal**, then the **Maintain BIV** source build (recommended recovery after the bake — outage transcript p. 6).
10. Continue with trimer formation and column alignments in the normal manner (see [Trimer Formation](../../maintenance/trimer-formation.md)); if a trimer cannot be formed even at very high extraction, use the **decrease BIV** source build and record the BIV for the next formation.
