---
title: "Power-Up"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "HIM_shutdown_and_open_procedure.pdf"
  - "ZEISS_Power_Outage_Procedure.pdf"
  - "Shutdown_and_Power_Up_NanoFab.jpg"
revision: "0.1"
---
# Power-Up

Power-up is not simply the reverse of shutdown.

1. Verify facility CDA and N₂ are restored.

1. Restore Dewar pump, UPS and chase-rack supplies; allow self-checks.

1. Boot the NanoFab PC and start Athena/System Manager.

1. Verify Power Distribution, hardware communications and firmware Query results.

1. Start the vacuum system in the documented rough/pump sequence.

1. Restore optional subsystems only after their required vacuum conditions are met.

## Logic review — source reconciliation required

> **WARNING — WAITING FOR MANUAL CONFIRMATION**  
> The ZEISS **Operator Manual does not provide the complete facilities power-outage recovery sequence**; that sequence is in the separate ZEISS power-outage procedure. The Operator Manual can, however, supply post-recovery acceptance checks: GFIS column state **Pumped**, gun pressure **<1E-9 Torr**, gun temperature **73–85 K**, column pressure **<1E-8 Torr**, chamber state **Pumped** with chamber pressure **<3E-7 Torr**, and Dewar **Maintain Cool** with bottom temperature **<60 K**.  
> **Manual references:** ZEISS Operator Manual §5.1 Basic System Checks, printed p. **94** (PDF page **99**); gun/Dewar troubleshooting §7.4, printed pp. **157–165** (PDF **162–170**).  
> **Waiting for confirmation:** mark non-installed GaFIB/GIS/NPVE options N/A and confirm which of these manufacturer checks are the required local release checkpoints after the separate power-up/recovery procedure.

