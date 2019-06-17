#! /usr/bin/env python

from asa import (ASA,asa_login)



# Entry point for program
if __name__ == "__main__":
    # Initialize Cisco ASA Object
    asa = ASA(
        address=asa_login['host'],
        username=asa_login['username'],
        password=asa_login['password']
    )

    print(asa.getAllPhysicalIfaces())

    asa.setDescMgmtIface("Very Ugly Interface")

    asa.createLocalUsr("Georgios","admin","15")



