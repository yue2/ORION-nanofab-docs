---
title: "Vacuum Problems"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
  - "HIM_main_chamber_vent.pdf"
revision: "0.1"
---
# Vacuum Problems

## Symptom

Use this page when the gun/column, chamber, or Dewar does not reach or maintain its expected vacuum state or pressure, when a pump/valve state is abnormal, or when a vacuum module remains in an unexpected state. The affected region should be identified before any corrective action is attempted.

The ZEISS manual separates gun/column, chamber and Dewar vacuum regions. Use the Vacuum Dashboard to diagnose state, pressure, valves and pumps.

> **NOTE**  
> Normal users The manufacturer describes the Vacuum Dashboard as useful for observation during normal operation; Superusers use diagnostic controls only under the approved procedure.

## Logic review — incomplete curated procedure

> **WARNING — WAITING FOR MANUAL CONFIRMATION**  
> **ZEISS manual guidance to confirm locally:** start with the Basic System Checks (gun **<1E-9 Torr**, column **<1E-8 Torr**, chamber **<3E-7 Torr**, Dewar Maintain Cool). Use normal state-machine commands rather than Diagnostic mode; the manual warns that Diag gives individual valve/pump control and should only be used by a trained engineer or under ZEISS instruction. For gun/column faults, §7.4.6 provides Pump-state checks; for Dewar faults, §7.4.5 checks contents pressure, rough valve and rough pump before service escalation.  
> **Manual references:** §5.1 printed p. **94** (PDF **99**); Vacuum Dashboard §7.1, printed pp. **144–150** (PDF **149–155**); Dewar Issues §7.4.5, printed pp. **161–164** (PDF **166–169**); Gun/Column Pressure §7.4.6, printed pp. **165–166** (PDF **170–171**).  
> **Waiting for confirmation:** define the site's stop-work thresholds and explicitly list which state-machine actions are authorized for superusers. Keep Diag-mode actions outside the local procedure unless separately authorized.

