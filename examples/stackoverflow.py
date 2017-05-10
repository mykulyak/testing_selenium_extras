#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example illustrates how to use this library
'''

import logging
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from testing_selenium_extras.assertions import AssertionMixin
from testing_selenium_extras.page_objects import PageObject, PageComponent, PageElement


def open_page(address):
    driver = webdriver.Firefox(
        # replace the following with paths to gecko driver and firefox binaries on your machine
        executable_path=r'D:\Projects\WEBDRIVER\geckodriver.exe',
        firefox_binary=FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    )
    driver.get(address)
    return driver


class Header(PageComponent):
    # Page component that declares several elements visible on the page
    # components can contain other components and elements while elements
    # cannot.
    logo = PageElement('.-logo')
    link_questions = PageElement('#nav-questions')
    search_field = PageElement('[name=q]')


class Footer(PageComponent):
    # Page component that declares one element
    copyright_label = PageElement('#copyright')


class StackOverflowPage(PageObject):
    # Concrete page object. it can declare components and elements
    header = Header('header.so-header')
    footer = Footer('#footer')


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    assertions = AssertionMixin()
    driver = open_page('http://stackoverflow.com/')

    # one can perform tests about page attributes
    assertions.assert_alert_is_not_present(driver)
    assertions.assert_document_title_equal(driver, 'Stack Overflow')
    assertions.assert_urlhash_equal(driver, '')

    # one can wait until page object is loaded
    page = StackOverflowPage.load(driver)

    # one can reference single elements and groups of elements (components), e.g.:
    #   page.header.link_questions
    #   page.footer.element
    print(page.header.link_questions.rect)

    # one can make assertions about element properties
    assertions.assert_element_visible(page.header.link_questions)
    assertions.assert_element_css_class_contains(page.header.link_questions, 'js-gps-track')
    assertions.assert_element_tag_name_equal(page.header.logo, 'a')

    driver.quit()
