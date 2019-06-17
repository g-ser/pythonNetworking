#!/bin/python

from ncclient import manager
import xml.dom.minidom



with manager.connect(host='192.168.20.158',
                     port=830, #Comware 7 uses port 830 to listen for NETCONF messages
                     username='admin',
                     password='admin',
                     hostkey_verify=False,
                     allow_agent=False,
                     look_for_keys=False
                     ) as netconf_manager:
    vlans_filter = '''
                     <top xmlns="http://www.hp.com/netconf/data:1.0">
                          <VLAN>
                              <VLANs>
                              </VLANs>
                          </VLAN>
                      </top>
                   '''
    #load configuration into running datastore
    data = netconf_manager.get(('subtree', vlans_filter))

#print
xmlstr = xml.dom.minidom.parseString(str(data))
pretty_xml_as_string = xmlstr.toprettyxml()
print pretty_xml_as_string