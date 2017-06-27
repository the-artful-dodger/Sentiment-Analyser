# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

class CommentParser(HTMLParser):
    def init_parser(self):
        self.dataflag = 0
        self.data_container = ''
        self.data_list = []

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if 'comment' in attr[1]:
                    self.dataflag = 1
        self.data_container = tag

    def handle_data(self, data):
        if self.dataflag == 1:
            self.data_list.append(data)
            #self.dataflag = 0

    def handle_endtag(self, tag):
        if self.data_container == tag:
            self.dataflag = 0


class Parser(HTMLParser):
    def init_parser(self):
        self.data_list = []

    def handle_data(self, data):
        self.data_list.append(data)

