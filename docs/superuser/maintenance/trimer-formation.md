---
title: "Trimer Formation"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-03
sources:
  - "HIM_trimer_form.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.2"
nav_previous: "Gas Cylinders"
nav_previous_path: "./superuser/maintenance/gas-cylinders.md"
---
# Trimer Formation

The trimer is a tungsten tip sharpened to an apex of **three atoms**. Helium is ionized on one apex atom to form the beam; after continued electrical stress that atom eventually "pops" — at this site roughly every 1–2 months — so the tip must be re-formed and a new trimer selected. The remaining dimer can still image, but is markedly less stable: if the tip is in the dimer state, the tool may be used but a new trimer formation should be scheduled promptly.

> **WARNING**  
> Trimer formation applies kilovolt-level extractor/accelerator voltages and mechanical gun-head movement. Follow the wizard exactly; if the source shows no organized pyramid, or no trimer appears by ≈ −50 kV, stop and run the ion-beam checks (ZEISS §7.6.3) before continuing. Do not guess — contact a Superuser/Service Engineer.

## Prepare
1. Move the stage to the standard Au sample; power on the ET detector; adjust ET detector to default values (30% - 50% for brightness and contrast); put the GFIS column in **Standby**. In SFIM: spot control **4.0**, FOV start **1**, dwell **2 µs** .
2. ZEN top menu bar **Maintenance → GFIS → GFIS Source Maintenance**. The wizard opens on the **Process Selection** list.

## Form the source
3. Select **Form the source**. Keep the defaults **Maintain BIV Source Build** and **Keep most recent field**. Click **Begin**: gas is first turned off (evacuation can take up to ~5 min), voltages ramp down, then the tip is heated and re-shaped (recipe ~20 min total — HIM slide p. 1). Completion shows **State: Form Completed / SUCCEEDED**.
4. Click **Next** to enter **Form a Trimer**. SFIM imaging starts, the aperture is set to **Big Hole** automatically, gas restarts, and the column pressure reaches ~1e-6 torr.

## Form a trimer
5. With extraction below ionization, set the accelerator to **20–25 kV** and lens 1 to ~**80% of the accelerator** (≈16–20 kV). Slowly increase the extraction field (more negative) until a bright spot appears in imaging — typically **−20 to −25 kV**.
6. Increase the extraction to ≈ **−32 kV**, then raise the accelerator to **30 kV** and adjust lens 1 to go over the focus crossover, continue to increase lens 1 voltage to spread the signal until emission from **individual atoms** is visible; raise extraction further to peel atoms, adjusting contrast to avoid saturation.
7. Continue until the organized **pyramid/trimer** forms — expected roughly −40 to −45 kV. If the structure is disorganized, repeat **Form the source**. If **no trimer appears by ≈ −50 kV**, stop and check for an ion beam (ZEISS §7.6.3, printed p. 111 / PDF p. 116).
8. **As soon as the three-atom structure is in sight, reduce the extraction to ≈ −35 kV** to avoid evaporating the trimer. Stop the scan, click **Done**, then **Next**.
9. If formation fails with a "hollow center," click **Finish**, then re-run the build from Form the Source keeping **Maintain BIV**. If the build still does not produce a usable source, choose the **increase BIV** option for the next build. If no trimer forms even at very high extraction, re-run the build choosing **decrease BIV** and record the BIV number at the next trimer formation.

> **NOTE** — Repair the Source (e.g., post-overheat degas/recovery) is a separate Service/Tool-Owner workflow (ZEISS §5.2.2); it is not part of this routine trimer formation procedure. See the gun-overheat recovery page if an overheat occurred.


## Determine BIV
10. With the trimer live, click **Show All**, then in the **Graphics** tab draw a circle around the trimer and enable **M** (measure). Tune the extractor up and down for the **maximum mean intensity** (the last logged site value was ≈ −32.5 kV — consult the log book） Round to the nearest 500 V, enter it, and click **Set BIV**. Click **Next**.

### Align the source
11. **Tilt alignment:** adjust lens 1 to **crossover**, then note the above- and below-crossover lens-1 values and use **Back** to toggle between them. Check **Enable air bearing**, draw a circle around the atom to align (brightest recommended), and use **Gun Tilt** virtual joystick iteratively until the atom sits in the circle in both views. Uncheck **Enable air bearing**.
12. **Shift alignment:** select **Shift Alignment**, choose a previously aligned aperture, zoom the trimer, and use the **physical gun shift knobs** on the machine column to center the atom on the cross-hairs; back the knobs off slightly to remove tension.

## Set source distance and finish
13. Click **Next → Set source distance**. The software selects Big Hole; adjust **lens 1** for the sharpest aperture edge, select fine and tracking for lens 1 to allow fine tuning. Then adjust **Source Distance** until the **Crossover Position reads ≈ −104.0 mm**. Click **Done** and **Finish**.
14. Return to the ZEN imaging tab. In SFIM, grab an image of the new trimer, capture a final screenshot, and record the BIV/maintenance details.
