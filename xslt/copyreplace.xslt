<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fn="http://www.w3.org/2005/xpath-functions">
	<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:strip-space elements="*"/>
	
	<xsl:param name="i" select="1"/>
	<xsl:param name="testValue" select="100"/>
	
	<xsl:template match="node()|@*">
	   <xsl:param name="i" />
		<xsl:choose>
			<xsl:when test="name() ='OrderID'  ">
			<xsl:copy>
			<xsl:value-of select="$i+1119"/>
			</xsl:copy>
			</xsl:when>
			<xsl:otherwise>
			<xsl:copy>
				<xsl:apply-templates select="node()|@*">
			   <xsl:with-param name="i" select="$i"/>
			</xsl:apply-templates>
			</xsl:copy>
			</xsl:otherwise>
		</xsl:choose>		
		
	</xsl:template>
	
  <xsl:template match="/Orders/Order[2]">
	<!-- without [1] the result will become to 0 -->
		<xsl:apply-templates select="node()|@*">
			<xsl:with-param name="i" select="101"/>
			</xsl:apply-templates>
	</xsl:template>
	
	<xsl:template match="/Orders/Order[1]">
	<!-- without [1] the result will become to 198 -->

		<xsl:call-template name="for-loop">
			<xsl:with-param name="i" select="count(/Orders/Order)"/>
			<xsl:with-param name="testValue" select="100"/>
		</xsl:call-template>
	</xsl:template>
		<!-- 
	<xsl:template match="/Orders/Order/OrderHeader/OrderID/text()">
		<xsl:value-of select="count(ancestor::Order/preceding-sibling::Order)+1121"/>
	</xsl:template>
	 -->
	<xsl:template name="for-loop">
		<xsl:param name="i"/>
		<xsl:param name="testValue" />
		<xsl:copy>
			<xsl:apply-templates select="node()|@*">
			<xsl:with-param name="i" select="$i"/>
			</xsl:apply-templates>
		</xsl:copy>
		<xsl:if test="$i &lt; $testValue">
			<xsl:call-template name="for-loop">
				<xsl:with-param name="i" select="$i + 1"/>
				<xsl:with-param name="testValue" select="$testValue"/>
			</xsl:call-template>
		</xsl:if>
	</xsl:template>
	
</xsl:stylesheet>
