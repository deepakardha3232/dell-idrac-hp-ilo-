import requests
import urllib3

urllib3.disable_warnings()

ILO_IP = '192.168.1.101'
USERNAME = 'Administrator'
PASSWORD = 'your_password'

BASE_URL = f"https://{ILO_IP}/redfish/v1"

def get_ilo_resource(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, auth=(USERNAME, PASSWORD), verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {endpoint}: {response.status_code}")
        return {}

def check_system_health():
    data = get_ilo_resource("/Systems/1")
    print("System Health:", data.get("Status", {}).get("Health", "Unknown"))

def check_nic_status():
    ethernet_interfaces = get_ilo_resource("/Systems/1/EthernetInterfaces")
    members = ethernet_interfaces.get("Members", [])
    print("\nNIC Status:")
    for nic in members:
        nic_data = get_ilo_resource(nic["@odata.id"].replace(BASE_URL, ""))
        print(f"  - {nic_data.get('Name', 'NIC')} Status: {nic_data.get('Status', {}).get('Health', 'Unknown')}")

def check_thermal_status():
    thermal_data = get_ilo_resource("/Chassis/1/Thermal")
    sensors = thermal_data.get("Temperatures", [])
    print("\nTemperature Sensors:")
    for sensor in sensors:
        name = sensor.get("Name")
        reading = sensor.get("ReadingCelsius")
        status = sensor.get("Status", {}).get("Health")
        print(f"  - {name}: {reading}°C ({status})")

def check_power_status():
    power_data = get_ilo_resource("/Chassis/1/Power")
    power_supplies = power_data.get("PowerSupplies", [])
    print("\nPower Supplies:")
    for psu in power_supplies:
        name = psu.get("Name")
        status = psu.get("Status", {}).get("Health")
        print(f"  - {name}: {status}")

if __name__ == "__main__":
    print("Connecting to HP iLO...\n")
    check_system_health()
    check_nic_status()
    check_thermal_status()
    check_power_status()
