import requests
from requests.auth import HTTPBasicAuth
from enum import Enum, auto
import json.tool


# suppress the message which comes from the self-signed certificate of ASA
requests.packages.urllib3.disable_warnings()


def sendrequest(verb, headers, url, auth, data=''):
    """
    Helper method used by the methods in ASA class to
    send HTTP-based request to ASA
    """
    try:
        response = requests.request(verb, headers=headers, url=url, verify=False, auth=auth, data=data)
    except requests.exceptions.ConnectionError:
        print('Unable to reach url {0}'.format(url))
        exit(1)

    if response.status_code == 401:
        print(
            "Login request failed.  Status Code {}".format(
                response.status_code
            )
        )
        print("Response body: ")
        print(response.text)
        exit(1)

    return response


class ASA(object):

    """A simple object for interacting with Cisco ASA through its REST API"""

    def __init__(self, address, username, password):
        """
        Setup a new ASA object given address and credentials
        """
        self.address = address
        self.auth = HTTPBasicAuth(username, password)
        self.headers = {"content-type": "application/json", "accept": "application/json"}


    def getAllPhysicalIfaces(self):
        """
        Use the REST API of ASA to Log into and retrieve all physical interfaces
        """
        url = "https://{0}/api/interfaces/physical".format(self.address)
        return sendrequest('GET', self.headers, url, self.auth).json()


    def setDescMgmtIface(self,desc):
        """
        Configures a description for the Management Interface of Cisco ASA
        """
        payload = {
            "kind" : "object#MgmtInterface",
            "interfaceDesc" : "{0}".format(desc)
        }
        url = "https://{0}/api/interfaces/physical/Management0_API_SLASH_0".format(self.address)
        sendrequest('PATCH', self.headers, url, self.auth, json.dumps(payload))

    def createLocalUsr(self, name, password, privilegeLevel):
        """
        Create local user on Cisco ASA
        """
        payload = {
            "kind" : "object#LocalUserObj",
            "name" : "{0}".format(name),
            "password" : "{0}".format(password),
            "privilegeLevel" : "{0}".format(privilegeLevel)
        }

        url = "https://{0}/api/objects/localusers".format(self.address)
        sendrequest('POST', self.headers, url, self.auth, json.dumps(payload))
