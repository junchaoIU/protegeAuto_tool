#!/usr/bin/python
# -*- coding: UTF-8 -*-

class GA:
    'General axioms的基类'

    def __init__(self, domainName, className, owlLines):
        if(owlLines is None or len(owlLines) == 1):
            # initial DP
            owlLines = []
            owlLines.append('<rdf:Description>')
            owlLines.append('</rdf:Description>')
        self.className = className
        self.domainName = domainName
        self.owlLines = owlLines

    def addDiferentInds(self, indsList):
        lines = self.owlLines
        lines.insert(1, '<rdf:type rdf:resource="http://www.w3.org/2002/07/owl#AllDifferent"/>')
        lines.insert(1, '<owl:distinctMembers rdf:parseType="Collection">')
        for indName in indsList:
            lines.insert(1, '<rdf:Description rdf:about="http://www.owl-ontologies.com/' + self.domainName + '#' + indName + '">')
        lines.insert(1, '</owl:distinctMembers>')
        self.owlLines = lines
        print(lines)