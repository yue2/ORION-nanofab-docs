---
title: "Main Chamber Vent"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "HIM_main_chamber_vent.pdf"
revision: "0.2"
nav_previous: "Troubleshooting"
nav_previous_path: "./superuser/error-recovery/troubleshooting/index.md"
nav_next_path: "./superuser/error-recovery/troubleshooting/gun-overheat.md"
nav_next: "Gun Overheat"
---
# Main Chamber Vent

## Symptom

Sample falls from the stage. Stage is not secured and the transfer rod is retracted so the sample stage is left tilted in the main chamber. Thus, an intrusive chamber recovery is required, such as retrieving a sample holder that cannot be recovered through the normal air-lock transfer path.

> **WARNING**  
> **Intrusive recovery:** this procedure opens the process chamber and risks contact with the ET detector filament/source region.

> **WARNING**  
> **Access policy:** if this main-chamber vent was caused by mishandling of the transfer procedure (e.g., retracting the rod before confirming the holder is secured, or an unsecured/tilted sample stage), it counts as **one unauthorized operation** under the local access policy. Accumulating a second unauthorized operation results in suspension of tool access and a new round of training. This is one of the most common mishaps — always report it honestly to a Superuser and follow the recovery steps above.


### Vent
1. Confirm the GFIS column is in **Standby** and the gun/column isolation valve (CIV) is closed (check vacuum screen).
2. From the air lock, click **Transfer** to keep the transfer door open; make sure the transfer rod is fully retracted.
3. In the vacuum screen (Dewar tab), close the Dewar jacket valve.
4. Right-click **Main Chamber → Vent**. Wait until the main chamber and loading dock are vented to **≥ 1000 Torr**.
5. Turn off table stabilization (air table) in the vacuum screen.

### Retrieve the holder
6. Using a hex spanner from the cabinet drawer, unscrew the chamber door screws on the **service side** and place them on a **clean tissue**; open the door carefully without pinching cables.
7. Retrieve the holder without touching the ET detector filament or source tip. Keep the sample stage outside.
8. Close and re-seal: hand-tighten the screws first, then tighten a few rounds with a screwdriver — **do not over-tighten**.

### Restore
9. Return the stage through the loading chamber; **hold the loading door** while inserting it, since all chambers are vented.
10. Pump the main chamber from the vacuum screen (right-click **Main Chamber → Pump**). The loading door closes automatically when the chamber reaches ~1e-2 torr.
11. **Confirm the loading door is closed**, then restore table stabilization (Air Lock and Chamber tab). Leave the chamber to pump overnight — it should reach the ~1e-8 torr range by the next day.
12. The next day, check the main-chamber vacuum (~1e-8 torr after the overnight pump) and the gun pressure (should be unaffected, normal ~1E-10 torr range); verify the ion source/trimer on the Au standard sample.
13. Schedule a **Chamber Cleaning** from ZEN: **Maintenance → System → Chamber Cleaning**. Select **Mild** or **Moderate** intensity for 1–2 hours, with the start time outside office hours; verify completion afterwards.
14. If the trimer was lost due to vacuum fluctuation, form a new trimer (see [Trimer Formation](../../maintenance/trimer-formation.md)).
