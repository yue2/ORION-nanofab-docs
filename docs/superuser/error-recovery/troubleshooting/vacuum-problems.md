---
title: "Vacuum Problems"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
  - "HIM_main_chamber_vent.pdf"
revision: "0.2"
nav_previous: "Gun Overheat"
nav_previous_path: "./superuser/error-recovery/troubleshooting/gun-overheat.md"
nav_next_path: "./superuser/error-recovery/troubleshooting/communication-firmware.md"
nav_next: "Communication / Firmware"
---
# Vacuum Problems

## Symptom

Use this page when the gun/column, chamber, or Dewar does not reach or maintain its expected vacuum state or pressure, when a pump/valve state is abnormal, or when a vacuum module stays in an unexpected state. **Identify the affected region first**, then apply the checks below.

Start from the Basic System Checks: gun **~1E-10 Torr**, column **<1E-8 Torr**, chamber **<5E-7 Torr**, Dewar in **Maintain Cool**. Use the Vacuum Dashboard to read state, pressure, valves and pumps (ZEISS §7.1, printed pp. 144–147 / PDF pp. 149–152).

### Gun / column region
1. Check the gas cylinders and CDA/N₂ supply pressures (see [Gas Cylinders](../../maintenance/gas-cylinders.md)); low or absent gas supply can hold the column in an abnormal state.
2. Check the ion pumps: if off, check their high-voltage supplies on the back rack of the tool, behind the column. If the state does not recover, follow the gun/column pump-state checks.

### Chamber region
3. Check the rough pump(s) in the backroom. If the chamber rough pump is off, restart it. Confirm the turbo pump spins up to speed.
4. If the main-chamber vacuum is **persistently** higher than normal, review the usage logs for previously loaded samples. **No volatile substance is allowed in this tool** — advise users during training, especially about organic samples. Loading an inappropriate volatile/organic sample counts as **one unapproved use**; do not use the tool if volatile organic residues are suspected (high-voltage arcing can severely damage electronics).
5. If inappropriate samples were loaded, a **moderate** chamber cleaning should restore the main-chamber vacuum.

### Dewar region
6. Check the Dewar state and auto-fill; the Dewar **rotary** (rough) pump is in the backroom. If the rough pump is off, restart it; confirm the Dewar returns to Maintain Cool and LN₂ supply is adequate (see [LN₂ System](../../maintenance/ln2-system.md); Dewar issues per ZEISS §7.4.5, printed pp. 161–164 / PDF pp. 166–169).

If the vacuum does not recover after the above, contact the service representative.

> **NOTE**  
> **Normal users:** the manufacturer describes the Vacuum Dashboard as useful for observation during normal operation. Superusers use diagnostic/state-machine controls only under the approved procedure; do not use **Diagnostic mode** outside the approved steps.

> **Related pages:** Communication / Firmware (dashboard/readback faults), Gun Overheat (bake/recovery aftermath), Image Problems (symptom cross-checks), Trimer Formation (post-recovery trimer check).
