#!/usr/bin/env python
from lxml import etree
data = etree.parse("initialConfigData.xml")
xslt = etree.parse("configurationTemplate.xsl")
transform = etree.XSLT(xslt)
config = transform(data)
commands = []
xslResultTreeToStr = str(config)
commands = list(map(str.strip, xslResultTreeToStr.split('\n')))
#remove <?xml version="1.0"?> from list which is the 1st element
commands = commands[1:]
#remove any None elements
commands = list(filter(None, commands))

for command in commands:
    print(command)
