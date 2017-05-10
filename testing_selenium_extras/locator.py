# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class Locator(object):
    '''
    A jQuery-like WebElement locator.

    TODO To be copied from CaMon.
    '''

    def __init__(self, driver):
        self._driver = driver

    def parent(self):
        pass

    @classmethod
    def by_id(cls, selector):
        pass

    @classmethod
    def by_xpath(cls, selector):
        pass

    @classmethod
    def by_css(cls, selector):
        pass

    @classmethod
    def by_class_name(cls, selector):
        pass

    @classmethod
    def by_tag_name(cls, selector):
        pass

    @classmethod
    def by_name(cls, selector):
        pass

    @classmethod
    def by_link_text(cls, selector):
        pass

    @classmethod
    def by_partial_link_text(cls, selector):
        pass
