---
title: "Power-Up"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "HIM_shutdown_and_open_procedure.pdf"
  - "ZEISS_Power_Outage_Procedure.pdf"
  - "Shutdown_and_Power_Up_NanoFab.jpg"
revision: "0.2"
nav_previous: "Planned Shutdown"
nav_previous_path: "./superuser/error-recovery/shutdown/planned-shutdown.md"
nav_next_path: "./superuser/error-recovery/shutdown/gfis-recovery.md"
nav_next: "GFIS Recovery"
---
# Power-Up

Power-up is **not** simply the reverse of shutdown. This sequence follows the local scanned power-outage procedure. 

### Facilities and electronics
1. Verify the facility **CDA and N₂** are restored and at the desired pressures.
2. Unlock the chase-rack **EMO**; switch the **Sogevac Dewar pump** on (Start). Set both **UPS circuit breakers** to ON and allow the self-check (~1 min) until the display reads **"ONLINE MODE"**.
3. Switch on the four chase-rack supplies (**Evactron controller; two Duracomm switches; one Acopian switch**) — the Acopian power light will not illuminate yet.
4. Power on the NanoFab PC and let it boot; log in, open and start **Athena System Manager**, and wait for **"The server has started."**
5. Verify the **Power Distribution** page restarted: the boxes unchecked during shutdown should now be checked (normally only **Dewar Bake** remains unchecked); if not, check every right-side box except Dewar Bake.
6. Wait **~5 minutes** for the boards to boot; open **Hardware Communications Status** and verify all modules are talking (no yellow/red); restart Athena if needed. Run **Firmware Update → Query** — all green (see Communication / Firmware).
7. Open the vacuum screen from Athena and start the ZEN UI.

### Vacuum pumpdown
8. In the Dewar tab, verify the Dewar state is **Idle** (prevents auto-fill until the jacket valve is opened later).
9. Confirm the rough pump is running; let it run ~**5 minutes**.
10. Right-click the **GFIS Column** state → **Pump No Ion Pump**: valves cycle and the gun turbo spins up; the GFIS ion pump stays off.
11. When the **gun pressure is below ~1e-4 torr**, open the **column manual valve** (back of the machine, beside the stabilizing module).
12. Select **Pump** for the chamber; when the chamber reaches rough vacuum, open the **Dewar jacket valve** (Dewar tab).
13. Wait ~**10 minutes** until both the column and chamber read pumped; confirm the chamber turbo spins to **Ready**.
14. Leave the ion pumps off ~**2 hours** (better: overnight), watching the pressure trends.
15. When the **gun pressure is better than ~1e-6 torr**, turn on the two ion pumps and confirm the pressure keeps decreasing.
16. Confirm LN₂ supply is adequate (tank pressure ~**1.5 bar**) so the Dewar can fill.
17. **Home the stage**, then power up the ET detector (Operation Center); on ZEN Brisbane, enable the sample bias separately when needed.
18. After a full outage, continue to the **GFIS Recovery** page (next in this chain) for the bake → anneal → trimer sequence; do not attempt the gun-pressure release gates until that recovery completes.

### NPVE 
19. Power up the **NPVE controller box** and wait ~1 minute, then power up the NPVE PC.
20. On the **NanoFab PC** (not the NPVE PC), start the **Zeiss Fibics Server** (FibicsZeissServer.exe under `Program Files (x86)\Fibics\Server`).
29. Log in and start the NPVE user interface.


### Acceptance (pre-bake)
Confirm the states reached by this pumpdown sequence: chamber **Pumped**, chamber pressure **<3E-7 Torr**, Dewar in **Maintain Cool** with bottom **<60 K**, column valve open, ion pumps running, and gun pressure trending below ~1e-6 torr. The full ZEISS §5.1 gun/column gates — GFIS **Pumped**, gun **<1E-9 Torr**, column **<1E-8 Torr** — are confirmed **after** the GFIS bake (see GFIS Recovery); note the site-specific gun-temperature readback of **92–95 K** (thermocouple deviation), not the manual's 73–85 K.

> **Manual references:** vacuum restoration per `HIM_shutdown_and_open_procedure.pdf`, "Turning on," pp. 2–4 (site sequence); rack/boot sequence per the scanned outage transcript, p. 5.
