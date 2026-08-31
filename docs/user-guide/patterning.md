---
title: "Patterning"
access: all-users
category: user-guide
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "Local_ORION_NanoFab_SOP.docx"
  - "SOP_ORION_NanoFab_He_Ne_Users.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
---
# Patterning

1. Open the Patterning tab and focus before patterning.

1. Set dose in ions/cm² and verify expected beam current.

1. Use the local SOP values appropriate to He or Ne and the intended process.

1. For complex patterns, use NPVE; verify the server/communication connection before starting.

1. Draw/import patterns, review parameters, select the intended patterns and start from the NPVE GUI.

> **NOTE**  
> Source note The local SOP records example process values; treat them as local working notes, not universal defaults.

## Logic review — item requiring confirmation

> **WARNING — WAITING FOR MANUAL CONFIRMATION**  
> **ZEISS manual parameters to confirm for the local checklist:** acceleration voltage/ion species, aperture and Spot Control (beam current/diameter), dwell time and passes/repeats, beam overlap, scan direction, ion dose/fluence, and material-specific volume-per-dose/dose-array information. The NPVE workflow then calls for aperture selection, acceleration voltage, HIM alignment, gas selection, image capture, drawing patterns, setting pattern parameters, defining the stop criterion, and starting the pattern.  
> **Manual references:** §12.1.1 Patterning Parameters, printed pp. **233–237** (PDF pages **238–242**); §12.2 Patterning Basics Using NPVE and §12.2.1 Patterning Process, printed p. **238** onward (PDF **243** onward).  
> **Waiting for confirmation:** decide which of these fields are mandatory in the local He/Ne patterning checklist and which values are application-specific rather than fixed defaults.

