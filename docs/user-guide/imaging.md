---
title: "Imaging"
access: all-users
category: user-guide
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-02
sources:
  - "Local_ORION_NanoFab_SOP.docx"
  - "SOP_ORION_NanoFab_He_Ne_Users.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
nav_previous: "Starting a Session"
nav_previous_path: "./user-guide/starting-session.md"
nav_next_path: "./user-guide/patterning.md"
nav_next: "Patterning"
---
# Imaging

## Tuning focus

Tune on a standard sample where possible to minimize exposure of the specimen.

1. Set landing energy to your designed value. Set aperture and spot control so that the beam current reaches your designed value.
2. In normal imaging mode, using a relatively fast scan (1 - 5 us dwell time), start continuous scan.
3. Adjust magnification and focus.
4. Adjust beam shift:
    1. In GFIS settings, find Lens 2 section. Start wobble, choose small or medium. Use a faster scan (0.5 - 1 us) to observe the wobble more clearly. 
    2. Make sure the status bar shows beam shift before using the x-y knobs to correct the beam shift. 
     3. When the beam shift values exceed ±200 µrad, the electrical adjustment is not sufficient. Zero the X/Y beam shift, then go to aperture settings in the GFIS tab and adjust the aperture position to minimize the wobble. Click save to save the aperture position (ZEISS §5.3.3, printed p. 128 / PDF p. 133).
	  4. Turn off Lens 2 wobble.
5. Adjust astigmatism:
	  1. Zoom in to the edge of a feature. Adjust the stigmator knobs on the keyboard to make the edges sharp.
	  2. Take note of the stigmator values in GFIS settings as a reference point.

- Repeat 3 -5 when necessary to achieve a good image focus.

## Imaging your sample

1. Navigate to the region of interest and use Continuous scanning for setup. The stage can tilt -5° to +54°.
2. Set the desired dwell time and scan size.
3. At a flat region, iteratively correct astigmatism, Gun Shift/wobbler and focus.
4. For capture, go to the Scan Parameters in the left column. Set up a high quality scan. Suggested parameters: 1024x1024 px, line averaging 4 - 6, 2 - 5 µs dwell time. Increase dwell time and/or line averaging when higher quality is required.
5. Stop continuous scan, then use Grab to take the image.
6. Save the image to the designated data location.

## Using flood gun

Use the flood gun to aid imaging non-conductive samples.

> **WARNING**  
> Before powering up the flood gun, verify the ET detector grid is not shorted: set the grid to 0 V and confirm the image darkens and shifts, then restore 500 V (ZEISS §4.9, printed pp. 88–89 / PDF pp. 93–94). If the grid voltage has no effect, **do not power up the flood gun** — contact a superuser; a shorted grid can allow flood electrons to damage the ET scintillator.

1. In ZEN top menu, open Power Systems window. Turn on flood gun.
2. From the left column of ZEN, find Flood Gun settings. Click show all to expand the setting options.
3. Set flood gun mode to line.
4. Keep default flood gun energy. Default flood time is 200 ms. Tune the flood time to longer if the imaging contrast is not satisfactory. Grid delay time should be >= flood time.
5. Toggle the deflection x-y in flood gun window to optimize contrast.
6. Astigmatism usually needs readjustment while using the flood gun.
