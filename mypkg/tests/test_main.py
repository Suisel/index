#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:34:30 2018

@author: mariya
"""

from main import pdfminer, pdf, docx, docx_xml, doc_ole, html

class TestMain:
    
    def test_pdfminer(self):
        assert pdfminer() == None
        
    def test_pdf(self):
        assert pdf() == None
        
    def test_docx(self):
        assert docx() == None
        
    def test_docx_xml(self):
        assert docx_xml() == None
        
    def test_doc_ole(self):
        assert doc_ole() == None
        
    def test_html(self):
        assert html() == None
