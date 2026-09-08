---
title: "Gun Overheat"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-08
sources:
  - "HIM_overheat.pdf"
revision: "0.2"
nav_previous: "Main Chamber Vent"
nav_previous_path: "./superuser/error-recovery/troubleshooting/main-chamber-vent.md"
nav_next_path: "./superuser/error-recovery/troubleshooting/vacuum-problems.md"
nav_next: "Vacuum Problems"
---
# Gun Overheat

## Symptom

Sustained gun temperature above ~95 K **outside** an LN₂ auto-fill (site readback normal is 92–95 K; a brief rise toward ~95–100 K during the scheduled fill is expected and should recover within about an hour).

## Possible causes

- **LN₂ supply exhausted** (main tank depleted before the next delivery).
- **Dewar not being pumped / auto-fill interrupted** (check Dewar status first — see LN₂ System).
- **Transient Dewar-fill rise** — no action needed; confirm it recovers after the refill.

## What to do

### Transient refill rise (scheduled 8 am / 8 pm fills)
1. Do not start GFIS during the fill window (roughly 06:00–08:30). If the gun is already up and the temperature rises during a fill, put the GFIS to standby and wait; it should return to normal within ~1 hour.

### LN₂ exhausted — source bake-and-cool recovery

> **NOTE** — This is the overheat-recovery bake (Source Repair → **bake and cool**), distinct from the full-outage GFIS bake (`GFIS Recovery`: **Warm, Bake and Get Cold**, HV cables unplugged and wrapped, 72 h).

2. Confirm the Dewar/main tank state (see [LN₂ System](../../maintenance/ln2-system.md)). If the tank is depleted and the next delivery hasn't arrived, a source-repair (bake) procedure is required.
3. In Service Machine → Power Distribution, disable **accelerator, Lens 1 and extractor**.
4. Physically isolate the documented HVP connections: unscrew the cable guards and disconnect the feedthroughs; **cover the disconnected cable ends with gloves**. Follow lockout/site electrical safety requirements — this is restricted high-voltage work.
5. When LN₂ is delivered, connect the heating cable from the back of the tool.
6. In Service Machine → Source Repair, choose the **bake and cool** process; enter a bake time of **48 h or 72 h** and start it immediately.
7. Put up a notice at the keyboard and message all users: **no one may use the tool during source maintenance**. Wait until the heating procedure starts successfully, then leave it to bake and cool.
8. After completion, check the gun pressure — it should be in the normal ~1e-10 torr range. If 2 days after a successful bake-and-cool the pressure is still high, run **degas** from source repair, then a **cryosurface regeneration**; if it still does not recover, contact the service representative.
9. When the gun pressure is back to normal, reconnect the high-voltage cables and remove the heating cable.
10. Perform a new trimer formation (see [Trimer Formation](../../maintenance/trimer-formation.md)). If a trimer cannot be formed even at very high extraction, choose the **decrease BIV** source build at the Form-the-Source stage and **record the BIV at the next trimer formation**.

> **WARNING**  
> **High voltage:** this is restricted maintenance. Follow lockout/site electrical safety requirements.
