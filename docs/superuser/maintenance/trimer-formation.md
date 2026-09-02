---
title: "Trimer Formation"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "HIM_trimer_form.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
---
# Trimer Formation

> **WARNING**  
> Maintenance procedure 
> Only trained Superusers should perform source/trimer formation and high-voltage related recovery.

Trimer refers to the tungsten tip consists of 3 atoms at its apex. He gas is ionized on one of the W atoms to form the He ion beam. Due to continued electrical stress, the atom will pop in 1-2 months, requiring sharpening the W tip to form a new trimer. The remaining 2 atoms can still generate He beam, but the dimer is much more unstable than the trimer. 

When the W tip is in the dimer state, the tool can still be used but superusers are advised to schedule a new trimer formation soon.

1. Move the stage to the standard Au sample. Power up ET detector. Place GFIS in Standby.
2. Maintenance → GFIS → Form the source; run the documented source-build recipe.
3. Start trimer selection and observe in SFIM.
4. Adjust accelerator/extractor/Lens 1 according to the local maintenance record until the three-atom structure is resolved.
5. Determine BIV by measuring trimer intensity and tuning extractor for maximum intensity.
6. Mechanically align the source and set source distance.
7. Capture a final screenshot and record BIV/maintenance details.

See HIM trimer form.pdf and ZEISS manual §5.2.
