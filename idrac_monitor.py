import requests
import urllib3
urllib3.disable_warnings()

IDRAC_IP = '192.168.1.100'
USERNAME = 'root'
PASSWORD = '*****'

def fetch_idrac_health():
    url = f"https://{IDRAC_IP}/redfish/v1/Systems/System.Embedded.1"
    response = requests.get(url, auth=(USERNAME, PASSWORD), verify=False)
    if response.status_code == 200:
        data = response.json()
        print("System Health:", data.get('Status', {}).get('Health'))
    else:
        print("Failed to fetch iDRAC data")

if __name__ == "__main__":
    fetch_idrac_health()
