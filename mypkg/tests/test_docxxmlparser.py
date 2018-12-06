#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:11:16 2018

@author: mariya
"""

from docxxmlparser import DocxXMLParser

class TestDocxXMLParser:
    
    def test_DocxXMLParser(self):
        docx_xml = DocxXMLParser()
        docx_xml.parse('files/Test.docx')
        text = ['i', 'test', 'poop', 'test', 'anim', 'test', 'anim', 'googl', 'link']
        assert docx_xml.get_processed_stems() == text