---
title: "Starting a Session"
access: all-users
category: user-guide
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "Local_ORION_NanoFab_SOP.docx"
  - "SOP_ORION_NanoFab_He_Ne_Users.pdf"
revision: "0.1"
nav_previous: "Starting a Session"
nav_previous_path: "./user-guide/starting-session.md"
nav_next_path: "./user-guide/imaging.md"
nav_next: "Imaging"
---
# Starting a Session

After loading the samples, wait for the main chamber pressure to go below 5e-7 torr then start your experiments. The following operations will be performed in ZEN software unless otherwise stated.

## Power up

1. In ZEN software, enter the imaging tab on top of the left column. This is the default function mode. 
2. From the left column, find Sample List. Select 'Std Au', click 'go to' at the right bottom corner of the Sample List window to go to the standard gold sample. **Take note of the movement in the chamber scope. Click stop immediately when the tallest point of your sample is within 2 mm of the detector.**
3. From the top menu bar, click Operation Center to open the Operation Center window. Power on the ET detector. From the left column, find ET Detector tab, set brightness and contrast to 30% - 50% each.
4. GFIS power should be in mixed state. Flood gun will be powered up only when needed.
5. Check the left bottom row of the software for the current status. Make sure the imaging mode is in Normal Imaging. If not, click the SFIM/Normal button on keyboard to switch.
6. From the left column, find GFIS settings, click 'Show all' to expand the options. 
    1. Confirm the appropriate aperture (Default is #2 10 µm He) before turning on the gun. Choose the aperture type based on the gas you will use.
    2. In gas control, Select helium and allow gas pressure to stabilize.
    3. Set landing energy (default 30 kV)
    4. Set Spot Control to achieve the beam current for the intended work (default 1.1 pA).
    5. Enable Lens 2 power, increase Lens 2 voltage gradually using the GUI slider in the software or the focus knob on keyboard. **Check the leakage current of Lens 2 when powering up. Do not exceed 0.5 µA**
    6. Increase the Lens 2 voltage so that the rough focus is achieved. Working distance showing below the image window should be ~9.5 mm. Lens 2 voltage should be ~19000 V to achieve the rough focus.

## Check trimer status

1. Stay on the standard Au sample / saved reference site.
2. Keep the rough focus at 9.5 mm working distance, field of view 100 microns, and use a short dwell time (1 - 2 us).
3. Enter SFIM mode by clicking the SFIM/Normal button on keyboard. Grab an image by clicking grab on keyboard or grab button under the imaging tab.
4. Image shows at the center of the ZEN window. Check whether the designated trimer atom is centered; use Gun Tilt if adjustment is required. Adjust gun tilt in GFIS options or use the x-y knobs on keyboard while in Gun tilt mode. Check the adjustment mode at the bottom right corner. Click the Mode button on keyboard to toggle between Gun tilt and Gun shift. 
5. Confirm the tilt is corrected. Beam current should reach a maximum value at the correct tilt position, and the trimer atom appears at the center of the crosshair. If the beam tilt exeeds ±200 µrad, the aperture housing needs to be manually corrected. Contact a superuser.
6. Expose the trimer as briefly as possible, then return to normal imaging and Gun Shift mode.

> **WARNING**  
> Operator boundary: 
> Do not use Extract Voltage as an ordinary user control unless explicitly trained/authorized.
