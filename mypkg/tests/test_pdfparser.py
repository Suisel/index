#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:05:43 2018

@author: mariya
"""

from pdfparser import PDFParser

class TestPDFParser:
    
    def test_PDFParser(self):
        pdf = PDFParser()
        pdf.parse('files/Test.pdf')
        text = []
        assert pdf.get_processed_stems() == text