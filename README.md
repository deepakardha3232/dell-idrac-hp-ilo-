# dell-idrac-hp-ilo-
# Dell iDRAC & HP iLO Hardware Health Checks
RAID status
Battery health (RAID controller battery or BBU)
NIC card status (link, speed, firmware)

idrac-ilo-hardware-checks/
├── dell/
│ ├── check_raid_idrac.sh
│ ├── check_bbu_idrac.sh
│ ├── check_nic_idrac.sh
├── hp/
│ ├── check_raid_ilo.sh
│ ├── check_bbu_ilo.sh
│ ├── check_nic_ilo.sh

# Dell iDRAC (via RACADM or Redfish API)
- `check_raid_idrac.sh`: Lists all physical and virtual disks, checks status, errors, and predictive failures.
- `check_bbu_idrac.sh`: Checks RAID controller battery health (charging status, voltage, capacity).
- `check_nic_idrac.sh`: Displays NIC card info including speed, firmware version, and link status.

# HP iLO (via SSH or iLO REST API)
- `check_raid_ilo.sh`: Uses `hpssacli` or REST API to fetch logical and physical drive health.
- `check_bbu_ilo.sh`: Reads battery health from the storage controller logs.
- `check_nic_ilo.sh`: Gathers link status, MAC address, and firmware version.

# Requirements

- Dell RACADM CLI or Redfish Tools
- HP iLO REST API access or SSH enabled
- Bash environment
- Access credentials for iDRAC or iLO interfaces
