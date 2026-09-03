---
title: "LN₂ System"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-09-03
sources:
  - "HIM_superuser_maintenance.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
nav_previous: "Routine Checks"
nav_previous_path: "./routine-checks.md"
nav_next_path: "./gas-cylinders.md"
nav_next: "Gas Cylinders"
---
# LN₂ System

The integrated Dewar cools the GFIS gun to cryogenic temperature and is automatically refilled from an external transfer tank twice a day (8 am and 8 pm). The external tank itself is refilled by the LN₂ supplier about every 16 days (roughly 2 weeks).

Delivery needs to be scheduled at least one day in advance.

1. Before the supplier exchanges the external tank, put the Dewar into Service mode so Auto Fill cannot start while the tank is disconnected. In ZEN software, click the Dewar Fill icon on the top menu bar to open the Dewar Control tool panel, then click Begin Servicing at the bottom of the panel.
2. Make sure the GFIS column is in standby mode when moving the tank because movement can disturb the beam. User can continue to use the tool when the tank is moved out of the room.
3. After refill/reconnection, verify the external tank outlet valve and the transfer-line valves are open. The delivery personnel will help you to open the valves. Do not attempt on your own without proper PPE.
4. Click Done Servicing in Dewar Control to restore automatic refill. Do not leave the tool in Service mode after the exchange: while servicing mode is active the Dewar does not fill and the emergency fill is suppressed, so the Dewar can run out and the gun will warm up if the mode is left on (ZEISS §4.5, printed p. 79; §4.8.4–4.8.5, printed p. 88).
5. Sign the delivery order with signature and date. Hand the singed copy to Mr. Teo for billing purposes.

> **WARNING**  
> **Cryogenic hazard** Follow institutional LN₂ handling rules and the ZEISS safety labels/MSDS guidance.
