#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 00:17:45 2018

@author: mariya
"""

from docxparser import DocxParser

class TestDocxParser:

    def test_DocxParser(self):
        docx = DocxParser()
        docx.parse('files/Test.docx')
        text = ['i', 'test', 'poop', 'test', 'anim', 'test', 'anim', 'googl', 'link']
        assert docx.get_processed_stems() == text
