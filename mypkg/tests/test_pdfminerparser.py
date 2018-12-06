#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:04:29 2018

@author: mariya
"""

from pdfminerparser import PDFMinerParser

class TestPDFMinerParser:
    
    def test_PDFMinerParser(self):
        pdf = PDFMinerParser()
        pdf.parse('files/Test.pdf')
        text = ['i', 'test', 'poop', 'test', 'anim', 'test', 'anim', 'googl', 'link']
        assert pdf.get_processed_stems() == text
