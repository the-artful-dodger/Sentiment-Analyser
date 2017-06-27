from lxml import html
import requests

class Scraper(object):

    @staticmethod
    def get_page(link):
        page = requests.get(link)
        return page

    @staticmethod
    def get_html_tree(page):
        tree = html.fromstring(page.content)
        return tree

    @staticmethod
    def get_data_list(tree, x_path = '//*'):
        data_list = tree.xpath(x_path)
        return data_list

    @staticmethod
    def get_word_list():
        pass

