---
title: "Image Problems"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
---
# Image Problems

## Symptom

Use this page when the instrument is scanning but there is **no valid image**, or when the displayed signal does not respond as expected. The ZEISS troubleshooting sequence distinguishes detector/noise problems from cases where secondary electrons are not reaching the ET detector or no ion beam is present.

Check the basic image configuration, ET detector, beam presence, focus/stigmation, Gun Shift and trimer alignment. The ZEISS manual contains dedicated troubleshooting sections for image configuration, ET detector and checking for an ion beam.

## Logic review — incomplete curated procedure

> **WARNING — WAITING FOR MANUAL CONFIRMATION**  
> **ZEISS manual diagnostic order for a no-image condition:** verify imaging gas is on and gun pressure reaches set point; select **Big Hole**; verify **Autoblanking**; verify a suitable sample is under the beam; verify scanning is running; then check the ET detector. If configuration and detector checks pass, verify a trimer/beam is present and verify Accelerator, Extractor, Lens 1 and Lens 2 supplies are enabled. The manual directs service escalation when these checks do not resolve the fault.  
> **Manual references:** §7.6 Image Issues, printed pp. **167–173** (PDF pages **172–178**); Basic Image Configuration §7.6.1, printed pp. **167–169**; ET Detector §7.6.2, printed pp. **169–172**; Ion Beam §7.6.3, printed pp. **172–173**.  
> **Waiting for confirmation:** confirm which checks local superusers are authorized to perform and add site-specific branches for poor contrast, charging, focus/astigmatism and escalation.

