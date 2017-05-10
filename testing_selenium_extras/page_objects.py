# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class PageElement(object):
    '''
    Descriptor that references a single WebElement on a page.
    '''

    def __init__(self, locator):
        self.locator = locator

    def __get__(self, instance, owner):
        '''
        Magic allowing referencing components and their elements using dot notation.
        '''
        if isinstance(instance, PageObject):
            return instance.driver.find_element_by_css_selector(self.locator)
        elif isinstance(instance, PageComponent):
            return instance.element.find_element_by_css_selector(self.locator)
        else:
            raise TypeError('PageObject or PageComponent expected')

    def __set__(self, instance, value):
        raise AttributeError('This is a read-only descriptor')


class PageComponent(object):
    '''
    Descriptor that describes a part of the page. Can itself contain descriptors to
    elements and other components.
    '''

    def __init__(self, element):
        self.element = element

    def __get__(self, instance, owner):
        '''
        Magic allowing referencing components and their elements using dot notation.
        '''
        if isinstance(instance, PageComponent):
            parent = instance.element.parent
        elif isinstance(instance, PageObject):
            parent = instance.driver
        else:
            raise TypeError('PageObject or PageComponent expected')
        return self.__class__(parent)

    def __set__(self, instance, value):
        raise AttributeError('This is a read-only descriptor')

    def wait_to_load(self):
        '''
        Waits until all elements declared in this component are found in DOM.
        '''
        descriptor_dict = self.__class__.__dict__
        for attr, value in descriptor_dict.items():
            if isinstance(value, PageElement):
                getattr(self, attr)
            elif isinstance(value, PageComponent):
                component = getattr(self, attr)
                component.wait_to_load()


class PageObject(object):
    '''
    Describes a whole page.
    '''

    def __init__(self, driver):
        self.driver = driver

    def wait_to_load(self):
        '''
        Waits until all components and elements are found on the page.
        '''
        descriptor_dict = self.__class__.__dict__
        for attr, value in descriptor_dict.items():
            if isinstance(value, PageElement):
                getattr(self, attr)
            elif isinstance(value, PageComponent):
                component = getattr(self, attr)
                component.wait_to_load()

    @classmethod
    def load(cls, driver):
        result = cls(driver)
        result.wait_to_load()
        return result
