<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/">
      <xsl:for-each select="config/interfaces/interface">
      interface <xsl:value-of select="name"/>
        ip address <xsl:value-of select="ipv4addr"/>
        description <xsl:value-of select="description"/>
      </xsl:for-each>
      hostname <xsl:value-of select="config/hostname"/>
</xsl:template>
</xsl:stylesheet>
