#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:37:59 2018

@author: mariya
"""

from docxparser import DocxParser

class TestAbstractParser:
        
    def test_get_text(self):
        abstract = DocxParser()
        abstract.parse('files/Test.docx')
        text = "I am test here poops,  Test animals, tests animal something. google link"
        assert abstract.get_text() == text
        
    def test_get_words(self):
        abstract = DocxParser()
        abstract.parse('files/Test.docx')
        text = ['I', 'am', 'test', 'here', 'poops,', 'Test', 'animals,', 'tests', 'animal', 'something.', 'google', 'link']
        assert abstract.get_words() == text
        
    def test_get_stems(self):
        abstract = DocxParser()
        abstract.parse('files/Test.docx')
        text = ['i', 'am', 'test', 'here', 'poops,', 'test', 'animals,', 'test', 'anim', 'something.', 'googl', 'link']
        assert abstract.get_stems() == text
        
    def test_get_processed_text(self):
        abstract = DocxParser()
        abstract.parse('files/Test.docx')
        text = "I test poops Test animals tests animal google link"
        assert abstract.get_processed_text() == text
        
    def test_get_processed_stems(self):
        abstract = DocxParser()
        abstract.parse('files/Test.docx')
        text = ['i', 'test', 'poop', 'test', 'anim', 'test', 'anim', 'googl', 'link']
        assert abstract.get_processed_stems() == text
