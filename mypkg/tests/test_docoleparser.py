#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:30:15 2018

@author: mariya
"""

from docoleparser import DocOleParser

class TestDocOleParser:
    
    def test_DocOleParser(self):
        doc_ole = DocOleParser()
        doc_ole.parse('files/Test.doc')
        text = ['m', '0', 'caolan80', '5', 'l', 'f', 'f', 'f', 'z', 'f', 'r', 'b', 'i', 'm', 't', 'e', 's', 't', 'h', 'e', 'r', 'e', 'p', 'o', 'o', 'p', 's', 't', 'e', 's', 't', 'n', 'm', 'l', 's', 't', 'e', 's', 't', 's', 'n', 'm', 'l', 's', 'o', 'm', 'e', 't', 'h', 'n', 'g', 'h', 'y', 'p', 'e', 'r', 'l', 'i', 'n', 'k', 'h', 't', 't', 'p', 'g', 'o', 'o', 'g', 'l', 'e', 'c', 'o', 'm', 'g', 'o', 'o', 'g', 'l', 'e', 'l', 'n', 'k', 'z', '0j', 'j', 'u', 'u', '3', '0', 'a', 'n', 'n', 'n', 'n', '2p', '1d', '0p', '3p', '2', '0']
        assert doc_ole.get_processed_stems() == text
        