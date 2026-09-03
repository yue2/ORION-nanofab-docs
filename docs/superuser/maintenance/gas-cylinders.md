---
title: "Gas Cylinders"
access: superuser
category: superuser
owner: HIM Superuser
status: draft
last-reviewed: 2026-08-31
sources:
  - "HIM_superuser_maintenance.pdf"
  - "ZEISS_ORION_NanoFab_Operator_Manual_Rev2.pdf"
revision: "0.1"
nav_previous: "LN₂ System"
nav_previous_path: "./superuser/maintenance/ln2-system.md"
nav_next_path: "./superuser/maintenance/trimer-formation.md"
nav_next: "Trimer Formation"
---
# Gas Cylinders

Gas cylinders are stored in the backroom of the HIM lab. There are 3 cylinder slots, one for compressed zero air (CDA), one for dry N₂, the other one for storing a spare zero air cylinder. 

1. Compressed zero air is used for column valves and dry N₂ for load-lock purge.
2. Pressure monitor is on the back of the base of the machine. An LCD window shows 2 values, the upper one being compressed air, and the lower one being N₂. 
3. Monitor local pressure indications weekly. Normal pressure range for CDA is 80 - 90 psi, N₂ is 9 - 13 psi. 
4. When cylinder pressure is lower than 200 psi, prepare to order new cylinders. Cylinders are delivered on Mondays, Wednesdays, and Fridays only, so place the order in advance so the new cylinder arrives before the current one runs out. 
5. When cylinder pressure is lower than 100 psi, change to a new cylinder. One CDA cylinder typically lasts one month, N₂ cylinder can be longer.
5. When gas pressure is out of range, a warning message appears in the Vacuum Dashboard window from the main PC. Check the cylinder gauge to determine if changing new cylinder is required. If cylinder pressure is > 200 psi but gas pressure shows lower than the normal range, tune the regulator to the normal pressure.

## Replace gas cylinders

1. Before disconnecting, suspend the air table. In Vacuum Dashboard, click the Air Lock and Chamber tab, right click the air table icon below Chamber -> Turn Off. This prevents a sudden pressure drop from dropping the table while the supply is disconnected.
2. In the back room, close the cylinder valve and exchange the cylinder using a spanner. Follow the site manifold sequence: decrease the regulator (valve 1) to relieve the line, then shut the main valve (valve 2) fully before loosening the connection.
3. Perform the static pressure leak check: open the main valve to see the pressure reading rise, then close it again immediately. Monitor the gauge for one minute. If the reading is stable, there is no leak; open the main valve fully.
4. Increase the regulator (valve 1) to ~85 psi and confirm the main-chamber CA reading is around 86 psi. For the N₂ line, confirm the reading is back in its normal range.
5. Re-check pressure over the following 3 days; if pressure drops too quickly, repeat the leak check.
