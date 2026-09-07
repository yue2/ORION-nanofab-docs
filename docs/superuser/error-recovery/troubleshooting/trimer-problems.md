---
title: "Trimer Problems"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "HIM_trimer_form.pdf"
  - "HIM_overheat.pdf"
revision: "0.2"
nav_previous: "Communication / Firmware"
nav_previous_path: "./superuser/error-recovery/troubleshooting/communication-firmware.md"
nav_next_path: "./superuser/error-recovery/troubleshooting/image-problems.md"
nav_next: "Image Problems"
---
# Trimer Problems

## Symptom

Use this page when the expected **three-atom trimer cannot be found** while imaging the conductive standard Au sample in SFIM, or when source emission is visible but no usable trimer is available.

Trimer loss can result from **aging** (the apex atom pops, typically after ~1–2 months), **gun overheat**, an **extractor high-voltage trip**, or **loss of gun vacuum**.

## Check in order

1. **Dark image panel?** If you are on the Au surface in SFIM mode but the panel is dark, first confirm the ET detector is powered up and brightness/contrast are in the usual 30–50% range.
2. **Still completely dark?** The most likely cause is lost hardware communication — check the Hardware Communication Status and restart ZEN/server/PC if needed (see Communication / Firmware). Re-check the trimer once communication is restored.
3. **Scattered bright points that refresh on Grab, or no trimer visible once communication is normal?** A new trimer formation is required (see Trimer Formation, `../../maintenance/trimer-formation.md`). Minimize SFIM exposure: confirm the structure only when necessary, on the standard Au sample / saved reference site, following the last recorded trimer atom from the logbook when available.
4. **Cannot form a trimer even at very high extractor?** Use the **decrease BIV** source build at the Form-the-Source stage and record the BIV at the next formation (HIM overheat notes, p. 3).

> **WARNING**  
> **Do not expose the source unnecessarily:** use the standard conducting Au sample and minimize SFIM exposure.

## Related pages

- **Communication / Firmware** — dark panel caused by lost communication.
- **Gun Overheat** — overheat triggered a bake/recovery.
- **Vacuum Problems** — gun vacuum was lost.
- **Trimer Formation** — full formation procedure, including the decrease-BIV recovery.
