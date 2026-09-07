---
title: "Patterning"
access: all-users
category: user-guide
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-03
sources:
  - "Local_ORION_NanoFab_SOP.docx"
  - "SOP_ORION_NanoFab_He_Ne_Users.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
  - "NPVE User Guide.pdf"
  - "Setting up NPVE GIS control for the ORION Nanofab.pdf"
revision: "0.2"
nav_previous: "Imaging"
nav_previous_path: "./user-guide/imaging.md"
nav_next_path: "./user-guide/neon.md"
nav_next: "Working with Neon"
---
# Patterning

Use the ZEN patterning tab for simple patterns. If more advanced patterning is required, or if you want to use a saved pattern, use the NPVE PC.

## ZEN patterning

1. Focus on ROI before patterning.
2. Open the Patterning tab. Select a shape from the graphics window and draw the pattern. Selected shapes show a yellow contour in the imaging window.
3. In the left column of the software window, find Shape Properties. Set dose in ions/cm² and verify expected beam current.
4. Click start to start the pattern irradiation.

## NPVE

1. For complex patterns, use NPVE in the right hand side PC.
2. Verify the server/communication connection before starting the NPVE software
3. Click grab on NPVE to refresh the image.
4. Draw/import patterns, review parameters.
5. Select the intended patterns. Active shapes are in green.
6. Define the stop condition before starting: stop after a set time, dose, or repeats, or monitor with the endpoint image/graph.
7. Click start from the NPVE GUI to start patterning.
8. Save the current pattern in designated folder if you intend to repeat the pattern in the future.

For advanced pattern and dose details, see the NPVE User Guide transcript in the Information Base (Fibics v4.0, 2013). Note the installed NPVE is v4.6.2, so treat the guide as a concept reference and follow the installed GUI for exact controls.

> **NOTE**  
> Pattern depth depends on the material and on dose/beam current. Determine your stop condition (time, dose, repeats, or endpoint) before starting; use a Dose Array to calibrate milling depth for an unknown material.
