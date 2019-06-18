import json
import requests
from requests.auth import HTTPBasicAuth

# suppress the message which comes from the self-signed certificate of Nexus Switch
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    switchuser = 'admin'
    switchpassword = 'admin'
    switchmgmtip='192.168.20.99'
    auth = HTTPBasicAuth(switchuser, switchpassword)
    myheaders = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    url='https://{0}/ins'.format(switchmgmtip)
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": 'show version',
            "output_format": "json"
        }
    }
    response = requests.post(url, data=json.dumps(payload), headers=myheaders, auth=auth, verify=False)

    print(response.json())