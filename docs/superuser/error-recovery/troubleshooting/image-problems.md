---
title: "Image Problems"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-07
sources:
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
nav_previous: "Trimer Problems"
nav_previous_path: "./superuser/error-recovery/troubleshooting/trimer-problems.md"
---
# Image Problems

## Symptom

Use this page when the instrument is **scanning but no valid image** appears, or when the displayed signal does not respond as expected. The ZEISS sequence distinguishes: detector/noise problems, secondary electrons not reaching the ET detector, and no ion beam present.

## Diagnostic checklist

1. **Imaging gas and gun pressure** — confirm the imaging gas is on and the gun pressure reaches its set point (2E-6 torr for He gas).
2. **Aperture** — confirm the gas-appropriate aperture is selected; if no image appears, select **Big Hole**.
3. **Sample** — verify a suitable sample (standard Au) is under the beam.
4. **Scanning** — verify continuous scanning is running and the beam is not blanked.
5. **ET detector** — confirm it is powered up with brightness/contrast in the usual 30–50% range; if detector/noise is suspected, follow the ZEISS ET-detector checks.
6. **Beam/trimer present** — if the panel is dark with only scattered bright points, or no trimer is visible in SFIM, follow the trimer checks and, if needed, form a new trimer (see Trimer Problems; Trimer Formation).
7. **High-voltage supplies** — if no beam, confirm Accelerator, Extractor, Lens 1 and Lens 2 are enabled (see Gun Overheat if a bake/recovery occurred).
8. **Alignment drift** — if an image exists but is poor, re-check focus/stigmation, Gun Shift and trimer alignment rather than rebuilding the source.

## Related pages

- **Trimer Problems** / **Trimer Formation** — dark panel with no trimer; new source/trimer build and the decrease-BIV recovery.
- **Communication / Firmware** — dark panel from lost controller communication.
- **Gun Overheat** — HV-supply or bake/recovery history.
- **Vacuum Problems** — gas or gun vacuum out of range.
- **User Guide: Imaging / Starting a Session** — normal configuration baseline.

> **Manual reference:** ZEISS Operator Manual §7.6 Image Issues (printed pp. 167 ff. / PDF pp. 172 ff.), especially Basic Image Configuration §7.6.1 and Checking for an Ion Beam §7.6.3.
