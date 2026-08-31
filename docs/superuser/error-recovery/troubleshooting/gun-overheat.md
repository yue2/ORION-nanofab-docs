---
title: "Gun Overheat"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "HIM_overheat.pdf"
revision: "0.1"
---
# Gun Overheat

## Symptom

When the gun temperature value in the vacuum screen exceeds 95K.

## Possible causes

- LN2 supply has been exhausted
- During a Dewar refill. A Dewar fill can temporarily raise gun temperature before it returns to normal.

## What to do

1. In case of a scheduled Dewar refill (8 am or 8 pm every day), do not use the tool. Avoid starting GFIS from 6 am (pm) to 830 am (pm)
2. In case of exhausted LN2 supply, meaning that the main tank is depleted but the next delivery has not arrived.
  1. In Service Machine → Power Distribution, disable accelerator, Lens 1 and extractor.
  1. Physically isolate the documented HVP connections only if trained/authorized.
  2. When LN2 is delivered, connect the heating cable and start the bake and cool process.
  1. After completion, reconnect, remove heating cable, run GFIS source repair/degas, then form source and trimer.

> **WARNING**  
> High voltage This is restricted maintenance. Follow lockout/site electrical safety requirements.

## Logic review — unresolved source gaps
  
> **Manual references:** §7.4.3 Column Maintenance and §7.4.4 Gun Temperature, printed pp. **160–161** (PDF pages **165–166**); §7.4.5 Dewar Issues, printed pp. **161–164** (PDF **166–169**).  
> **Waiting for confirmation:** the Operator Manual does **not** confirm the local note's physical HVP-disconnection/heating-cable sequence or its bake completion criteria. Confirm whether that intrusive local recovery is still required, and if so document heater connection, bake recipe/duration, completion indication, electrical isolation and reconnection criteria from the applicable service procedure.

