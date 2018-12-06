#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:18:47 2018

@author: mariya
"""

from htmlparser import HTMLParser

class TestHTMLParser:
    
    def test_parseHTMLParser(self):
        html = HTMLParser()
        html.parse('files/Test.html')
        text = ['page', 'margin', '2cm', 'p', 'margin', '0', '25cm', 
                'direct', 'ltr', 'color', '00000a', 'line', 'height', 
                '115', 'text', 'align', 'left', 'orphan', '2', 'widow',
                '2', 'p', 'western', 'font', 'famili', 'liber', 'serif', 
                'serif', 'font', 'size', '12pt', 'languag', 'ru', 'ru', 
                'p', 'cjk', 'font', 'famili', 'noto', 'san', 'cjk', 'sc', 
                'regular', 'font', 'size', '12pt', 'languag', 'zh', 'cn', 
                'p', 'ctl', 'font', 'famili', 'lohit', 'devanagari', 'font', 
                'size', '12pt', 'languag', 'hi', 'in', 'link', 'languag', 'zxx', 
                'i', 'test', 'poop', 'test', 'anim', 'test', 'anim', 'googl', 
                'link']
        assert html.get_processed_stems() == text
        
    def test_get_linksHTMLParser(self):
        html = HTMLParser()
        html.parse('files/Test.html')
        text = [('google\nlink', 'http://google.com/'), ('google\nlink', 'http://google.com/')]
        assert html.get_links() == text

